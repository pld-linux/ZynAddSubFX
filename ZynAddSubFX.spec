%define 	namelc zynaddsubfx
Summary:	Realtime software synthesizer
Summary(pl.UTF-8):	Syntezator programowy działający w czasie rzeczywistym
Name:		ZynAddSubFX
Version:	2.4.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/%{namelc}/%{name}-%{version}.tar.bz2
# Source0-md5:	59eb69ce24d6f8c605f8ba43958d0526
Source1:	%{name}.desktop
Patch0:		%{name}-make-jN.patch
URL:		http://zynaddsubfx.sourceforge.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	fftw3-devel
BuildRequires:	fltk-devel >= 1.1.3
BuildRequires:	jack-audio-connection-kit-devel >= 0.66.3
BuildRequires:	mxml-devel >= 2.2
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZynAddSubFX is a software synthesizer capable of making a countless
number of instruments.

%description -l pl.UTF-8
ZynAddSubFX jest programowym syntezatorem zdolnym do tworzenia
niezliczonej ilości instrumentów.

%prep
%setup -q
%patch0 -p1
sed -i -e "s|-O6|\$(OPTFLAGS)|" src/Makefile

%build
%{__make} -C src \
%ifnarch %{ix86} %{x8664}
	ASM_F2I=NO \
%endif
	OPTFLAGS="%{rpmcflags}" \
	LINUX_AUDIOOUT="OSS_AND_JACK" \
	CXX="%{__cxx}"

%{__make} -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{namelc}} \
	$RPM_BUILD_ROOT%{_desktopdir}

install -c src/zynaddsubfx $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install -c doc/%{namelc}.html $RPM_BUILD_ROOT%{_datadir}/%{namelc}
cp -r examples $RPM_BUILD_ROOT%{_datadir}/%{namelc}/
cp -r banks $RPM_BUILD_ROOT%{_datadir}/%{namelc}/
cp -r doc/images $RPM_BUILD_ROOT%{_datadir}/%{namelc}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ.txt HISTORY.txt README.txt
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{namelc}
%{_desktopdir}/%{name}.desktop
