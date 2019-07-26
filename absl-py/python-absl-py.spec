# Created by pyp2rpm-3.3.2
%global pypi_name absl-py

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        1%{?dist}
Summary:        Abseil Python Common Libraries, see

License:        Apache 2.0
URL:            https://github.com/abseil/abseil-py
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 Abseil Python Common LibrariesThis repository is a collection of Python
library code for building Python applications. The code is collected from
Google's own Python code base, and has been extensively tested and used in
production. Features* Simple application startup * Distributed commandline
flags system * Custom logging module with additional features * Testing
utilities Getting Started...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
 Abseil Python Common LibrariesThis repository is a collection of Python
library code for building Python applications. The code is collected from
Google's own Python code base, and has been extensively tested and used in
production. Features* Simple application startup * Distributed commandline
flags system * Custom logging module with additional features * Testing
utilities Getting Started...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/absl
%{python3_sitelib}/absl_py-%{version}-py?.?.egg-info

%changelog
* Fri Jul 26 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 0.7.1-1
- Update to 0.7.1

* Wed Aug 15 2018 Grace Petegorsky <grace.petegorsky@yale.edu> - 0.4.0-1
- Initial package.
* Wed Aug 15 2018 Grace Petegorsky <grace.petegorsky@yale.edu> - 0.4.0-1
- Initial package.
