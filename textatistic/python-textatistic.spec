# Created by pyp2rpm-3.3.2
%global pypi_name textatistic

Name:           python-%{pypi_name}
Version:        0.0.1
Release:        1%{?dist}
Summary:        Calculate readability scores (Flesch Reading Ease, etc

License:        Apache 2.0
URL:            http://www.erinhengel.com/software/textatistic/
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Textatistic
===========

Textatistic is a Python package to calculate the
`Flesch Reading Ease
<https://en.wikipedia.org/wiki/Flesch&#8211;Kincaid_readability_tests>`_,
`Flesch-Kincaid
<https://en.wikipedia.org/wiki/Flesch&#8211;Kincaid_readability_tests>`_,
`Gunning Fog <https://en.wikipedia.org/wiki/Gunning_fog_index>`_, `Simple
Measure of Gobbledygook <https://en.wikipedia.org/wiki/SMOG>`_...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(pyhyphen) >= 2.0.5
%description -n python3-%{pypi_name}
Textatistic
===========

Textatistic is a Python package to calculate the
`Flesch Reading Ease
<https://en.wikipedia.org/wiki/Flesch&#8211;Kincaid_readability_tests>`_,
`Flesch-Kincaid
<https://en.wikipedia.org/wiki/Flesch&#8211;Kincaid_readability_tests>`_,
`Gunning Fog <https://en.wikipedia.org/wiki/Gunning_fog_index>`_, `Simple
Measure of Gobbledygook <https://en.wikipedia.org/wiki/SMOG>`_...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed May 01 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 0.0.1-1
- Initial package.