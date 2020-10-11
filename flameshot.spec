%define	debug_package %{nil}

Summary:	Powerful yet simple to use screenshot software
Name:		flameshot	
Version:	0.8.4
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
%{_datadir}/applications/flameshot.desktop
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/dbus-1/interfaces/*.Flameshot.xml
%{_datadir}/dbus-1/services/*.Flameshot.service
%{_datadir}/%{name}
%{_iconsdir}/*
%{_datadir}/metainfo/%{name}.metainfo.xml
%{_datadir}/zsh/site-functions/_flameshot

#------------------------------------------------------------------

%prep
%setup -q

%build
%cmake
%make_build

%install
%make_install -C build
