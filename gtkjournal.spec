Summary:	Journal/Diary
Summary(pl):	Dziennik/Pamiêtnik
Name:		gtkjournal
Version:	0.3.4a
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://linuxhelp.homeunix.com/gtkjournal/files/%{name}-%{version}.tar.bz2
# Source0-md5:	a59e68e8a5f09afd58dbc840c22ec814
URL:		http://linuxhelp.homeunix.com/gtkjournal/
BuildRequires:	gtkmm-devel
BuildRequires:	libsigc++12-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRequires:	sqlite-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gtk+ Journal is a Journal/Diary application written using the C++
bindings for Gtk+2 (gtkmm). It uses SQlite to store your entries, and
the OpenSSL implementations of the BlowFish and SHA-1 algorithms to
keep your data safe.

%description -l pl
Gtk+ Journal jest Dziennikiem/Pamiêtnikiem, napisanym z u¿yciem gtkmm.
U¿ywa SQlite do przechowywania twoich wpisów i implementacji OpenSSL
algorytmów BlowFish oraz SHA-1 do zabezpieczenia twoich danych.

%prep
%setup -q -n %{name}

%build
%{__make} \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir}}

install gtkjournal $RPM_BUILD_ROOT%{_bindir}
install icon.xpm $RPM_BUILD_ROOT%{_pixmapsdir}/gtkjournal.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
