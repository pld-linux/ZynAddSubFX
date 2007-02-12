%define 	doc_ver	1.4.3
Summary:	Realtime software synthesizer
Summary(pl.UTF-8):	Syntezator programowy działający w czasie rzeczywistym
Name:		ZynAddSubFX
Version:	2.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/zynaddsubfx/%{name}-%{version}.tar.bz2
# Source0-md5:	fca8560e37d799bd20d17e22b11674d6
#Source1:	http://dl.sourceforge.net/zynaddsubfx/%{name}-doc-%{doc_ver}.tar.gz
Source2:	%{name}.desktop
URL:		http://zynaddsubfx.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	fftw3-devel
BuildRequires:	fltk-devel >= 1.1.3
BuildRequires:	jack-audio-connection-kit-devel >= 0.66.3
BuildRequires:	mxml >= 2.2
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
sed -i -e "s|-O6|\$(OPTFLAGS)|" src/Makefile

%build
%{__make} -C src \
%ifnarch %{ix86} %{x8664}
	ASM_F2I=NO \
%endif
	OPTFLAGS="%{rpmcflags}" \
	LINUX_AUDIOOUT="OSS_AND_JACK" \
	CXX="%{__cxx}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}} \
	$RPM_BUILD_ROOT%{_desktopdir} \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/images

install -c src/zynaddsubfx $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
mv banks/* examples/Banks
cp -r examples $RPM_BUILD_ROOT%{_datadir}/%{name}/

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
