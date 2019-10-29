# Created by pyp2rpm-3.3.2
%global pypi_name ipywidgets

Name:           python-%{pypi_name}
Version:        7.5.1
Release:        1%{?dist}
Summary:        IPython HTML widgets for Jupyter

License:        BSD
URL:            http://ipython.org
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
 Interactive HTML Widgets Interactive HTML widgets for Jupyter notebooks and
the IPython kernel.Usage .. code-block:: python from ipywidgets import
IntSlider IntSlider()

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 Interactive HTML Widgets Interactive HTML widgets for Jupyter notebooks and
the IPython kernel.Usage .. code-block:: python from ipywidgets import
IntSlider IntSlider()

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 29 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 7.5.1-1
- Initial package.
