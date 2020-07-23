# Created by pyp2rpm-3.3.4
%global pypi_name pysmell

Name:           python-%{pypi_name}
Version:        0.7.3
Release:        1%{?dist}
Summary:        An autocompletion library for Python

License:        None
URL:            http://code.google.com/p/pysmell
Source0:        %{pypi_source %{pypi_name} %{version} zip}
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)

%description
PySmell is a python IDE completion helper. It tries to statically analyze
Python source code, without executing it, and generates information about a
project's structure that IDE tools can PySmell currently supports Vim, Emacs
and TextMate. It can be integrated with any editor that can run Python scripts
and has an auto-complete API.

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

Requires:       python2dist(setuptools)
%description -n python2-%{pypi_name}
PySmell is a python IDE completion helper. It tries to statically analyze
Python source code, without executing it, and generates information about a
project's structure that IDE tools can PySmell currently supports Vim, Emacs
and TextMate. It can be integrated with any editor that can run Python scripts
and has an auto-complete API.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build

%install
%py2_install


%files -n python2-%{pypi_name}
%doc README.markdown
%{_bindir}/pysmell
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py%{python2_version}.egg-info

%changelog
* Thu Jul 23 2020 Adil Mahmood - 0.7.3-1
