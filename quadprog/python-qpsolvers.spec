# Created by pyp2rpm-3.3.2
%global pypi_name qpsolvers

Name:           python-%{pypi_name}
Version:        1.4
Release:        1%{?dist}
Summary:        Quadratic Programming solvers for Python with a unified API

License:        LGPL
URL:            https://github.com/stephane-caron/qpsolvers
Source0:        https://files.pythonhosted.org/packages/source/q/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This module provides a single function solve_qp(P, q, G, h, A, b, solverX) with
a *solver* keyword argument to select the backend solver. The quadratic program
it solves is, in standard form: .. figure:: vector inequalities are taken
coordinate by coordinate.Solvers The list of supported solvers currently
includes:- Dense solvers: - CVXOPT < - qpOASES < - quadprog < - Sparse solvers:
- ECOS <

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files 
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Jul 15 2020 Mahmood Adil - 1.4-1
* Mon Apr 20 2020 Mahmood Adil - 1.1-1
- Initial package.
