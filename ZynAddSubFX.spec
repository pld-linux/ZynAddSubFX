#
# Conditional build:
# _with_jack		- build with jack audio connection kit
#
%define 	doc_ver  1.4.2
Summary:	Realtime software synthesizer
Summary(pl):	Syntezator programowy dzia³aj±cy w czasie rzeczywistym
Name:		ZynAddSubFX
Version:	1.4.2
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/sourceforge/zynaddsubfx/%{name}-%{version}.tar.gz
# Source0-md5:	0e071d5c9babf4cae71677bdb3805c29
Source1:	http://dl.sourceforge.net/sourceforge/zynaddsubfx/%{name}-doc-%{doc_ver}.tar.gz
# Source1-md5:	fadaab515d02517fbbc3014164e4aca2
Source2:	%{name}.desktop
Patch0:		%{name}-jack.patch
Patch1:		%{name}-optflags.patch
URL:		http://zynaddsubfx.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	fftw-devel
BuildRequires:	fltk-devel >= 1.1.3
%{?_with_jack:BuildRequires:	jack-audio-connection-kit-devel >= 0.66.3}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZynAddSubFX is a software synthesizer capable of making a countless
number of instruments.

%description -l pl
ZynAddSubFX jest programowym syntezatorem zdolnym do tworzenia
niezliczonej ilo¶ci instrumentów.

%prep
%setup -q -a1
%{?_with_jack:%patch0 -p1}
%patch1 -p1

%build
cd src
%{__make} OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{%{_bindir},%{_datadir}/%{name}} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/images \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/examples/Instruments \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/examples/Scales

install -c src/zynaddsubfx $RPM_BUILD_ROOT%{_bindir}
cd %{name}-doc-%{doc_ver}
bzip2 -dc demo_src.tar.bz2 | tar xf - -C ../examples
cp images/* $RPM_BUILD_ROOT%{_datadir}/%{name}/images
cp *.ogg $RPM_BUILD_ROOT%{_datadir}/%{name}
cp *.html $RPM_BUILD_ROOT%{_datadir}/%{name}
cd ..
cp examples/*.*zyn $RPM_BUILD_ROOT%{_datadir}/%{name}/examples
cp examples/demo_src/*.*zyn $RPM_BUILD_ROOT%{_datadir}/%{name}/examples
cp examples/Instruments/*.*zyn $RPM_BUILD_ROOT%{_datadir}/%{name}/examples/Instruments
cp examples/Scales/*.*zyn $RPM_BUILD_ROOT%{_datadir}/%{name}/examples/Scales

install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ.txt HISTORY.txt README.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
