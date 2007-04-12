
%define plugin	pilot
%define name	vdr-plugin-%plugin
%define version	0.0.9
%define rel	7

Summary:	VDR plugin: A zapping co-pilot
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://famillejacques.free.fr/vdr/pilot/
Source:		http://famillejacques.free.fr/vdr/pilot/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
Pilot is a plugin for VDR that brings the ability to quickly browse
the EPG information.

%prep
%setup -q -n %plugin-%version

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


