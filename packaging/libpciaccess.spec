Name:           libpciaccess
Version:        0.13.1
Release:        1
License:        MIT
Summary:        PCI access library
Url:            http://gitweb.freedesktop.org/?p=xorg/lib/libpciaccess.git
Group:          System Environment/Libraries
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(zlib)

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
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libpciaccess.so.0
%{_libdir}/libpciaccess.so.0.11.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/pciaccess.h
%{_libdir}/libpciaccess.so
%{_libdir}/pkgconfig/pciaccess.pc
