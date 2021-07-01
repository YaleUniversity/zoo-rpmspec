# Created by pyp2rpm-3.3.6
%global pypi_name Keras

Name:           python-%{pypi_name}
Version:        2.4.3
Release:        1%{?dist}
Summary:        Deep Learning for humans

License:        MIT
URL:            https://github.com/keras-team/keras
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(h5py)
BuildRequires:  python3dist(markdown)
BuildRequires:  python3dist(numpy) >= 1.9.1
BuildRequires:  python3dist(pandas)
BuildRequires:  python3dist(pydot) >= 1.2.4
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(pytest-pep8)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(pyyaml)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(scipy) >= 0.14
BuildRequires:  python3dist(setuptools)

%description
Keras is a high-level neural networks API for Python.Read the documentation at:
is compatible with Python 3.6+ and is distributed under the MIT license.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(flaky)
Requires:       python3dist(h5py)
Requires:       python3dist(markdown)
Requires:       python3dist(numpy) >= 1.9.1
Requires:       python3dist(pandas)
Requires:       python3dist(pydot) >= 1.2.4
Requires:       python3dist(pytest)
Requires:       python3dist(pytest-cov)
Requires:       python3dist(pytest-pep8)
Requires:       python3dist(pytest-xdist)
Requires:       python3dist(pyyaml)
Requires:       python3dist(requests)
Requires:       python3dist(scipy) >= 0.14
%description -n python3-%{pypi_name}
Keras is a high-level neural networks API for Python.Read the documentation at:
is compatible with Python 3.6+ and is distributed under the MIT license.


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
%license LICENSE
%doc docs/README.md README.md examples/README.md
%{python3_sitelib}/docs
%{python3_sitelib}/keras
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Thu Jul 01 2021 Michael Dunlap <michael.dunlap@yale.edu>
 - 2.4.3-1
