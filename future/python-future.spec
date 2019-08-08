# Created by pyp2rpm-3.3.2
%global pypi_name future

Name:           python-%{pypi_name}
Version:        0.17.1
Release:        1%{?dist}
Summary:        Clean single-source support for Python 3 and 2

License:        MIT
URL:            https://python-future.org
Source0:        https://files.pythonhosted.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
future: Easy, safe support for Python 2/3 compatibility future is the missing
compatibility layer between Python 2 and Python 3. It allows you to use a
single, clean Python 3.x-compatible codebase to support both Python 2 and
Python 3 with minimal overhead.It is designed to be used as follows:: from
__future__ import (absolute_import, division, print_function, unicode_literals)
from builtins...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
future: Easy, safe support for Python 2/3 compatibility future is the missing
compatibility layer between Python 2 and Python 3. It allows you to use a
single, clean Python 3.x-compatible codebase to support both Python 2 and
Python 3 with minimal overhead.It is designed to be used as follows:: from
__future__ import (absolute_import, division, print_function, unicode_literals)
from builtins...

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
# PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
# rm -rf html/.{doctrees,buildinfo}

%install
%py3_install


%files -n python3-%{pypi_name}
%license docs/_themes/LICENSE LICENSE.txt
%doc README.rst
%{_bindir}/futurize
%{_bindir}/pasteurize
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/libfuturize
%{python3_sitelib}/libpasteurize
%{python3_sitelib}/past
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Aug 07 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 0.17.1-1
- Initial package.
