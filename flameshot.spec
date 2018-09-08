%define	debug_package %{nil}

Summary:	Powerful yet simple to use screenshot software
Name:		flameshot	
Version:	0.6.0
Release:	1
License:	GPLv3
Group:		Graphics
Url:		https://flameshot.js.org
Source0:	https://github.com/lupoDharkael/flameshot/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	qt5-devel
BuildRequires:	qt5-linguist
BuildRequirea:  qt5-linguist-tools
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
%{_datadir}/metainfo/%{name}.appdata.xml

#------------------------------------------------------------------

%prep
%setup -q

%build
%qmake_qt5 CONFIG+=packaging CONFIG-=debug CONFIG+=release
%make

%install
%makeinstall INSTALL_ROOT=%{buildroot}
