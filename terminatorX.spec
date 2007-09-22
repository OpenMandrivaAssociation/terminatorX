%define name 	terminatorX
%define version 3.82
%define release %mkrel 3

Summary: 	Realtime Audio Synthesizer
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Group: 		Sound
License: 	GPL
URL: 		http://www.terminatorx.cx/

Source: 	%{name}-%{version}.tar.bz2
Source1: 	%{name}48.png
Source2: 	%{name}32.png
Source3: 	%{name}16.png
Buildroot: 	%{_tmppath}/%{name}-buildroot

BuildRequires:	pkgconfig ladspa-devel zlib-devel sox-devel mpg123 vorbis-tools
BuildRequires:	gtk2-devel libmad-devel libvorbis-devel libaudiofile-devel
BuildRequires:	libalsa-devel libxml2-devel liblrdf-devel XFree86-devel
BuildRequires:	gtk+2-devel libgdk_pixbuf2.0-devel
BuildRequires:	librarian-devel jackit-devel
Requires: liblrdf2-common

%description
TerminatorX is a realtime audio synthesizer that allows you to "scratch" on
digitally sampled audio data (*.wav, *.au, *.mp3, etc.) the way hiphop-DJs
scratch on vinyl records. It features multiple turntables, realtime effects
(built-in as well as LADSPA plugin effects), a sequencer, and an easy-to-use
GTK+ GUI.

%prep
%setup -q

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
Categories=X-MandrivaLinux-Multimedia-Sound;Player;X-MandrivaLinux-CrossDesktop
EOF

#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
cat %SOURCE1 > $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
cat %SOURCE2 > $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
cat %SOURCE3 > $RPM_BUILD_ROOT/%_miconsdir/%name.png
 
%post
%{update_menus}
scrollkeeper-update -p /var/lib/scrollkeeper -o /usr/share/omf/terminatorX

%postun
%{clean_menus}  
scrollkeeper-update

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%doc COPYING AUTHORS ChangeLog NEWS README README.PERFORMANCE THANKS TODO
%{_datadir}/gnome/apps/Multimedia/%name.desktop
%{_mandir}/man1/*
%{_datadir}/omf/%name/
%{_datadir}/pixmaps/*.png
%{_datadir}/%name
%{_datadir}/mime-info/terminatorX.keys
%{_datadir}/mime-info/terminatorX.mime
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/%name.desktop
