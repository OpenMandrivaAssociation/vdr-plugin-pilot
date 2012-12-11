
%define plugin	pilot
%define name	vdr-plugin-%plugin
%define version	0.0.9
%define rel	16

Summary:	VDR plugin: A zapping co-pilot
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://famillejacques.free.fr/vdr/pilot/
Source:		http://famillejacques.free.fr/vdr/pilot/vdr-%plugin-%version.tar.bz2
Patch0:		01_drop-unused-code.dpatch
Patch1:		02_gcc-4.1.x.dpatch
Patch2:		03_vdr-1.5-i18n.dpatch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
Pilot is a plugin for VDR that brings the ability to quickly browse
the EPG information.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README*




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.9-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.9-15mdv2009.1
+ Revision: 359347
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.9-14mdv2009.0
+ Revision: 197959
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.9-13mdv2009.0
+ Revision: 197702
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- drop unused code (P0 from e-tobi)
- fix compiler warning (P1 from e-tobi)
- adapt to gettext i18n of VDR 1.6 (P2 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.9-12mdv2008.1
+ Revision: 145162
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.9-11mdv2008.1
+ Revision: 103177
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.9-10mdv2008.0
+ Revision: 50027
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.9-9mdv2008.0
+ Revision: 42113
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.9-8mdv2008.0
+ Revision: 22765
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.9-7mdv2007.0
+ Revision: 90956
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.9-6mdv2007.1
+ Revision: 74065
- rebuild for new vdr
- Import vdr-plugin-pilot

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.9-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.9-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.9-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.9-2mdv2007.0
- rebuild for new vdr

* Sun Jul 16 2006 Anssi Hannula <anssi@mandriva.org> 0.0.9-1mdv2007.0
- initial Mandriva release

