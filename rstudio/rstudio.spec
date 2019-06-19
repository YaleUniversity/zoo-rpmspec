%global version_major 1
%global version_minor 1
%global version_patch 453

%global co_date 20160730
%global gin_ver 1.5
%global gwt_ver 2.7.0
%global junit_ver 4.9b3
%global mathjax_ver 26
%global selenium_ver 2.37.0

Name:           rstudio
Version:        %{version_major}.%{version_minor}.%{version_patch}
Release:        1%{?dist}
Summary:        Integrated development environment for the R programming language

License:        AGPLv3
URL:            https://www.rstudio.com/products/RStudio/
Source0:        https://github.com/rstudio/rstudio/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://s3.amazonaws.com/rstudio-dictionaries/core-dictionaries.zip

# Additional build stuff
Source2:        https://s3.amazonaws.com/rstudio-buildtools/gin-%{gin_ver}.zip
Source3:        https://s3.amazonaws.com/rstudio-buildtools/gwt-%{gwt_ver}.zip
Source5:        https://s3.amazonaws.com/rstudio-buildtools/mathjax-%{mathjax_ver}.zip
Source6:        https://s3.amazonaws.com/rstudio-buildtools/selenium-java-%{selenium_ver}.zip
Source7:        https://s3.amazonaws.com/rstudio-buildtools/selenium-server-standalone-%{selenium_ver}.jar

# Additional deps
Source8:        https://github.com/rstudio/shinyapps/archive/master.zip#/shinyapps-%{co_date}.zip
Source9:        https://github.com/rstudio/rsconnect/archive/master.zip#/rsconnect-%{co_date}.zip

Patch0:         %{name}-%{version}-dependencies.patch
Patch3:         %{name}-%{version}-sysmacros.patch

BuildRequires:  ant
BuildRequires:  boost-devel
BuildRequires:  clang-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
BuildRequires:  java-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  pandoc
BuildRequires:  qt5-devel
BuildRequires:  libuuid-devel
BuildRequires:  R-devel
BuildRequires:  xml-commons-apis
BuildRequires:  junit

%description
RStudio is an integrated development environment (IDE) for the R programming
language. 

Some of its features include:
  * Customizable workbench with all of the tools required to work with R in one
    place (console, source, plots, workspace, help, history, etc.).
  * Syntax highlighting editor with code completion.
  * Execute code directly from the source editor (line, selection, or file).
  * Full support for authoring Sweave and TeX documents.


%package common
Summary:        Integrated development environment for the R programming language
Requires:       hicolor-icon-theme
Requires:       java
Requires:       pandoc
Requires:       R
Requires:       xml-commons-apis

# We cannot coexist with upstream RPM files
Conflicts:      rstudio

%description common
RStudio is an integrated development environment (IDE) for the R programming
language.

Some of its features include:
  * Customizable workbench with all of the tools required to work with R in one
    place (console, source, plots, workspace, help, history, etc.).
  * Syntax highlighting editor with code completion.
  * Execute code directly from the source editor (line, selection, or file).
  * Full support for authoring Sweave and TeX documents.

This package contains files common to both rstudio-desktop and rstudio-server.

%package desktop
Summary:        Integrated development environment for the R programming language
Requires:       rstudio-common
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

# We cannot coexist with upstream RPM files
Conflicts:      rstudio

%description desktop
RStudio is an integrated development environment (IDE) for the R programming
language.

Some of its features include:
  * Customizable workbench with all of the tools required to work with R in one
    place (console, source, plots, workspace, help, history, etc.).
  * Syntax highlighting editor with code completion.
  * Execute code directly from the source editor (line, selection, or file).
  * Full support for authoring Sweave and TeX documents.

This package provides the desktop client.

%package server
Summary:        Integrated development environment for the R programming language
Requires:       rstudio-common

# We cannot coexist with upstream RPM files
Conflicts:      rstudio

%description server
RStudio is an integrated development environment (IDE) for the R programming
language.

Some of its features include:
  * Customizable workbench with all of the tools required to work with R in one
    place (console, source, plots, workspace, help, history, etc.).
  * Syntax highlighting editor with code completion.
  * Execute code directly from the source editor (line, selection, or file).
  * Full support for authoring Sweave and TeX documents.

This package provides the server edition.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch3 -p1

# copy in additional resources
cd dependencies/common

mkdir dictionaries
cd dictionaries
unzip %{SOURCE1}
cd ..

mkdir mathjax-%{mathjax_ver}
cd mathjax-%{mathjax_ver}
unzip %{SOURCE5}
cd .. 

mkdir rsconnect
cd rsconnect
unzip %{SOURCE9}                
cd ..

mkdir shinyapps
cd shinyapps
unzip %{SOURCE8}                
cd ../../../

cd src/gwt
mkdir -p lib/gin/%{gin_ver}
unzip -qd lib/gin/%{gin_ver} %{SOURCE2}
mkdir -p lib/gwt
unzip -qd lib %{SOURCE3}
mv lib/gwt-%{gwt_ver} lib/gwt/%{gwt_ver}
ln -s %{_datadir}/java/gwt lib/gwt/%{gwt_ver}
mkdir lib/selenium
unzip -qd lib %{SOURCE6}
mv lib/selenium-%{selenium_ver} lib/selenium/%{selenium_ver}
cp %{SOURCE7} lib/selenium/%{selenium_ver}/


%build
# rstudio-desktop
mkdir build_desktop
pushd build_desktop
export RSTUDIO_VERSION_MAJOR=%{version_major}
export RSTUDIO_VERSION_MINOR=%{version_minor}
export RSTUDIO_VERSION_PATCH=%{version_patch}
%cmake -DRSTUDIO_TARGET=Desktop \
  -DCMAKE_BUILD_TYPE=Release \
  -DQT_QMAKE_EXECUTABLE=%{_qmake_qt5} \
  -DCMAKE_INSTALL_PREFIX=%{_libdir}/%{name} .. 
%make_build
popd

# rstudio-server
mkdir build_server
pushd build_server
%cmake -DRSTUDIO_TARGET=Server \
  -DCMAKE_BUILD_TYPE=Release \
  -DQT_QMAKE_EXECUTABLE=%{_qmake_qt5} \
  -DCMAKE_INSTALL_PREFIX=%{_libdir}/%{name} .. 
%make_build
popd

%install
# rstudio-desktop
pushd build_desktop
%make_install
popd
# rstudio-server
pushd build_server
%make_install
popd
# clean extra init files
mkdir -p %{buildroot}/usr/lib/systemd/system
cp %{buildroot}/%{_libdir}/%{name}/extras/systemd/rstudio-server.service %{buildroot}/usr/lib/systemd/system/rstudio-server.service
rm -rf %{buildroot}/%{_libdir}/%{name}/extras

%post desktop
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/bin/touch --no-create %{_datadir}/mime/packages &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :
if [ $1 -eq 1 -o ! -e /usr/bin/rstudio ]; then
    ln -s %{_libdir}/%{name}/bin/%{name} /usr/bin/
fi

%preun desktop
if [ $1 -eq 0 ]; then
    rm -f /usr/bin/rstudio
fi

%postun desktop
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
if [ $1 -eq 0 ] ; then
  /usr/bin/update-mime-database %{_datadir}/mime &> /dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :

%posttrans desktop
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :


%files common
%license COPYING
%doc NEWS.md NOTICE README.md INSTALL
%{_libdir}/%{name}/COPYING
%{_libdir}/%{name}/INSTALL
%{_libdir}/%{name}/NOTICE
%{_libdir}/%{name}/README.md
%{_libdir}/%{name}/www
%{_libdir}/%{name}/www-symbolmaps
%{_libdir}/%{name}/R
%{_libdir}/%{name}/SOURCE
%{_libdir}/%{name}/VERSION
%{_libdir}/%{name}/bin/diagnostics
%{_libdir}/%{name}/bin/postback
%{_libdir}/%{name}/bin/r-ldpath
%{_libdir}/%{name}/bin/rpostback
%{_libdir}/%{name}/bin/rsession
%{_libdir}/%{name}/bin/rstudio-backtrace.sh
%{_libdir}/%{name}/*.png
%{_libdir}/%{name}/resources

%files desktop
%{_libdir}/%{name}/bin/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png

%files server
%{_libdir}/%{name}/bin/rserver
%{_libdir}/%{name}/bin/rserver-pam
%{_libdir}/%{name}/bin/%{name}-server
/usr/lib/systemd/system/rstudio-server.service


%changelog
* Thu May 17 2018 David Goerger - 1.1.453-1
- update to 1.1.453

* Wed Mar 28 2018 David Goerger - 1.1.442-1
- update to 1.1.442

* Mon Nov 27 2017 David Goerger - 1.1.383-1
- update to 1.1.383

* Wed Jun 21 2017 David Goerger - 1.0.143-1
- update to 1.0.143

* Tue Nov 22 2016 David Goerger - 1.0.44-2
- include rstudio-server subpackage

* Tue Nov 22 2016 David Goerger - 1.0.44-1
- update to 1.0.44

* Sun Jul 31 2016 Christian Dersch <lupinix@mailbox.org> - 0.99.903-6
- small fixes

* Sun Jul 31 2016 Christian Dersch <lupinix@mailbox.org> - 0.99.903-2
- added proper conflicts

* Sat Jul 30 2016 Christian Dersch <lupinix@mailbox.org> - 0.99.903-1
- initial package
