Name:		prime95
Version:	30.3b6
Release:	1%{?dist}
Summary:	A tool for performing benchmarking and stability testing by finding Mersenne primes

Group:		System/Benchmarking
License:	GIMPS Free Software License
URL:		https://www.mersenne.org/
Source0:	prime95-30.3b6.tar.gz
Source1:	curl-7.76.1.tar.gz
Patch0:		prime95-dynamic.patch

BuildRequires:	hwloc-devel, autoconf, automake
Requires:	hwloc	

%description
Prime95, also distributed as a command-line utility mprime under FreeBSD and Linux, is a freeware application written by George Woltman. It is used by Great Internet Mersenne Prime Search (GIMPS), a distributed computing project dedicated to Mersenne prime hunting. In overclocking circles, its also commonly used for stability testing.

%prep
%setup -q
%patch0 -p1
%setup -T -D -b 1

%build
cd %{_builddir}/curl-7.76.1
autoreconf -fi
%configure --without-ssl --without-libssh2 --without-libidn --disable-ldap --disable-ldaps --without-gssapi --enable-ipv6 --without-krb4
make
make DESTDIR=/tmp/temp_install install

cd %{_builddir}/prime95-30.3b6
cd gwnum
make -f make64 %{?_smp_mflags}
cd ../linux64
make -f makefile %{?_smp_mflags} -mno-avx
cd ..

#%{?_smp_mflags}

%install
%{__install} -D -m 0755 linux64/mprime %{buildroot}%{_bindir}/mprime

%files
%{_bindir}/mprime


%changelog

