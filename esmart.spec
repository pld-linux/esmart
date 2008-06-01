#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
%define		ecore_ver	0.9.9.043
%define		edje_ver	0.9.9.043
%define		epsilon_ver	0.3.0.012
%define		evas_ver	0.9.9.043

Summary:	Evas "smart objects"
Summary(pl.UTF-8):	"Inteligentne obiekty" Evas
Name:		esmart
Version:	0.9.0.042
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://download.enlightenment.org/snapshots/2008-01-25/%{name}-%{version}.tar.bz2
# Source0-md5:	62c1d73d2610da148b260efc36b1d03a
Patch0:		%{name}-layout_in_libdir.patch
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
# ecore-evas ecore-x
BuildRequires:	ecore-devel >= %{ecore_ver}
BuildRequires:	edje-devel >= %{edje_ver}
BuildRequires:	epsilon-devel >= %{epsilon_ver}
BuildRequires:	evas-devel >= %{evas_ver}
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
Requires:	ecore-devel >= %{ecore_ver}
Requires:	edje-devel >= %{edje_ver}
Requires:	epsilon-devel >= %{epsilon_ver}
Requires:	evas-devel >= %{evas_ver}
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
%attr(755,root,root) %{_bindir}/esmart_text_entry_test
%attr(755,root,root) %{_bindir}/esmart_test
%{_datadir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libesmart_*.so.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/layout
%attr(755,root,root) %{_libdir}/%{name}/layout/*.so

%files devel
%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/esmart-config
%attr(755,root,root) %{_libdir}/libesmart_*.so
%{_libdir}/libesmart_*.la
%dir %{_includedir}/Esmart
%{_includedir}/Esmart/Esmart_*.h
%{_pkgconfigdir}/esmart_*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libesmart_*.a
%endif
