%global pypi_name tensorflow

Name:           python-%{pypi_name}-gpu
Version:        1.8.0
Release:        1%{?dist}
Summary:        TensorFlow helps the tensors flow

License:        Apache 2.0
URL:            http://tensorflow.org/
# https://www.tensorflow.org/install/install_linux#the_url_of_the_tensorflow_python_package
Source0:        https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-%{version}-cp36-cp36m-linux_x86_64.whl
BuildArch:      x86_64
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-devel
BuildRequires:  python3-mock >= 2.0.0
BuildRequires:  python3-numpy >= 1.11.0
BuildRequires:  python3-protobuf >= 3.2.0
BuildRequires:  python3-scipy >= 0.15.1
BuildRequires:  python3-wheel
BuildRequires:  python3-pip

%description
TensorFlow is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) that flow between them. This flexible architecture lets you deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device without rewriting code. TensorFlow also includes TensorBoard, a data visualization toolkit.

%package -n     python3-%{pypi_name}-gpu
Summary:        TensorFlow helps the tensors flow
%{?python_provide:%python_provide python3-%{pypi_name}-gpu}
 
Requires:       python3-six >= 1.10.0
Requires:       python3-mock >= 2.0.0
Requires:       python3-numpy >= 1.11.0
Requires:       python3-protobuf >= 3.2.0
Requires:       python3-wheel
# assumes http://negativo17.org/nvidia-driver/
Requires:       cuda-devel => 8.0
Requires:       cuda < 9.1
Requires:       cuda-cudnn-devel => 5.0
# can't have both GPU and CPU-only versions installed simultaneously
Conflicts:      python3-tensorflow
%description -n python3-%{pypi_name}-gpu
tensorflow-gpu for python3 (CUDA)

%prep

%build

%install
pip3 install --no-deps --disable-pip-version-check -I %{SOURCE0} --root %{buildroot} --strip-file-prefix %{buildroot}
rm -rf %{buildroot}/%{python3_sitelib}/external
# fix for wheel package weirdness installing to inconsistent package/directory names ("tensorflow" versus "tensorflow-gpu" versus "tensorflow_gpu")
mv %{buildroot}/%{python3_sitearch}/%{pypi_name}_gpu-%{version}.dist-info %{buildroot}/%{python3_sitelib}/%{pypi_name}-%{version}.dist-info

%check

%files -n python3-%{pypi_name}-gpu
%{_bindir}/freeze_graph
%{_bindir}/saved_model_cli
%{_bindir}/tensorboard
%{_bindir}/toco
%{_bindir}/toco_from_protos
%{python3_sitelib}/%{pypi_name}*


%changelog
* Mon Apr 30 2018 David Goerger - 1.8.0-1
- update to 1.8.0

* Mon Apr 02 2018 David Goerger - 1.7.0-1
- update to 1.7.0
- deprecate python2 flavour

* Wed Nov 08 2017 David Goerger - 1.4.0-1
- update to latest

* Thu Apr 27 2017 David Goerger - 1.1.0
- update to latest

* Wed Dec 14 2016 David Goerger - 0.12.0rc1-1
- package tensorflow-gpu
