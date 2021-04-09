Name:		htop		
Version:	3.0.6
Release:	1%{?dist}
Summary:	htop is a cross-platform interactive process viewer.

Group:		System/Monitoring
License:	GPL-2.0
URL:		https://github.com/htop-dev/htop/
Source0:	htop-3.0.6.tar.gz

BuildRequires:	ncurses-devel, hwloc-devel, autoconf
Requires:	ncurses, hwloc

%description
htop allows scrolling the list of processes vertically and horizontally to see their full command lines and related information like memory and CPU consumption.

The information displayed is configurable through a graphical setup and can be sorted and filtered interactively.

Tasks related to processes (e.g. killing and renicing) can be done without entering their PIDs.

Running htop requires ncurses libraries (typically named libncursesw*).

%prep
%setup -q


%build
./autogen.sh
%configure --enable-hwloc
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
/usr/bin/htop
/usr/share/applications/htop.desktop
/usr/share/icons/hicolor/scalable/apps/htop.svg
%doc /usr/share/man/man1/htop.1.gz
/usr/share/pixmaps/htop.png



%changelog
* Thu Apr 8 2021 Richard.Xiong@qube-rt.com
- initial build of dev branch
