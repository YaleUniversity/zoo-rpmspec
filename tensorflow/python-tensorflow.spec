%global pypi_name tensorflow

Name:           python-%{pypi_name}
Version:        2.5.0
Release:        1%{?dist}
Summary:        TensorFlow helps the tensors flow

License:        Apache 2.0
URL:            http://tensorflow.org/
# https://www.tensorflow.org/install/install_linux#the_url_of_the_tensorflow_python_package
Source0:        https://files.pythonhosted.org/packages/dc/0e/72070fe6d5774bfc6b73e857f1747ba99b95cb808c46b709ab7c9ec757eb/tensorflow-2.5.0-cp39-cp39-manylinux2010_x86_64.whl
BuildArch:      x86_64
 
BuildRequires:  python3-setuptools
BuildRequires:  python3-six >= 1.10.0
BuildRequires:  python3-devel
BuildRequires:  python3-mock >= 2.0.0
BuildRequires:  python3-numpy >= 1.11.0
BuildRequires:  python3-protobuf >= 3.6.0
BuildRequires:  python3-scipy >= 0.15.1
BuildRequires:  python3-absl-py
BuildRequires:  python3-wheel
BuildRequires:  python3-pip

%description
TensorFlow is an open source software library for numerical computation using data flow graphs. Nodes in the graph represent mathematical operations, while the graph edges represent the multidimensional data arrays (tensors) that flow between them. This flexible architecture lets you deploy computation to one or more CPUs or GPUs in a desktop, server, or mobile device without rewriting code. TensorFlow also includes TensorBoard, a data visualization toolkit.

%package -n     python3-%{pypi_name}
Summary:        TensorFlow helps the tensors flow
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-six >= 1.10.0
Requires:       python3-mock >= 2.0.0
Requires:       python3-numpy >= 1.11.0
Requires:       python3-protobuf >= 3.6.0
Requires:       python3-h5py >= 2.8.0
Requires:       python3-wheel
Conflicts:      python3-tensorflow-gpu
%description -n python3-%{pypi_name}
tensorflow for python3

%prep

%build

%install
pip3 install --no-deps --disable-pip-version-check -I %{SOURCE0} --root %{buildroot} 
# fix for wheel package weirdness installing to inconsistent package/directory names
mv %{buildroot}/%{python3_sitearch}/%{pypi_name}-%{version}.dist-info %{buildroot}/%{python3_sitelib}/%{pypi_name}-%{version}.dist-info
rm -rf %{buildroot}/%{python3_sitelib}/external


%check

%files -n python3-%{pypi_name}
%{_bindir}/freeze_graph
%{_bindir}/saved_model_cli
%{_bindir}/tensorboard
%{_bindir}/tf_upgrade_v2
%{_bindir}/tflite_convert
%{_bindir}/toco
%{_bindir}/toco_from_protos
%{python3_sitelib}/%{pypi_name}*


%changelog
* Thu Jul 01 2021 Michael Dunlap <michael.dunlap@yale.edu> 2.5.0
- update to 2.5.0

* Fri Jul 26 2019 Grace Petegorsky <grace.petegorsky@yale.edu> 1.14.0-1
- update to 1.14.0
- new: /usr/bin/tf_upgrade_v2

* Wed Aug 15 2018 Grace Petegorsky <grace.petegorsky@yale.edu> 1.10.0-2
- add dependency on h5py; build dependencies python3-protobuf >= 3.6.0 and python3-absl-py

* Sat Aug 11 2018 David Goerger - 1.10.0-1
- update to 1.10.0
- new: /usr/bin/tflite_convert

* Mon Apr 02 2018 David Goerger - 1.7.0-1
- update to 1.7.0
- deprecate python2 flavour

* Wed Nov 08 2017 David Goerger - 1.4.0-1
- update to 1.4.0

* Fri Nov 11 2016 David Goerger - 0.11.0-1
- Initial package.
