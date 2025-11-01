Summary:	Powerful yet simple to use screenshot software
Name:		flameshot	
Version:	13.3.0
Release:	1
License:	GPLv3
Group:		Graphics
Url:		https://flameshot.org
Source0:	https://github.com/flameshot-org/flameshot/archive/refs/tags/v%{version}.tar.gz
BuildRequires:	git
BuildRequires:	cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6LinguistTools)
BuildRequires:	cmake(KDSingleApplication-qt6)
BuildRequires:	cmake(qtcolorwidgets)
BuildRequires:  qmake-qt6
BuildSystem:	cmake
BuildOption:	-DUSE_BUNDLED_KDSINGLEAPPLICATION:BOOL=OFF
BuildOption:	-DUSE_SYSTEM_QTCOLORWIDGETS:BOOL=ON

%patchlist
flameshot-system-QtColorWidgets.patch

%description
Flameshot is a screenshot software, it's
powerful yet simple to use for GNU/Linux.

%install -a
%libpackages

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
