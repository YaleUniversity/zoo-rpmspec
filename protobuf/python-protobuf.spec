# Created by pyp2rpm-3.3.2
%global pypi_name protobuf

Name:           python-%{pypi_name}
Version:        3.6.1
Release:        1%{?dist}
Summary:        Protocol Buffers

License:        3-Clause BSD License
URL:            https://developers.google.com/protocol-buffers/
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.9

%description
Protocol Buffers are Google's data interchange format

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(setuptools)
Requires:       python3dist(six) >= 1.9
%description -n python3-%{pypi_name}
Protocol Buffers are Google's data interchange format


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
%{python3_sitelib}/google
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?-*.pth
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Aug 15 2018 Grace Petegorsky <grace.petegorsky@yale.edu> - 3.6.1-1
- Initial package.