# Created by pyp2rpm-3.2.1
%global pypi_name xlsx2csv

Name:           python-%{pypi_name}
Version:        0.7.6
Release:        1%{?dist}
Summary:        xlsx to csv converter

License:        TODO
URL:            http://github.com/dilshod/xlsx2csv
Source0:        https://files.pythonhosted.org/packages/source/x/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description

xlsx to csv converter (http://github.com/dilshod/xlsx2csv)

Converts xslx
files to csv format.
Handles large XLSX files. Fast and easy to use.
Installation:
  sudo easy_install xlsx2csv
  or
  pip install xlsx2csv

Usage:
xlsx2csv.py [-h] [-v] [-a] [-d DELIMITER] [-f DATEFORMAT] [-i] [-e]
[-p SHEETDELIMITER] [-s SHEETID] [--hyperlinks]
              [-I
INCLUDE_SHEET_PATTERN] ...

%package -n     python3-%{pypi_name}
Summary:        xlsx to csv converter
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}

xlsx to csv converter (http://github.com/dilshod/xlsx2csv)

Converts xslx
files to csv format.
Handles large XLSX files. Fast and easy to use.
Installation:
  sudo easy_install xlsx2csv
  or
  pip install xlsx2csv

Usage:
xlsx2csv.py [-h] [-v] [-a] [-d DELIMITER] [-f DATEFORMAT] [-i] [-e]
[-p SHEETDELIMITER] [-s SHEETID] [--hyperlinks]
              [-I
INCLUDE_SHEET_PATTERN] ...


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc 
%{_bindir}/xlsx2csv
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py*
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Aug 05 2019 Grace Petegorsky - 0.7.6-1
- Update to 0.7.6
* Wed Jan 25 2017 David Goerger - 0.7.2-1
- Initial package.
