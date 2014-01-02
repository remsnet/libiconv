#
# spec file for package libiconv
#
# Remsnet  Spec file for package ntdb  (Version 1.00)
#
# Copyright (c) 1995-2008 Remsnet Netzwerk Service OhG , D-73630 Remshalden
# Copyright (c) 2008-2014 Remsnet Consullting & Internet Services LTD , D-40476 Duesseldorf

# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via https://github.com/remsnet/samba-dc-opensuse-RPi
#

Name:         libiconv
License:      LGPL v2.0 or later
Group:        System
Provides:     iconv libiconv
Version:      1.14
Release:      oss13.1
Summary:      GNU libiconv
URL:          http://www.gnu.org/software/libiconv/
Source0:      ftp://ftp.gnu.org/pub/gnu/libiconv/%{name}-%{version}.tar.gz
Patch:       libiconv-1.14-add-relocatable-module.patch
Patch1:      libiconv-1.14-autoconf.patch
BuildRoot:    %{_tmppath}/%{name}-%{version}-build

BuildRequires: automake autoconf gcc make
BuildRequires: libsigc++2-devel

%description
character set conversion library

%prep
%setup
%setup -T -D -a 1
%patch -p1
%patch1 -p1
#quilt push -a

%build
export CFLAGS="$RPM_OPT_FLAGS -DNO_VERSION_DATE -fno-strict-aliasing" LDFLAGS="-L%{_libdir}"
#export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -DLDAP_DEPRECATED" LDFLAGS="-L%{_libdir}"
#export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -fpie" LDFLAGS="-L%{_libdir} -pie"
CONFIGURE_OPTIONS="\
        --prefix=%{_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sysconfdir=%{_sysconfdir} \
        --localstatedir=%{_var} \
        --includedir=%{_includedir}/libiconv \
        --libdir=%{_libdir} \
        --mandir=%{_mandir} \
        --infodir=%{_infodir} \
        --enable-relocatable  \
        --exec-prefix=%{_prefix}  \
        --with-libintl-prefix=/usr  \
        --with-gnu-ld --enable-static \
        --enable-dependency-tracking \
        --enable-extra-encodings \
"

make %{?jobs:-j%jobs}

%install
%makeinstall
# avoid rpath error
#rm -f $RPM_BUILD_ROOT/usr/bin/iconv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/lib/preloadable_libiconv.so

%changelog
* Sat Dec 28 2013 - Horst venzke - info@remsnet.de - 1.0 _b
- rewriten oss13.1 spec file
- added patch libiconv-1.14-add-relocatable-module.patch
- added patch libiconv-1.14-autoconf.patch
