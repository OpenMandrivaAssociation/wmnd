Summary:	A dockapp for monitoring network interfaces
Name:		wmnd
Version:	0.4.16
Release:	1
License:	GPLv2
Group:		Monitoring
Source0:	http://www.thregr.org/~wavexx/software/wmnd/releases/%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.bz2
URL:		http://www.thregr.org/~wavexx/software/wmnd/
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(sm)

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




%changelog
* Tue Oct 18 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.4.16-1
+ Revision: 705252
- new version 0.4.16
  cleaned up spec file

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 0.4.12-7mdv2010.0
+ Revision: 434892
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 0.4.12-6mdv2009.0
+ Revision: 262060
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.4.12-5mdv2009.0
+ Revision: 256209
- rebuild
- drop old menu

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 3mdv2008.1-current
+ Revision: 140932
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'


* Tue Feb 06 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.4.12-3mdv2007.0
+ Revision: 116895
- fixed .desktop file Comment

* Mon Jan 29 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.4.12-2mdv2007.1
+ Revision: 115170
- menu migrated to XDG scheme, for great compliance
- cleanup
  . manpages are compressed automatically
  . removing generic FSF 'INSTALL' from package as it is mostly useless

* Mon Jan 29 2007 Gustavo De Nardin <gustavodn@mandriva.com> 0.4.12-1mdv2007.1
+ Revision: 114943
- new version 0.4.12
- fixed Group and menu category, better Summary
- fixed BuildRequires
- spec cleanup

* Sat Sep 11 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.4.9-1mdk
- 0.4.9

