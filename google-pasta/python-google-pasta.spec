# Created by pyp2rpm-3.3.2
%global pypi_name google-pasta

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        1%{?dist}
Summary:        pasta is an AST-based Python refactoring library

License:        Apache 2.0
URL:            None
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3-six 
%description


%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}



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
%doc README.md
%{python3_sitelib}/pasta
%{python3_sitelib}/google_pasta-%{version}-py?.?.egg-info

%changelog
* Fri Jul 26 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 0.1.7-1
- Initial package.
* Fri Jul 14 2020 Adil Mahmood <adil.mahmood@yale.edu> - 0.2.0
