# Created by pyp2rpm-3.3.2
%global pypi_name wordsegment

Name:           python-%{pypi_name}
Version:        1.3.1
Release:        1%{?dist}
Summary:        English word segmentation

License:        Apache 2.0
URL:            http://www.grantjenks.com/docs/wordsegment/
Source0:        https://files.pythonhosted.org/packages/source/w/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(tox)

%description
Python Word Segmentation WordSegment_ is an Apache2 licensed module for English
word segmentation, written in pure-Python, and based on a trillion-word
corpus.Based on code from the chapter "Natural Language Corpus Data_" by Peter
Norvig from the book "Beautiful Data_" (Segaran and Hammerbacher, 2009).Data
files are derived from the Google Web Trillion Word Corpus_, as described by
Thorsten...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Python Word Segmentation WordSegment_ is an Apache2 licensed module for English
word segmentation, written in pure-Python, and based on a trillion-word
corpus.Based on code from the chapter "Natural Language Corpus Data_" by Peter
Norvig from the book "Beautiful Data_" (Segaran and Hammerbacher, 2009).Data
files are derived from the Google Web Trillion Word Corpus_, as described by
Thorsten...


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
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Thu Jul 25 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 1.3.1-1
- Initial package.