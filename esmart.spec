#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Evas "smart objects"
Summary(pl.UTF-8):	"Inteligentne obiekty" Evas
Name:		esmart
Version:	0.9.0.008
Release:	2
License:	BSD
Group:		X11/Libraries
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	80d0c7ea0ad7252c36626e5cab59ee9b
Patch0:		%{name}-layout_in_libdir.patch
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
# ecore-evas ecore-x
BuildRequires:	ecore-devel >= 0.9.9.038
BuildRequires:	edje-devel >= 0.5.0.038
BuildRequires:	epsilon-devel >= 0.3.0.008
BuildRequires:	evas-devel >= 0.9.9.038
BuildRequires:	imlib2-devel >= 1.0.0
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	__cxx

%description
Esmart contains "smart" pre-built evas objects. It currently includes
a thumbnail generator and a horizontal/vertical container.

%description -l pl.UTF-8
Esmart zawiera "inteligentne" wstępnie zbudowane obiekty evas.
Aktualnie zawiera generator miniaturek i kontener poziomy/pionowy.

%package libs
Summary:	Esmart libraries
Summary(pl.UTF-8):	Biblioteka Esmart
Group:		X11/Libraries

%description libs
Esmart libraries.

%description libs -l pl.UTF-8
Biblioteka Esmart.

%package devel
Summary:	Evas "smart objects" header files
Summary(pl.UTF-8):	Pliki nagłówkowe "inteligentnych obiektów" Evas
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
# ecore-evas ecore-x
Requires:	ecore-devel >= 0.9.9.038
Requires:	edje-devel >= 0.5.0.038
Requires:	epsilon-devel >= 0.3.0.008
Requires:	evas-devel >= 0.9.9.038
Requires:	imlib2-devel >= 1.0.0
Requires:	libltdl-devel

%description devel
Evas "smart objects" development headers.

%description devel -l pl.UTF-8
Pliki nagłówkowe "inteligentnych obiektów" Evas.

%package static
Summary:	Static Esmart libraries
Summary(pl.UTF-8):	Statyczne biblioteki Esmart
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Esmart libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Esmart.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
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

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/layout/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING README
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
%dir %{_includedir}/Esmart
%{_includedir}/Esmart/Esmart_*
%{_pkgconfigdir}/esmart.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libesmart_*.a
%endif
