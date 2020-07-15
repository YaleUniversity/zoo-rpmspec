# Created by pyp2rpm-3.3.2
%global pypi_name astor

Name:           python-%{pypi_name}
Version:        0.8.1
Release:        1%{?dist}
Summary:        Read/rewrite/write Python ASTs

License:        BSD-3-Clause
URL:            https://github.com/berkerpeksag/astor
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 astor -- AST observe/rewrite :PyPI: :Documentation: :Source: :License:
3-clause BSD :Build status: astor is designed to allow easy manipulation of
Python source via the AST.There are some other similar libraries, but astor
focuses on the following areas:- Round-trip an AST back to Python [1]_: -
Modified AST doesn't need linenumbers, ctx, etc. or otherwise

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 astor -- AST observe/rewrite :PyPI: :Documentation: :Source: :License:
3-clause BSD :Build status: astor is designed to allow easy manipulation of
Python source via the AST.There are some other similar libraries, but astor
focuses on the following areas:- Round-trip an AST back to Python [1]_: -
Modified AST doesn't need linenumbers, ctx, etc. or otherwise


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
* Fri Jul 26 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 0.8.0-1
- Initial package.
