%define 	doc_ver		1.4.3
Summary:	Realtime software synthesizer
Summary(pl):	Syntezator programowy dzia³aj±cy w czasie rzeczywistym
Name:		ZynAddSubFX
Version:	2.1.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://mesh.dl.sourceforge.net/sourceforge/zynaddsubfx/%{name}-%{version}.tar.bz2
# Source0-md5:	a078a85fc140bad8da6dd8114b9e5f41
Source1:	http://mesh.dl.sourceforge.net/sourceforge/zynaddsubfx/%{name}-doc-%{doc_ver}.tar.gz
# Source1-md5:	64a1c8d991e7ec9ffe0f9fbf929af62f
Source2:	%{name}.desktop
URL:		http://zynaddsubfx.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	fftw3-devel
BuildRequires:	fltk-devel >= 1.1.3
BuildRequires:	jack-audio-connection-kit-devel >= 0.66.3
BuildRequires:	mxml >= 2.0
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZynAddSubFX is a software synthesizer capable of making a countless
number of instruments.

%description -l pl
ZynAddSubFX jest programowym syntezatorem zdolnym do tworzenia
niezliczonej ilo¶ci instrumentów.

%prep
%setup -q -a1
sed -i -e "s|-O6|\$(OPTFLAGS)|" src/Makefile

%build
cd src
%{__make} OPTFLAGS="%{rpmcflags}" \
	LINUX_AUDIOOUT="OSS_AND_JACK" \
	CXX=%{__cxx}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/images \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/examples/Banks \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/examples/Instruments \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/examples/Scales

install -c src/zynaddsubfx $RPM_BUILD_ROOT%{_bindir}
cp examples/*.xmz $RPM_BUILD_ROOT%{_datadir}/%{name}/examples
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

# NOTE:
# Outdated, new version not ready yet
#
#cd %{name}-doc-%{doc_ver}
#bzip2 -dc demo_src.tar.bz2 | tar xf - -C ../examples
#cp images/* $RPM_BUILD_ROOT%{_datadir}/%{name}/images
#cp *.ogg $RPM_BUILD_ROOT%{_datadir}/%{name}
#cp *.html $RPM_BUILD_ROOT%{_datadir}/%{name}
#cd ..
#cp examples/demo_src/*.*zyn $RPM_BUILD_ROOT%{_datadir}/%{name}/examples/demos

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ.txt HISTORY.txt README.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
