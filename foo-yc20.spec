%define debug_package %{nil}
%define lv2dir  %{_libdir}/lv2/

Summary:	YC-20 organ emulation
Name:		foo-yc20
Version:	1.3.0
Release:	5
License:	GPLv2+
Group:		Sound
Source0:	http://%{name}.googlecode.com/files/%{name}-%{version}.tar.bz2
Url:		https://code.google.com/p/%{name}
BuildRequires:	desktop-file-utils
BuildRequires:	faust
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(lv2)
BuildRequires:	pkgconfig(slv2)

%description
The YC-20 is a divide-down combo organ designed in the late 60's. This
emulation faithfully copies the features, sounds and flaws of the
original organ. It comes as standalone synth and as LV2 plugin. Features
are as follows.

o Physical modelling, no polyphony restrictions
o 61 keys
o Two main voice sections
o Switchable bass section
o Realism control to add flaws found in the real organ

%files
%doc README
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{lv2dir}%{name}.lv2/%{name}-lv2ui.so
%{lv2dir}%{name}.lv2/%{name}.so
%{lv2dir}%{name}.lv2/%{name}.ttl
%{lv2dir}%{name}.lv2/manifest.ttl

#----------------------------------------------------------------------------

%prep
%setup -q

perl -pi -e 's/\/usr\/local/\/usr\//g' Makefile
perl -pi -e 's/\/lib\/lv2/\/%{_lib}\/lv2/g' Makefile
perl -pi -e 's/CFLAGS=/#CFLAGS=/g' Makefile

%build
CFLAGS="-mfpmath=sse -ffast-math -ftree-vectorize" %make

%install
%makeinstall_std

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --add-category="Midi" \
    --add-category="X-MandrivaLinux-Sound" \
    --dir %{buildroot}%{_datadir}/applications \
    %{buildroot}%{_datadir}/applications/%{name}.desktop

