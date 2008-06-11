%define name 	terminatorX
%define version 3.82
%define release %mkrel 4

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
BuildRequires:	libalsa-devel libxml2-devel liblrdf-devel X11-devel
BuildRequires:	gtk+2-devel libgdk_pixbuf2.0-devel gnome-libs gnome-devel
BuildRequires:	rarian jackit-devel
Requires: %{mklibname lrdf2}-common
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

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
Categories=AudioVideo;Audio;Player;X-MandrivaLinux-CrossDesktop
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
%{update_scrollkeeper}
%{update_desktop_database} 

%postun
%{clean_menus}  
%{clean_scrollkeeper}
%{update_menus} 

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%doc COPYING AUTHORS ChangeLog NEWS README README.PERFORMANCE THANKS TODO
%{_datadir}/gnome/apps/Multimedia/%name.desktop
%{_mandir}/man1/*
%{_datadir}/omf/%name/
%{_datadir}/pixmaps
%{_datadir}/%name
%{_datadir}/mime-info
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
%{_datadir}/applications/%{name}.desktop
