%bcond_with x

Name:           libpciaccess
Version:        0.13.2
Release:        0
License:        MIT
Summary:        PCI access library
Url:            http://cgit.freedesktop.org/xorg/lib/libpciaccess/
Group:          Base/Device Management
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libpciaccess.manifest

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
libpciaccess is a library for portable PCI access routines across multiple
operating systems.

%package devel
Summary:        PCI access library development package
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
libpciaccess is a library for portable PCI access routines across multiple
operating systems.

This package contains development files needed to develop with the
libpciaccess library.

%global TZ_SYS_RO_SHARE  %{?TZ_SYS_RO_SHARE:%TZ_SYS_RO_SHARE}%{!?TZ_SYS_RO_SHARE:/usr/share}

%prep
%setup -q
cp %{SOURCE1001} .
%build
NOCONFIGURE=1
%autogen
%configure --disable-static \
           --with-pciids-path=%{_datadir}/misc --with-zlib
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{TZ_SYS_RO_SHARE}/license
cp -af COPYING %{buildroot}/%{TZ_SYS_RO_SHARE}/license/%{name}
%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{TZ_SYS_RO_SHARE}/license/%{name}
%{_libdir}/libpciaccess.so.*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.so
%{_libdir}/pkgconfig/pciaccess.pc
%{TZ_SYS_RO_SHARE}/license/%{name}

