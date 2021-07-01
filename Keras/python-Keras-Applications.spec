# Created by pyp2rpm-3.3.6
%global pypi_name Keras_Applications

Name:           python-%{pypi_name}
Version:        1.0.8
Release:        1%{?dist}
Summary:        Reference implementations of popular deep learning models

License:        MIT
URL:            https://github.com/keras-team/keras-applications
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(numpy) >= 1.9.1
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-pep8)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(setuptools)

%description
Keras Applications is the applications module of the Keras deep learning
library. It provides model definitions and pre-trained weights for a number of
popular archictures, such as VGG16, ResNet50, Xception, MobileNet, and
more.Read the documentation at: Applications may be imported directly from an
up-to-date installation of Keras: from keras import applications Keras
Applications is...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(h5py)
Requires:       python3dist(numpy) >= 1.9.1
Requires:       python3dist(pytest)
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-pep8)
Requires:       python3dist(pytest-xdist)
%description -n python3-%{pypi_name}
Keras Applications is the applications module of the Keras deep learning
library. It provides model definitions and pre-trained weights for a number of
popular archictures, such as VGG16, ResNet50, Xception, MobileNet, and
more.Read the documentation at: Applications may be imported directly from an
up-to-date installation of Keras: from keras import applications Keras
Applications is...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/keras_applications
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Jul 01 2021 Michael Dunlap <michael.dunlap@yale.edu>
 - 1.0.8-1
