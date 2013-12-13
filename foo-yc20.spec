Name:            foo-yc20
Version:         1.3.0

Release:         3


%define lv2dir  %{_libdir}/lv2/

Summary:        YC-20 organ emulation
Source:         http://%{name}.googlecode.com/files/%{name}-%{version}.tar.bz2
URL:            http://code.google.com/p/%{name}
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  gtk+2.0-devel
BuildRequires:  jackit-devel
BuildRequires:  lv2-devel
BuildRequires:  slv2-devel
BuildRequires:  desktop-file-utils
BuildRequires:  faust

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


%prep
%setup -q

perl -pi -e 's/\/usr\/local/\/usr\//g' Makefile
perl -pi -e 's/\/lib\/lv2/\/%{_lib}\/lv2/g' Makefile
perl -pi -e 's/CFLAGS=/#CFLAGS=/g' Makefile

%build

CFLAGS="-mfpmath=sse -ffast-math -ftree-vectorize" %make

%install
rm -rf %{buildroot}
%makeinstall_std #DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
    --add-category="Midi" \
    --add-category="X-MandrivaLinux-Sound" \
    --dir %{buildroot}%{_datadir}/applications \
%{buildroot}%{_datadir}/applications/%{name}.desktop


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop

%{lv2dir}%{name}.lv2/%{name}-lv2ui.so
%{lv2dir}%{name}.lv2/%{name}.so
%{lv2dir}%{name}.lv2/%{name}.ttl
%{lv2dir}%{name}.lv2/manifest.ttl



%changelog
* Wed Apr 25 2012 Frank Kober <emuse@mandriva.org> 1.3.0-3
+ Revision: 793406
+ rebuild (emptylog)

* Sun Oct 23 2011 Frank Kober <emuse@mandriva.org> 1.3.0-2
+ Revision: 705781
- rebuild with reduced complier optimization, gcc hangs otherwise

* Tue Apr 19 2011 Frank Kober <emuse@mandriva.org> 1.3.0-1
+ Revision: 656070
- try single core make instead of -j2
- do not use mandriva optflags for better performance
- x86_64 LV2-plugin path fixed in Makefile
- import foo-yc20

