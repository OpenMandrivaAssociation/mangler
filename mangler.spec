%define develname %{name}-devel 

Summary:	Mangler is an open source VOIP client
Name:		mangler
Version:	1.2.2
Release:	3
Group:		Networking/Chat
License:	GPLv3
URL:		http://www.mangler.org/
Source0:	http://www.mangler.org/%{name}-%{version}.tar.gz
Source1:	%{name}.png		
BuildRequires:	gtk2-devel 
BuildRequires:	desktop-file-utils
BuildRequires:	freetype-devel
BuildRequires:	gvfs-devel
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libsigc++2.0-devel
BuildRequires:	libcairomm1.0-devel
BuildRequires:	libtool
BuildRequires:	speex-devel
BuildRequires:	pixman-devel
BuildRequires:	pangomm2.4-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gsm-devel
Obsoletes:	%name < %version

%description
Mangler is an open source VOIP client capable of connecting
to Ventrilo 3.x servers. 
It is capable of performing almost all standard user
functionality found in a Windows Ventrilo client.

%package -n	%{develname}
Summary:	Header files and static library for %{name}
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}

%description -n %{develname}
Header files and static library for %{name}.

%prep
%setup -q 

%build
%configure2_5x 
     
%make

%install
%makeinstall

# menu-entry
mkdir -p %{buildroot}/%{_datadir}/applications
cat > %{buildroot}/%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Mangler
GenericName=VOIP Client
Comment=Voice chat on Ventrilo 3.x servers
Exec=%{name}
Icon=%{name}
StartupNotify=true
Terminal=false
Type=Application
Categories=GTK;Network;X-MandrivaLinux-Network-Internet-Chat;
EOF

#remove
rm -f %{buildroot}/%{_datadir}/pixmaps/*.svg

#icon
install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 %SOURCE1 %{buildroot}/%{_datadir}/pixmaps

%files 
%doc COPYING AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/libventrilo3.so.*

%files -n %{develname}
%{_libdir}/libventrilo3.so
%{_libdir}/libventrilo3.a
%{_includedir}/ventrilo3.h


%changelog
* Fri Nov 18 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.2.2-1
+ Revision: 731513
- imported package mangler

