#define	debug_package %{nil}
%define _empty_manifest_terminate_build 0

Summary:	Powerful yet simple to use screenshot software
Name:		flameshot	
Version:	0.10.1
Release:	1
License:	GPLv3
Group:		Graphics
Url:		https://flameshot.js.org
Source0:	https://github.com/lupoDharkael/flameshot/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	qt5-devel
BuildRequires:	qt5-linguist
BuildRequires:  qt5-linguist-tools
BuildRequires:	git
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  qmake5
BuildRequires:  cmake
BuildRequires:  qt5-qtbase-devel

%description
Flameshot is a screenshot software, it's
powerful yet simple to use for GNU/Linux.

%files
%doc *.md LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/org.flameshot.Flameshot.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/dbus-1/interfaces/*.Flameshot.xml
%{_datadir}/dbus-1/services/*.Flameshot.service
%{_datadir}/%{name}
%{_iconsdir}/*
%{_datadir}/metainfo/org.flameshot.Flameshot.metainfo.xml
%{_datadir}/zsh/site-functions/_flameshot
%{_mandir}/man1/flameshot.1.*

#------------------------------------------------------------------

%prep
%setup -q

%build
%cmake
%make_build

%install
%make_install -C build
