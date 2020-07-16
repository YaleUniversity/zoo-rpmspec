# Created by pyp2rpm-3.3.2
%global pypi_name vaderSentiment

Name:           python-%{pypi_name}
Version:        3.3.2
Release:        1%{?dist}
Summary:        VADER Sentiment Analysis. VADER (Valence Aware Dictionary and sEntiment Reasoner) is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains

License:        MIT License: http://opensource.org/licenses/MIT
URL:            https://github.com/cjhutto/vaderSentiment
Source0:        https://files.pythonhosted.org/packages/source/v/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 VADER-Sentiment-Analysis VADER (Valence Aware Dictionary and sEntiment
Reasoner) is a lexicon and rule-based sentiment analysis tool that is
*specifically attuned to sentiments expressed in social media*. It is fully
open-sourced under the [MIT License] < (we sincerely appreciate all
attributions and readily accept most contributions, but please don't hold us
liable).* Features and Updates_ *...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
 VADER-Sentiment-Analysis VADER (Valence Aware Dictionary and sEntiment
Reasoner) is a lexicon and rule-based sentiment analysis tool that is
*specifically attuned to sentiments expressed in social media*. It is fully
open-sourced under the [MIT License] < (we sincerely appreciate all
attributions and readily accept most contributions, but please don't hold us
liable).* Features and Updates_ *...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Wed Jul 15 2020 Adil Mahmood <adil.mahmood@yale.edu> - 3.3.2
* Tue Feb 12 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 3.2.1-1
- Initial package.
