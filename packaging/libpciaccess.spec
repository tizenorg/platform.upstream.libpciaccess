%bcond_with x

Name:           libpciaccess
Version:        0.13.1
Release:        1
License:        MIT
Summary:        PCI access library
Url:            http://gitweb.freedesktop.org/?p=xorg/lib/libpciaccess.git
Group:          Base/Device Management
Source:         %{name}-%{version}.tar.bz2
Source1001: 	libpciaccess.manifest

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%if %{with x}
BuildRequires:  pkgconfig(xorg-macros)
%endif

%description
libpciaccess is a library for portable PCI access routines across multiple
operating systems.

%package devel
Summary:        PCI access library development package
Group:          Development/Libraries
Requires:       %{name} = %{version}
Requires:       pkgconfig

%description devel
Development package for libpciaccess.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --disable-static \
           --with-pciids-path=%{_datadir}/misc --with-zlib
make %{?_smp_mflags}

%install
%make_install

%remove_docs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libpciaccess.so.0
%{_libdir}/libpciaccess.so.0.11.*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.so
%{_libdir}/pkgconfig/pciaccess.pc
