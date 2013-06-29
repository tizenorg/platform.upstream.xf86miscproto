Name:           xf86miscproto
Version:        0.9.3
Release:        1
License:        MIT
Summary:        xf86miscproto protocol
Url:            http://www.x.org
Group:          Development/System
Source0:        %{name}-%{version}.tar.bz2
Source1001: 	xf86miscproto.manifest

BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xorg-macros)

%description
%{summary}.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%configure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

make %{?_smp_mflags}

%install
%make_install

%remove_docs


%files
%manifest %{name}.manifest
%license COPYING
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
