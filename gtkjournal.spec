Summary:	Journal/Diary
Summary(pl):	Dziennik/Pamiêtnik
Name:		gtkjournal
Version:	0.3.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://linuxhelp.homeunix.com/gtkjournal/files/%{name}-%{version}.tar.gz
# Source0-md5:	93a3f955c2e437e077ecf5d055b66f49
URL:		http://linuxhelp.homeunix.com/gtkjournal/
BuildRequires:	autoconf
BuildRequires:	automake
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
%setup -q 

%build
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
		DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
