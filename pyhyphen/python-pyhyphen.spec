# Created by pyp2rpm-3.3.2
%global pypi_name pyhyphen
%global camelcase_name PyHyphen

Name:           python-%{pypi_name}
Version:        3.0.1
Release:        1%{?dist}
Summary:        The hyphenation library of LibreOffice and FireFox wrapped for Python

License:        None
URL:            https://bitbucket.org/fhaxbox66/pyhyphen
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/PyHyphen-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 PyHyphen - hyphenation for Python (c) 2008-2017 Dr. LeoContact:
fhaxbox66@googlemail.comProject home: list: .. contents::0. Quickstart :: $ pip
install pyhyphen $ echo "long sentences and complicated words are
flabbergasting" | wraptext -w 10 - long sen- tences and compli- cated words are
flabber- gasting 1. Overview PyHyphen is a pythonic interface to the
hyphenation C library used in...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(appdirs)
Requires:       python3dist(setuptools)
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
 PyHyphen - hyphenation for Python (c) 2008-2017 Dr. LeoContact:
fhaxbox66@googlemail.comProject home: list: .. contents::0. Quickstart :: $ pip
install pyhyphen $ echo "long sentences and complicated words are
flabbergasting" | wraptext -w 10 - long sen- tences and compli- cated words are
flabber- gasting 1. Overview PyHyphen is a pythonic interface to the
hyphenation C library used in...


%prep
%autosetup -n %{camelcase_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/wraptext
%{python3_sitearch}/hyphen
%{python3_sitearch}/textwrap2
%{python3_sitearch}/%{camelcase_name}-%{version}-py?.?.egg-info

%changelog
* Fri Aug 02 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 3.0.1-1
- Initial package.
