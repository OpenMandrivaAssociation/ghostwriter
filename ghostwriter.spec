%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Name: ghostwriter
Version: 25.08.2
Release: %{?git:0.%{git}.}1
Group: Office
License: GPLv3+ and CC-BY and CC-BY-SA and MPLv1.1 and BSD and LGPLv3 and MIT and ISC
Summary: Cross-platform, aesthetic, distraction-free Markdown editor
URL: https://github.com/wereturtle/%{name}
%if 0%{?git:1}
Source0: https://invent.kde.org/office/ghostwriter/-/archive/%{gitbranch}/ghostwriter-%{gitbranchd}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/ghostwriter-%{version}.tar.xz
%endif
BuildRequires: cmake ninja
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Help)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6QmlCore)
BuildRequires: cmake(Qt6QmlNetwork)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: hunspell-devel
BuildRequires: pkgconfig(appstream-glib)
BuildRequires: qt6-qtbase-theme-gtk3

Provides: bundled(cmark-gfm) = 0.29.0
Provides: bundled(fontawesome-fonts) = 6.10.2
Provides: bundled(nodejs-mathjax-full) = 3.1.2
Provides: bundled(nodejs-react) = 17.0.1
Provides: bundled(QtAwesome) = 6

Requires: hicolor-icon-theme
Requires: qt6-qtwebengine

Recommends: cmark%{?_isa}
Recommends: multimarkdown%{?_isa}

%rename plasma6-ghostwriter

BuildSystem: cmake
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
Ghostwriter is a text editor for Markdown, which is a plain text markup
format created by John Gruber. For more information about Markdown, please
visit John Gruber's website at http://www.daringfireball.net.

Ghostwriter provides a relaxing, distraction-free writing environment,
whether your masterpiece be that next blog post, your school paper,
or your novel.

%prep -a
# We use the system copy
rm -rf 3rdparty/hunspell

%files -f ghostwriter.lang
%{_bindir}/ghostwriter
%{_datadir}/applications/org.kde.ghostwriter.desktop
%{_datadir}/icons/hicolor/*/apps/ghostwriter.*
%{_datadir}/metainfo/org.kde.ghostwriter.metainfo.xml
%{_mandir}/man1/ghostwriter.1*
