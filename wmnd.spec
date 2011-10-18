Summary:	A dockapp for monitoring network interfaces
Name:		wmnd
Version:	0.4.16
Release:	1
License:	GPLv2
Group:		Monitoring
Source0:	http://www.thregr.org/~wavexx/software/wmnd/releases/%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.bz2
URL:		http://www.thregr.org/~wavexx/software/wmnd/
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxpm-devel
BuildRequires:	libsm-devel

%description
WMND (WindowMaker Network Devices) is a network monitoring
dock app improved and based on WMiFS 1.3b. You can find the
features of WMiFS 1.3b from documents in directory WMiFS.

%prep
%setup -q

%build
%configure2_5x
%make

%install
[ -d %{buildroot} ] && rm -rf %{buildroot}

%makeinstall_std
install -m 755 -d %{buildroot}%{_datadir}/pixmaps
tar xOjf %SOURCE1 %{name}-48x48.png > %{buildroot}%{_datadir}/pixmaps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=wmnd
Comment=A dockapp for monitoring network interfaces
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-Monitoring;System;Monitor;
EOF

%clean
[ -z %{buildroot} ] || {
    rm -rf %{buildroot}
}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr (-,root,root)
%doc examples/wmndrc NEWS AUTHORS README TODO ChangeLog
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/wmndrc


