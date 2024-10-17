%define name 	terminatorX
%define version 3.82
%define release %mkrel 9

Summary: 	Realtime Audio Synthesizer
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Group: 		Sound
License: 	GPLv2+
URL: 		https://www.terminatorx.cx/

Source: 	%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
Patch0:		%{name}-3.82-fix-str-fmt.patch
Buildroot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	libx11-devel
BuildRequires:	libxi-devel
BuildRequires:	libxxf86dga-devel
BuildRequires:	libalsa-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libcap-devel
BuildRequires:	libaudiofile-devel
BuildRequires:	jackit-devel
BuildRequires:	liblrdf-devel
BuildRequires:	libmad-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libxml2-devel
BuildRequires:	zlib-devel
BuildRequires:	rarian
BuildRequires:	ladspa-devel

%description
TerminatorX is a realtime audio synthesizer that allows you to "scratch" on
digitally sampled audio data (*.wav, *.au, *.mp3, etc.) the way hiphop-DJs
scratch on vinyl records. It features multiple turntables, realtime effects
(built-in as well as LADSPA plugin effects), a sequencer, and an easy-to-use
GTK+ GUI.

%prep
%setup -q
%patch0 -p1 -b .strfmt

%build
%configure2_5x --enable-alsa
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

#menu
install -d -m755 %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=terminatorX
GenericName=Realtime Audio Synthesizer
Comment=Scratch on digitally sampled audio data
Exec=terminatorX
Icon=terminatorX-app
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Player;
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png
 
%if %mdkversion < 200900
%post
%{update_menus} 
%{update_scrollkeeper}
%{update_desktop_database} 
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}  
%{clean_scrollkeeper}
%{update_menus} 
%endif

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%doc COPYING AUTHORS ChangeLog NEWS README README.PERFORMANCE THANKS TODO
%{_mandir}/man1/*
%{_datadir}/omf/%name/
%{_datadir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/%{name}.desktop
