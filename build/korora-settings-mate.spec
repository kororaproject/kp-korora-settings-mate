%define  debug_package %{nil}

Summary:    Korora configs for MATE
Name:       korora-settings-mate
Version:    0.4
Release:    1%{?dist}

Group:      System Environment/Base
License:    GPLv3+
Url:        http://kororaproject.org
Source0:    %{name}-%{version}.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#BuildArch: noarch

%description
%{summary}.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
#mkdir -p %{buildroot}%{_libdir}/firefox/browser/defaults/profile
mkdir -p %{buildroot}%{_datadir}/mate-panel/layouts
mkdir -p %{buildroot}%{_sysconfdir}/skel/.config

cp -a %{_builddir}/%{name}-%{version}/autostart %{buildroot}%{_sysconfdir}/skel/.config/
cp -a %{_builddir}/%{name}-%{version}/compiz %{buildroot}%{_sysconfdir}/skel/.config/
cp -a %{_builddir}/%{name}-%{version}/plank %{buildroot}%{_sysconfdir}/skel/.config/
cp -a %{_builddir}/%{name}-%{version}/mate-panel-layouts/korora.layout %{buildroot}%{_datadir}/mate-panel/layouts/
cp %{_builddir}/%{name}-%{version}/mimeapps.list %{buildroot}%{_sysconfdir}/skel/.config/

%clean
rm -rf %{buildroot}

%pre

%post
#cd %{_libdir}/firefox/browser/defaults/profile/

%postun
# clean up the link on uninstall of this package (not updates though)
#if [ "$1" == "0" ]
#then
#  cd %{_libdir}/firefox/browser/defaults/profile/
#  unlink prefs.js 2>/dev/null
#  cd -
#fi

%files
%defattr(-,root,root,-)
%{_sysconfdir}/skel/.config/autostart/compiz-mate-gtk.desktop
%{_sysconfdir}/skel/.config/autostart/plank.desktop
%{_sysconfdir}/skel/.config/compiz
%{_sysconfdir}/skel/.config/plank
%{_sysconfdir}/skel/.config/mimeapps.list
%{_datadir}/mate-panel/layouts/korora.layout

%changelog
* Thu Jul 16 2015 Ian Firns <firnsy@kororaproject.org> 0.4-1
- Added start up delay to plank to solve non-appearance issues

* Sun Feb 22 2015 Ian Firns <firnsy@kororaproject.org> 0.3-1
- Added preferred applications

* Sun Feb 22 2015 Ian Firns <firnsy@kororaproject.org> 0.1-1
- Initial settings for MATE
