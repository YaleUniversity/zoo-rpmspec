# Created by pyp2rpm-3.2.3
%global pypi_name hmmlearn

Name:           python-%{pypi_name}
Version:        0.2.0
Release:        2%{?dist}
Summary:        Hidden Markov Models in Python with scikit-learn like API

License:        new BSD
URL:            https://github.com/hmmlearn/hmmlearn
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch0:         %{pypi_name}.patch
 
BuildRequires:  python2-devel
BuildRequires:  python2-scikit-learn >= 0.16
BuildRequires:  python2-pytest
BuildRequires:  python2-setuptools
 
BuildRequires:  python3-devel
BuildRequires:  python3-scikit-learn >= 0.16
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%description
hmmlearn |travis| |appveyor| .. |travi .. |appveyo hmmlearn is a set of
algorithms for **unsupervised** learning and inference of Hidden Markov Models.
For supervised learning learning of HMMs and similar models see seqlearn < the
latest code To get the latest code using git, simply type::

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2-numpydoc
Requires:       python2-scikit-learn >= 0.16
Requires:       python2-scikit-learn >= 0.16
Requires:       python2-matplotlib
Requires:       python2-pillow
Requires:       python2-pytest
Requires:       python2-sphinx
Requires:       python2-sphinx-gallery
%description -n python2-%{pypi_name}
hmmlearn |travis| |appveyor| .. |travi .. |appveyo hmmlearn is a set of
algorithms for **unsupervised** learning and inference of Hidden Markov Models.
For supervised learning learning of HMMs and similar models see seqlearn < the
latest code To get the latest code using git, simply type::

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-numpydoc
Requires:       python3-scikit-learn >= 0.16
Requires:       python3-scikit-learn >= 0.16
Requires:       python3-matplotlib
Requires:       python3-pillow
Requires:       python3-pytest
Requires:       python3-sphinx
Requires:       python3-sphinx-gallery
%description -n python3-%{pypi_name}
hmmlearn |travis| |appveyor| .. |travi .. |appveyo hmmlearn is a set of
algorithms for **unsupervised** learning and inference of Hidden Markov Models.
For supervised learning learning of HMMs and similar models see seqlearn < the
latest code To get the latest code using git, simply type::


%prep
%autosetup -n %{pypi_name}-%{version} -p1 -p0
# Correct 'sklearn' to 'scikit-learn' (package name on Fedora)


%build
%py2_build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install

%py2_install


%files -n python2-%{pypi_name}
%license LICENSE
%doc README.rst
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Aug 14 2018 Grace Petegorsky <grace.petegorsky@yale.edu> - 0.2.0-1
- Update for Fedora 28; disable tests
* Mon Apr 16 2018 Grace Petegorsky <grace.petegorsky@yale.edu> - 0.2.0-1
- Initial package.
