# Created by pyp2rpm-3.3.6
%global pypi_name hmmlearn

Name:           python-%{pypi_name}
Version:        0.2.5
Release:        1%{?dist}
Summary:        Hidden Markov Models in Python with scikit-learn like API

License:        new BSD
URL:            https://github.com/hmmlearn/hmmlearn
Source0:        https://github.com/%{pypi_name}/%{pypi_name}/archive/ref/tags/%{version}.tar.gz


https://github.com/hmmlearn/hmmlearn/archive/refs/tags/0.2.5.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(matplotlib)
BuildRequires:  python3dist(numpy) >= 1.10
BuildRequires:  python3dist(numpy) >= 1.10
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(scikit-learn) >= 0.16
BuildRequires:  python3dist(scipy) >= 0.19
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-scm) >= 3.3
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-gallery)
BuildRequires:  python3dist(sphinx)

%description
| |GitHub| |PyPI| | |Read the Docs| |Azure Pipelines| |CodeCov|.. |GitHub| ..
|PyPI| .. |Read the Docs| .. |Azure Pipelines| :target:

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(matplotlib)
Requires:       python3dist(numpy) >= 1.10
Requires:       python3dist(pillow)
Requires:       python3dist(pytest)
Requires:       python3dist(scikit-learn) >= 0.16
Requires:       python3dist(scipy) >= 0.19
Requires:       python3dist(setuptools)
Requires:       python3dist(sphinx)
Requires:       python3dist(sphinx-gallery)
%description -n python3-%{pypi_name}
| |GitHub| |PyPI| | |Read the Docs| |Azure Pipelines| |CodeCov|.. |GitHub| ..
|PyPI| .. |Read the Docs| .. |Azure Pipelines| :target:

%package -n python-%{pypi_name}-doc
Summary:        hmmlearn documentation
%description -n python-%{pypi_name}-doc
Documentation for hmmlearn

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst examples/README.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Thu Jul 01 2021 Michael Dunlap <michael.dunlap@yale.edu> -
- build new release *  - 0.2.5
