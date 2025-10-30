Summary:	Powerful yet simple to use screenshot software
Name:		flameshot	
Version:	13.3.0
Release:	1
License:	GPLv3
Group:		Graphics
Url:		https://flameshot.org
Source0:	https://github.com/flameshot-org/flameshot/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	git
BuildRequires:	pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  qmake-qt6
BuildSystem:	cmake

%description
Flameshot is a screenshot software, it's
powerful yet simple to use for GNU/Linux.

%install -a
%libpackages
echo '%{_libdir}/cmake/KDSingleApplication-qt6' >>%{specpartsdir}/%{mklibname -s -d kdsingleapplication-qt6}.specpart

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
%{_datadir}/fish/vendor_completions.d/flameshot.fish
%{_mandir}/man1/flameshot.1.*
