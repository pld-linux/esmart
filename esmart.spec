#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Evas "smart objects"
Summary(pl):	"Inteligentne obiekty" Evas
Name:		esmart
Version:	0.9.0.004
%define	_snap	20051025
Release:	1.%{_snap}.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
Source0:	http://sparky.homelinux.org/snaps/enli/e17/libs/%{name}-%{_snap}.tar.bz2
# Source0-md5:	a9839d5d33c162bb81ad3480d1351f4a
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje-devel
BuildRequires:	epeg-devel
BuildRequires:	epsilon-devel
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Esmart contains "smart" pre-built evas objects. It currently includes
a thumbnail generator and a horizontal/vertical container.

%description -l pl
Esmart zawiera "inteligentne" wstêpnie zbudowane obiekty evas.
Aktualnie zawiera generator miniaturek i kontener poziomy/pionowy.

%package libs
Summary:	Esmart libraries
Summary(pl):	Biblioteka Esmart
Group:		X11/Libraries

%description libs
Esmart libraries.

%description libs -l pl
Biblioteka Esmart.

%package devel
Summary:	Evas "smart objects" header files
Summary(pl):	Pliki nag³ówkowe "inteligentnych obiektów" Evas
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	edje-devel
Requires:	epeg-devel
Requires:	epsilon-devel

%description devel
Evas "smart objects" development headers.

%description devel -l pl
Pliki nag³ówkowe "inteligentnych obiektów" Evas.

%package static
Summary:	Static Esmart libraries
Summary(pl):	Statyczne biblioteki Esmart
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Esmart libraries.

%description static -l pl
Statyczne biblioteki Esmart.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post libs	-p /sbin/ldconfig
%postun libs	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING* README
%attr(755,root,root) %{_bindir}/esmart_file_dialog_test
%attr(755,root,root) %{_bindir}/esmart_test
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libesmart_*.so.*.*.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/layout
%attr(755,root,root) %{_libdir}/%{name}/layout/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/esmart-config
%attr(755,root,root) %{_libdir}/libesmart_*.so
%{_libdir}/libesmart_*.la
%{_libdir}/%{name}/layout/*.la
%dir %{_includedir}/Esmart
%{_includedir}/Esmart/Esmart_*
%{_pkgconfigdir}/esmart.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libesmart_*.a
%{_libdir}/%{name}/layout/*.a
%endif
