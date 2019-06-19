# Created by pyp2rpm-3.3.2
%global pypi_name h5py

Name:           python-%{pypi_name}
Version:        2.8.0
Release:        1%{?dist}
Summary:        Read and write HDF5 files from Python

License:        BSD
URL:            http://www.h5py.org
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 0.23
BuildRequires:  python3dist(numpy) >= 1.7
BuildRequires:  python3dist(numpy) >= 1.7
BuildRequires:  python3dist(numpy) >= 1.7
BuildRequires:  python3dist(pkgconfig)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)

%description
The h5py package provides both a high- and low-level interface to the HDF5
library from Python. The low-level interface is intended to be a complete
wrapping of the HDF5 API, while the high-level component supports access to
HDF5 files, datasets and groups using established Python and NumPy concepts.A
strong emphasis on automatic conversion between Python (Numpy) datatypes and
data structures...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(numpy) >= 1.7
Requires:       python3dist(six)
%description -n python3-%{pypi_name}
The h5py package provides both a high- and low-level interface to the HDF5
library from Python. The low-level interface is intended to be a complete
wrapping of the HDF5 API, while the high-level component supports access to
HDF5 files, datasets and groups using established Python and NumPy concepts.A
strong emphasis on automatic conversion between Python (Numpy) datatypes and
data structures...

%package -n python-%{pypi_name}-doc
Summary:        h5py documentation
%description -n python-%{pypi_name}-doc
Documentation for h5py

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license licenses/license.txt lzf/LICENSE.txt docs/licenses.rst
%doc windows/README.txt lzf/README.txt README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license licenses/license.txt lzf/LICENSE.txt docs/licenses.rst

%changelog
* Wed Aug 15 2018 Grace Petegorsky <grace.petegorsky@yale.edu> - 2.8.0-1
- Initial package.