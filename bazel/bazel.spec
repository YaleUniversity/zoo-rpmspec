%global __strip /bin/true

Name:    bazel
Version: 0.25.2
Release: 0%{?dist}
Summary: Build and test software of any size, quickly and reliably.

License: Apache-2.0
URL:     https://bazel.build/
Source0: https://github.com/bazelbuild/%{name}/releases/download/%{version}/%{name}-%{version}-installer-linux-%{_arch}.sh

%description
{Fast, Correct} - Choose two
Build and test software of any size, quickly and reliably.
Speed up your builds and tests: Bazel only rebuilds what is necessary. With advanced local and distributed caching, optimized dependency
analysis and parallel execution, you get fast and incremental builds.
One tool, multiple languages: Build and test Java, C++, Android, iOS, Go, and a wide variety of other language platforms. Bazel runs on
Windows, macOS, and Linux.
Scalable: Bazel helps you scale your organization, codebase, and continuous integration solution. It handles codebases of any size, in
multiple repositories or a huge monorepo.
Extensible to your needs: Easily add support for new languages and platforms with Bazel's familiar extension language. Share and
re-use language rules written by the growing Bazel community.

%prep
mkdir -p %{_builddir}/%{name}
chmod +x %{_sourcedir}/%{name}-%{version}-installer-linux-%{_arch}.sh 
cp %{_sourcedir}/%{name}-%{version}-installer-linux-%{_arch}.sh %{_builddir}/%{name}/

%build
%{_builddir}/%{name}/%{name}-%{version}-installer-linux-%{_arch}.sh --prefix=%{_builddir}/%{name}

%install
mkdir -p %{buildroot}%{_bindir}
mv %{_builddir}/%{name}/lib/%{name}/bin/%{name} %{buildroot}%{_bindir}/
mv %{_builddir}/%{name}/lib/%{name}/bin/%{name}-real %{buildroot}%{_bindir}/

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-real

%changelog
* Wed Aug 07 2019 Grace Petegorsky <grace.petegorsky@yale.edu> -
* 0.25.2-1
- Initial package.
