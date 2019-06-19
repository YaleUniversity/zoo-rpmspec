%global debug_package %{nil}
%global packname typer
Name:		  erlang-%{packname}
Version:  0.9.13
Release:	1%{?dist}
Summary:	TypEr, a Type annotator for ERlang programs.

License:  Apache v2	
URL:		  http://erlang.org/doc/man/typer.html
Source0:	https://github.com/erlang/typer/archive/%{version}.tar.gz

Requires:	erlang
BuildRequires: rebar3

%description
TypEr shows type information for Erlang modules to the user. Additionally, it can annotate the code of files with such type information.

%prep
%autosetup -n %{packname}-%{version}

%build

%install
cd %{_builddir}/%{packname}-%{version}
rebar3 compile
mkdir -p %{buildroot}%{_bindir}
mv %{_builddir}/%{packname}-%{version}/%{packname} %{buildroot}%{_bindir}/%{packname}

%files
%{_bindir}/%{packname}

%changelog
* Wed Jul 25 2018 Grace Petegorsky - 0.9.13-1
- Initial package.
