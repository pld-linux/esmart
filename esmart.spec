Summary:	Evas "smart objects"
Name:		esmart
Version:	0.9.0
%define _snap	20050106
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Libraries
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	5a999db4998c4cf35ca43fd8e36134b1
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje-devel
BuildRequires:	epeg-devel
BuildRequires:	epsilon-devel
BuildRequires:	libltdl-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Esmart contains "smart" pre-built evas objects. It currently includes
a thumbnail generator and a horizontal/vertical container.

%package devel
Summary:	Eves "smart objects" headers and development libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	edje-devel
Requires:	epeg-devel
Requires:	epsilon-devel

%description devel
Evas "smart objects" development headers and libraries.

%package static
Summary:	Static libraries
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING* README
%attr(755,root,root) %{_libdir}/libesmart_*.so.*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/layout
%attr(755,root,root) %{_libdir}/%{name}/layout/*.so
%attr(755,root,root) %{_bindir}/esmart_file_dialog_test
%attr(755,root,root) %{_bindir}/esmart_test
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libesmart_*.so
%{_libdir}/libesmart_*.la
%{_libdir}/%{name}/layout/*.la
%{_includedir}/Esmart/Esmart_*
%attr(755,root,root) %{_bindir}/esmart-config
%{_pkgconfigdir}/esmart.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libesmart_*.a
%{_libdir}/%{name}/layout/*.a
