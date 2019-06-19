# Created by pyp2rpm-3.2.1
%global pypi_name Keras

Name:           python-%{pypi_name}
Version:        2.0.4
Release:        2%{?dist}
Summary:        Deep Learning for Python

License:        MIT
URL:            https://github.com/fchollet/keras
Source0:        https://files.pythonhosted.org/packages/source/K/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
UNKNOWN

%package -n     python2-%{pypi_name}
Summary:        Deep Learning for Python
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-theano
Requires:       PyYAML
Requires:       python-six
%description -n python2-%{pypi_name}
UNKNOWN

%package -n     python3-%{pypi_name}
Summary:        Deep Learning for Python
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-tensorflow
Requires:       python3-PyYAML
Requires:       python3-six
%description -n python3-%{pypi_name}
UNKNOWN


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

%py2_install


%files -n python2-%{pypi_name}
%doc 
%{python2_sitelib}/keras
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc 
%{python3_sitelib}/keras
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed May 03 2017 David Goerger - 2.0.4-2
- Initial package.
