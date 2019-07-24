# Created by pyp2rpm-3.3.2
%global pypi_name ipythonblocks

Name:           python-%{pypi_name}
Version:        1.9.0
Release:        1%{?dist}
Summary:        Practice Python with colored grids in the IPython Notebook

License:        None
URL:            https://github.com/jiffyclub/ipythonblocks/
Source0:        https://files.pythonhosted.org/packages/source/i/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
ipythonblocks ipythonblocks is a teaching tool for use with the IPython_
Notebook. It provides a BlockGrid object whose representation is an HTML table.
Individual table cells are represented by Block objects that have .red,

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(ipython) >= 4.0
Requires:       python3dist(notebook) >= 4.0
Requires:       python3dist(requests) >= 1.0
%description -n python3-%{pypi_name}
ipythonblocks ipythonblocks is a teaching tool for use with the IPython_
Notebook. It provides a BlockGrid object whose representation is an HTML table.
Individual table cells are represented by Block objects that have .red,


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Jul 24 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 1.9.0-1
- Initial package.