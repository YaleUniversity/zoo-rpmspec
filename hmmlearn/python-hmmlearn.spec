# Created by pyp2rpm-3.2.3
%global pypi_name hmmlearn

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        1%{?dist}
Summary:        Hidden Markov Models in Python with scikit-learn like API

License:        new BSD
URL:            https://github.com/hmmlearn/hmmlearn
Source0:        https://files.pythonhosted.org/packages/source/h/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3-scikit-learn >= 0.16
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools

%description
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
%autosetup -n %{pypi_name}-%{version}
# Correct 'sklearn' to 'scikit-learn' (package name on Fedora)
# %patch0 -p0 -R

%build
%py3_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py3_install



%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Fri Jul 26 2018 Grace Petegorsky <grace.petegorsky@yale.edu> - 0.2.2-1
- Update to 0.2.2
* Mon Apr 16 2018 Grace Petegorsky <grace.petegorsky@yale.edu> - 0.2.0-1
- Initial package.
