Summary:	Simple image viewer for KDE
Summary(pl):	Prosta przegl�darka obrazk�w dla KDE
Name:		gwenview
Version:	1.0.0
Release:	0.1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://dl.sourceforge.net/gwenview/%{name}-%{version}.tar.bz2
# Source0-md5:	e19e0ed3fb6ce857241fcaf2845d7271
URL:		http://gwenview.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Gwenview is an image viewer for KDE.

It features a folder tree window and a file list window to provide
easy navigation in your file hierarchy. Image loading is done by the
Qt library, so it supports all image formats your Qt installation
supports.

%description -l pl
Gwenview to przegl�darka obrazk�w dla KDE. Ma okno z drzewem katalog�w
oraz okno z list� plik�w w celu zapewnienia �atwej nawigacji w
hierarchii plik�w. Wczytywanie obrazk�w jest wykonywane przez
bibliotek� Qt, wi�c przegl�darka obs�uguje wszystkie formaty
obs�ugiwane przez zainstalowan� wersj� Qt.

%prep
%setup -q

%build
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# temporary, until glibc update
mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{nb,no}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gwenview
%{_datadir}/apps/gwenview
%{_pixmapsdir}/*/*/apps/gwenview.png
%{_desktopdir}/kde/gwenview.desktop
%{_datadir}/apps/konqueror/servicemenus/konqgwenview.desktop
%{_mandir}/man1/*
