# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       nethogs

# >> macros
# << macros

Summary:    a small 'net top' tool
Version:    0.8.7
Release:    1
Group:      Applications/Internet
License:    GPLv2
URL:        https://github.com/raboof/nethogs
Source0:    https://github.com/raboof/nethogs/archive/%{name}-%{version}.tar.gz
Source1:    files/%{name}.desktop
Source2:    files/%{name}.svgz
Source3:    files/%{name}_86.png
Source4:    files/%{name}_108.png
Source5:    files/%{name}_128.png
Source6:    files/%{name}_172.png
Source7:    files/%{name}_256.png
Source8:    files/%{name}_512.png
Source100:  nethogs.yaml
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  libpcap-devel
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
Obsoletes:   nethogs <= 0.8.1
Obsoletes:   openrepos-nethogs <= %{version}

%description
NetHogs is a small 'net top' tool. Instead of breaking the traffic down per
protocol or per subnet, like most tools do, it groups bandwidth by process.
NetHogs does not rely on a special kernel module to be loaded. If there's
suddenly a lot of network traffic, you can fire up NetHogs and immediately see
which PID is causing this. This makes it easy to indentify programs that have
gone wild and are suddenly taking up your bandwidth.

%if "%{?vendor}" == "chum"
Type: console-application
PackagerName: nephros
Categories:
 - Network
 - Utility
Custom:
  PackagingRepo: https://github.com/sailfishos-chum/nethogs
  Repo: https://github.com/raboof/nethogs
Icon: https://github.com/sailfishos-chum/nethogs/raw/legacy/rpm/nethogs_256.png
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
make %{?_smp_mflags} nethogs
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre

# >> install post
%{__make} install PREFIX="%{buildroot}"/usr
%{__install} -p -D -m 644 %SOURCE1 %{buildroot}%{_datadir}/applications/%{name}.desktop
%{__install} -p -D -m 644 %SOURCE2 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
%{__install} -p -D -m 644 %SOURCE3 %{buildroot}%{_datadir}/icons/hicolor/86x86/apps/%{name}.png
%{__install} -p -D -m 644 %SOURCE4 %{buildroot}%{_datadir}/icons/hicolor/108x108/apps/%{name}.png
%{__install} -p -D -m 644 %SOURCE5 %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{__install} -p -D -m 644 %SOURCE6 %{buildroot}%{_datadir}/icons/hicolor/172x172/apps/%{name}.png
%{__install} -p -D -m 644 %SOURCE7 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{__install} -p -D -m 644 %SOURCE8 %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
# disable man pages
rm -rf %{buildroot}%{_mandir}
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%defattr(-, root, root, 0755)
%license COPYING
%{_sbindir}/nethogs
%defattr(-, root, root, 0644)
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svgz
%{_datadir}/applications/%{name}.desktop
# >> files
# << files
