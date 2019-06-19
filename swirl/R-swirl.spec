%global packname swirl
%global packrel 1
%global debug_package %{nil}

%define coursesdir Courses

Name:             R-%{packname}
Version:          2.4.3
Release:          2%{?dist}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
Patch0:           swirl_userdata.patch
License:          GPLv2+
URL:              https://cran.r-project.org/web/packages/swirl/index.html
Group:            Applications/Engineering
Summary:          Interactive learning environment for R
BuildRequires:    R-devel, unzip
BuildRequires:    R-RCurl, R-digest, R-testthat, R-stringr, R-httr, R-yaml, R-R6
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:         R-RCurl, R-digest, R-testthat, R-stringr, R-httr, R-yaml, R-R6

%description
R interface to swirl. swirl is a software package for the R programming
language that turns the R console into an interactive learning
environment. Users receive immediate feedback as they are guided through
self-paced lessons in data science and R programming.

%prep
%setup -q -c -n %{packname}
curl -Lo swirl_courses.zip https://github.com/swirldev/swirl_courses/archive/master.zip
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}/R/library
%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf $RPM_BUILD_ROOT%{_libdir}/R/library/R.css

# copy in courses
unzip -d %{buildroot}/tmp %{_builddir}/%{packname}/swirl_courses.zip
rm -rf %{buildroot}%{_libdir}/R/library/%{packname}/%{coursesdir}
mv %{buildroot}/tmp/swirl_courses-master %{buildroot}%{_libdir}/R/library/%{packname}/%{coursesdir}
rm %{buildroot}%{_libdir}/R/library/%{packname}/%{coursesdir}/.gitignore

%check
# needed to pass the test-encoding
export LC_ALL="en_US.UTF-8"
%{_bindir}/R CMD check %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/html
%{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/LICENSE
%{_libdir}/R/library/%{packname}/NEWS.md
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/test/
%{_libdir}/R/library/%{packname}/%{coursesdir}

%changelog
* Mon Apr 02 2018 David Goerger - 2.4.3-2
- update bundled courses to commit ac5c6142b7a51698c16fe8587222284779d66122

* Sat Jun 10 2017 David Goerger - 2.4.3-1
- update to 2.4.3

* Wed Sep 07 2016 David Goerger - 2.4.2-2
- update to 2.4.2
- note that the test suite only passes with LC_ALL="en_US.UTF-8"

* Tue Jul 26 2016 David Goerger - 2.2.21-1
- initial package creation
