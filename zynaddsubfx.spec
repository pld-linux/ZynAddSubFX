Summary:	Realtime software synthesizer
Summary(pl.UTF-8):	Syntezator programowy działający w czasie rzeczywistym
Name:		zynaddsubfx
Version:	3.0.4
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	090331a1c26f89aa52bd7e35f40ce6b6
Patch0:		cxx_flags.patch
URL:		http://zynaddsubfx.sourceforge.net/
BuildRequires:	alsa-lib-devel
#BuildRequires:	doxygen
BuildRequires:	dssi-devel >= 0.9.0
BuildRequires:	fftw3-devel
BuildRequires:	fltk-devel >= 1.1.3
BuildRequires:	jack-audio-connection-kit-devel >= 0.66.3
BuildRequires:	lash-devel
BuildRequires:	liblo-devel >= 0.28
BuildRequires:	mxml-devel >= 2.2
BuildRequires:	pkgconfig
BuildRequires:	portaudio >= 19
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	sed >= 4.0
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	zlib-devel
Obsoletes:	ZynAddSubFX
Obsoletes:	zynaddsubfx-fusion
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/(dssi|lv2|vst)

%description
ZynAddSubFX is a software synthesizer capable of making a countless
number of instruments.

%description -l pl.UTF-8
ZynAddSubFX jest programowym syntezatorem zdolnym do tworzenia
niezliczonej ilości instrumentów.

%package dssi
Summary:	Realtime software synthesizer - DSSI plugin
Summary(pl.UTF-8):	Syntezator programowy działający w czasie rzeczywistym, plugin DSSI
Group:		X11/Applications/Sound
Obsoletes:	ZynAddSubFX-dssi
Obsoletes:	zynaddsubfx-fusion-dssi
Requires:	%{name} = %{version}-%{release}

%description dssi
ZynAddSubFX software synthesizer as a DSSI plugin.

%description dssi -l pl.UTF-8
Syntezator ZynAddSubFX jako wtyczka DSSI.

%package lv2
Summary:	Realtime software synthesizer - LV2 plugin
Summary(pl.UTF-8):	Syntezator programowy działający w czasie rzeczywistym, plugin LV2
Group:		X11/Applications/Sound
Obsoletes:	ZynAddSubFX-lv2
Obsoletes:	zynaddsubfx-fusion-lv2
Requires:	%{name} = %{version}-%{release}

%description lv2
ZynAddSubFX software synthesizer as a LV2 plugin.

%description lv2 -l pl.UTF-8
Syntezator ZynAddSubFX jako wtyczka LV2.

%package vst
Summary:	Realtime software synthesizer - VST plugin
Summary(pl.UTF-8):	Syntezator programowy działający w czasie rzeczywistym, plugin VST
Group:		X11/Applications/Sound
Obsoletes:	ZynAddSubFX-vst
Obsoletes:	zynaddsubfx-fusion-vst
Requires:	%{name} = %{version}-%{release}

%description vst
ZynAddSubFX software synthesizer as a VST plugin.

%description vst -l pl.UTF-8
Syntezator ZynAddSubFX jako wtyczka VST.

%prep
%setup -qn %{name}-%{version}

%patch0 -p1

%build

mkdir build
cd build
%cmake .. \
	-DPluginLibDir=%{_lib} \
	-DCMAKE_CXX_FLAGS_RELEASE="%{rpmcxxflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}} \
	$RPM_BUILD_ROOT%{_desktopdir}

%{__make} -C build install \
	DESTDIR="$RPM_BUILD_ROOT"

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.txt HISTORY.txt README.adoc
%attr(755,root,root) %{_bindir}/zynaddsubfx
%attr(755,root,root) %{_bindir}/zynaddsubfx-ext-gui
%{_datadir}/zynaddsubfx
%{_pixmapsdir}/zynaddsubfx.svg
%{_desktopdir}/zynaddsubfx-*.desktop

%files dssi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/dssi/libzynaddsubfx_dssi.so

%files lv2
%defattr(644,root,root,755)
%dir %{_libdir}/lv2/*.lv2
%dir %{_libdir}/lv2/ZynAddSubFX.lv2presets
%attr(755,root,root) %{_libdir}/lv2/*.lv2/*.so
%{_libdir}/lv2/*.lv2/*.ttl
%{_libdir}/lv2/ZynAddSubFX.lv2presets/*.ttl

%files vst
%defattr(644,root,root,755)
%dir %{_libdir}/vst
%attr(755,root,root) %{_libdir}/vst/*.so
