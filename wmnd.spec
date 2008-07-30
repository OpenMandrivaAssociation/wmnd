%define version 0.4.12
%define release %mkrel 5
%define name wmnd

Summary:	A dockapp for monitoring network interfaces
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
URL:		http://www.yuv.info/wmnd/
BuildRequires:	libx11-devel
BuildRequires:	libxext-devel
BuildRequires:	libxpm-devel
BuildRequires:	libsm-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
WMND (WindowMaker Network Devices) is a network monitoring
dock app improved and based on WMiFS 1.3b. You can find the
features of WMiFS 1.3b from documents in directory WMiFS.

%prep
%setup -q

%build
%configure
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
[ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

install -m 755 -d $RPM_BUILD_ROOT%{_miconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_iconsdir}
install -m 755 -d $RPM_BUILD_ROOT%{_liconsdir}
tar xOjf %SOURCE1 %{name}-16x16.png > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-32x32.png > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
tar xOjf %SOURCE1 %{name}-48x48.png > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/

install -m 755 src/wmnd $RPM_BUILD_ROOT%{_bindir}/wmnd
install -m 644 doc/wmnd.1 $RPM_BUILD_ROOT%{_mandir}/man1/wmnd.1


mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
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
[ -z $RPM_BUILD_ROOT ] || {
    rm -rf $RPM_BUILD_ROOT
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
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


