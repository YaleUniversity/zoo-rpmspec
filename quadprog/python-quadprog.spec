# Created by pyp2rpm-3.3.2
%global pypi_name quadprog

Name:           python-%{pypi_name}
Version:        0.1.7
Release:        1%{?dist}
Summary:        Quadratic Programming Solver

License:        GPLv2+
URL:            https://github.com/rmcgibbo/quadprog
Source0:        https://files.pythonhosted.org/packages/source/q/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools) >= 18.0
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
Minimize 1/2 x^T G x - a^T xSubject to C.T x > bThis routine uses the the
Goldfarb/Idnani dual algorithm [1].References - 1) D. Goldfarb and A. Idnani
(1983). A numerically stable dual method for solving strictly convex quadratic
programs. Mathematical Programming, 27, 1-33.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(cython)
%description -n python3-%{pypi_name}
Minimize 1/2 x^T G x - a^T xSubject to C.T x > bThis routine uses the the
Goldfarb/Idnani dual algorithm [1].References - 1) D. Goldfarb and A. Idnani
(1983). A numerically stable dual method for solving strictly convex quadratic
programs. Mathematical Programming, 27, 1-33.


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
%{python3_sitearch}/quadprog.cpython-37m-x86_64-linux-gnu.so
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Apr 20 2020 Mahmood Adil - 0.1.7-1
- Initial package.
