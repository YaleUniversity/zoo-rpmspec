%define debug_package %{nil}

Name:		  zotero
Version:	5.0.89
Release:	1%{?dist}
Summary:	Collect, organize, cite, and share research sources

License:	AGPLv3
URL:		  https://github.com/zotero/zotero
Source0:  https://download.zotero.org/client/release/%{version}/Zotero-%{version}_linux-x86_64.tar.bz2 
Source1:  zotero.desktop

Requires: firefox

%description
Zotero [zoh-TAIR-oh] is a free, easy-to-use tool to help you collect, organize, cite, and share your research sources.

%prep
%autosetup -n Zotero_linux-x86_64

%build

%install
mkdir -p %{buildroot}/{%{_bindir},%{_libdir}/%{name}}
cp -r %{_builddir}/Zotero_linux-x86_64/* %{buildroot}/%{_libdir}/%{name}/
ln -sf %{_libdir}/%{name}/zotero %{buildroot}/%{_bindir}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/%{name}.desktop
install -Dm644 %{buildroot}/%{_libdir}/%{name}/chrome/icons/default/default16.png %{buildroot}/%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
install -Dm644 %{buildroot}/%{_libdir}/%{name}/chrome/icons/default/default32.png %{buildroot}/%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
install -Dm644 %{buildroot}/%{_libdir}/%{name}/chrome/icons/default/default48.png %{buildroot}/%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
install -Dm644 %{buildroot}/%{_libdir}/%{name}/chrome/icons/default/default256.png %{buildroot}/%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%files
%doc
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/zotero.png
%{_libdir}/%{name}


%changelog
* Fri Aug 14 2020 Bugzy Little <bugzylittle@gmail.com> - 5.0.89-1
- Upgrade to 5.0.89
* Thu Jun 25 2020 Bugzy Little <bugzylittle@gmail.com> - 5.0.88-1
- Upgrade to 5.0.88
* Mon Aug 05 2019 Grace Petegorsky <grace.petegorsky@yale.edu> - 5.0.73-1
- Upgrade to 5.0.73
* Thu Aug 17 2017 David Goerger <david.goerger@yale.edu> - 5.0.12-1
- initial package
