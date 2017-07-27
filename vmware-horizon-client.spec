%undefine _missing_build_ids_terminate_build
%global ver 4.4.0
%global rel 5167967

Summary: Remote access client for VMware Horizon
Name: vmware-horizon-client
Version: %{ver}.%{rel}
Release: 1
URL: https://www.vmware.com/products/horizon.html
Source0: https://download3.vmware.com/software/view/viewclients/CART17Q1/VMware-Horizon-Client-%{ver}-%{rel}.x64.bundle
Source1: https://pubs.vmware.com/Release_Notes/en/horizon-client/horizon-client-linux-44-release-notes.html
Source2: https://www.vmware.com/pdf/horizon-view/horizon-client-linux-44-document.pdf
Source10: usbarb.rules
Source11: vmware-usbarbitrator.service
Source12: vmware-view-usbd.service
Patch0: %{name}-desktop.patch
License: VMware
ExclusiveArch: x86_64
BuildRequires: chrpath
BuildRequires: desktop-file-utils
BuildRequires: execstack
BuildRequires: systemd
Provides: bundled(mechanical-fonts) = 1.00
Provides: bundled(c-ares) = 1.12.0
Provides: bundled(curl) = 7.52.1
Provides: bundled(icu) = 58.1
Provides: bundled(libpng12) = 1.2.57
Provides: bundled(openssl) = 1.0.2k
Provides: bundled(opus) = 1.1.4
Provides: bundled(zlib) = 1.2.3
Provides: bundled(atk) = 1.9.0

%global __provides_exclude ^lib\(tsmmrClient\|mksvchanclient\|pcoip_client\|rdeSvc\|rdpvcbridge\|scredirvchanclient\|tsdrClient\|udpProxyLib\|vdpservice\|viewMMDevRedir\|viewMPClient\)\\.so.*\|lib\(crypto\|ssl\)\\.so\\.1\\.0\\.2.*$
%global __requires_exclude ^lib\(crypto\|ssl\)\\.so\\.1\\.0\\.2.*$

%description
Remote access client for VMware Horizon.

%package mmr
Summary: Multimedia Redirection support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}

%description mmr
Multimedia Redirection support plugin for VMware Horizon Client.

%package pcoip
Summary: PCoIP support plugin for VMware Horizon Client
Requires: freerdp1.2
Requires: %{name} = %{version}-%{release}
Provides: bundled(pcoip-soft-clients) = 3.45

%description pcoip
PCoIP support plugin for VMware Horizon Client.

%package rtav
Summary: Real-Time Audio-Video support plugin for VMware Horizon Client
Requires: %{name}-pcoip = %{version}-%{release}

%description rtav
Real-Time Audio-Video support plugin for VMware Horizon Client.

%package smartcard
Summary: SmartCard authentication support plugin for VMware Horizon Client
Requires: %{name}-pcoip = %{version}-%{release}

%description smartcard
SmartCard authentication support plugin for VMware Horizon Client.

%package tsdr
Summary: Client Drive Redirection support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}

%description tsdr
Client Drive Redirection support plugin for VMware Horizon Client.

%package usb
Summary: USB Redirection support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}

%description usb
USB Redirection support plugin for VMware Horizon Client.

%package virtual-printing
Summary: Virtual Printing support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}
Provides: bundled(thinprint) = 10.0.141

%description virtual-printing
Virtual Printing support plugin for VMware Horizon Client.

%prep
%setup -qcT
rmdir %{_builddir}/%{name}-%{version}
bash %{S:0} -x %{_builddir}/%{name}-%{version}
cd %{_builddir}/%{name}-%{version}
cp -p %{S:1} %{S:2} ./
%patch0 -p1
chrpath -d vmware-horizon-mmr/lib/vmware/view/vdpService/libtsmmrClient.so
chrpath -d vmware-horizon-pcoip/pcoip/bin/vmware-flash-projector
execstack -c vmware-horizon-mmr/lib/vmware/view/vdpService/libtsmmrClient.so
execstack -c vmware-horizon-pcoip/pcoip/lib/pcoip/vchan_plugins/libvdpservice.so
execstack -c vmware-horizon-pcoip/pcoip/lib/pcoip/vchan_plugins/libmksvchanclient.so
execstack -c vmware-horizon-pcoip/pcoip/lib/vmware/libudpProxyLib.so
execstack -c vmware-horizon-pcoip/pcoip/lib/vmware/view/vdpService/librdeSvc.so
execstack -c vmware-horizon-pcoip/pcoip/lib/vmware/view/vdpService/libviewMPClient.so
execstack -c vmware-horizon-rtav/lib/pcoip/vchan_plugins/libviewMMDevRedir.so
execstack -c vmware-horizon-tsdr/lib/vmware/view/vdpService/libtsdrClient.so

%build

%install
#cd %{_builddir}/%{name}-%{version}
install -dm0755 %{buildroot}%{_sysconfdir}/vmware{/vdp/host_overlay_plugins,-vix}
install -dm0755 %{buildroot}%{_bindir}
install -dm0755 %{buildroot}%{_unitdir}
install -dm0755 %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins
install -dm0755 %{buildroot}%{_prefix}/lib/freerdp
install -dm0755 %{buildroot}%{_prefix}/lib/vmware/rdpvcbridge
install -dm0755 %{buildroot}%{_prefix}/lib/vmware/view/{bin,usb,virtualPrinting,vdpService}
install -dm0755 %{buildroot}%{_prefix}/lib/vmware/xkeymap
install -dm0755 %{buildroot}%{_datadir}/applications
install -dm0755 %{buildroot}%{_datadir}/icons
install -dm0755 %{buildroot}%{_datadir}/pixmaps
install -dm0755 %{buildroot}%{_var}/log/vmware

echo 'BINDIR="%{_bindir}"' > %{buildroot}%{_sysconfdir}/vmware/bootstrap
echo 'BINDIR="%{_bindir}"' > %{buildroot}%{_sysconfdir}/vmware-vix/bootstrap

install -pm0755 vmware-horizon-client/bin/vmware-view{,-lib-scan,-log-collector} %{buildroot}%{_bindir}
cp -pr vmware-horizon-client/share/* %{buildroot}%{_datadir}
desktop-file-validate %{buildroot}%{_datadir}/applications/vmware-view.desktop
install -pm0755 vmware-horizon-client/lib/vmware/view/bin/vmware-view %{buildroot}%{_prefix}/lib/vmware/view/bin

echo "%{_prefix}/lib/pcoip/vchan_plugins/libvdpservice.so" > %{buildroot}%{_sysconfdir}/vmware/vdp/host_overlay_plugins/config
install -pm0755 vmware-horizon-mmr/lib/vmware/view/vdpService/libtsmmrClient.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService

install -pm0755 vmware-horizon-pcoip/pcoip/bin/vmware-flash-projector %{buildroot}%{_bindir}
install -pm0755 vmware-horizon-pcoip/pcoip/bin/vmware-remotemks{,-container} %{buildroot}%{_bindir}
install -pm0755 vmware-horizon-pcoip/pcoip/lib/libpcoip_client.so %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/pcoip/vchan_plugins/lib*.so %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins
cp -pr vmware-horizon-pcoip/pcoip/lib/vmware/{rdpvcbridge,xkeymap} %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/view/vdpService/lib*.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService
install -pm0755 vmware-horizon-pcoip/pcoip/lib/pcoip/vchan_plugins/libmksvchanclient.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/lib{crypto,ssl}.so.1.0.2 %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/libudpProxyLib.so %{buildroot}%{_prefix}/lib/vmware

install -pm0755 vmware-horizon-rtav/lib/pcoip/vchan_plugins/libviewMMDevRedir.so %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins

install -pm0755 vmware-horizon-smartcard/lib/pcoip/vchan_plugins/libscredirvchanclient.so %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins

install -pm0755 vmware-horizon-tsdr/lib/vmware/view/vdpService/libtsdrClient.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService

install -pm0755 vmware-horizon-usb/bin/vmware-{usbarbitrator,view-usbd} %{buildroot}%{_prefix}/lib/vmware/view/usb
ln -s %{_prefix}/lib/vmware/usb/vmware-usbarbitrator %{buildroot}%{_bindir}
ln -s %{_prefix}/lib/vmware/usb/vmware-view-usbd %{buildroot}%{_bindir}
install -pm0644 %{S:10} %{buildroot}%{_sysconfdir}/vmware
install -pm0644 %{S:11} %{S:12} %{buildroot}%{_unitdir}

#install -pm0755 vmware-horizon-virtual-printing/

%find_lang vmware-view

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{_builddir}/%{name}-%{version}/vmware-view.lang
%license vmware-horizon-client/doc/open_source_licenses.txt
%license %lang(de) vmware-horizon-client/doc/VMware-Horizon-Client-EULA-de.txt
%license vmware-horizon-client/doc/VMware-Horizon-Client-EULA-en.txt
%license %lang(es) vmware-horizon-client/doc/VMware-Horizon-Client-EULA-es.txt
%license %lang(fr) vmware-horizon-client/doc/VMware-Horizon-Client-EULA-fr.txt
%license %lang(ja) vmware-horizon-client/doc/VMware-Horizon-Client-EULA-ja.txt
%license %lang(ko) vmware-horizon-client/doc/VMware-Horizon-Client-EULA-ko.txt
%license %lang(zh_CN) vmware-horizon-client/doc/VMware-Horizon-Client-EULA-zh_CN.txt
%license %lang(zh_TW) vmware-horizon-client/doc/VMware-Horizon-Client-EULA-zh_TW.txt
%doc horizon-client-linux-44-release-notes.html horizon-client-linux-44-document.pdf
%dir %{_sysconfdir}/vmware
%config %{_sysconfdir}/vmware/bootstrap
%dir %{_sysconfdir}/vmware/vdp
%dir %{_sysconfdir}/vmware-vix
%config %{_sysconfdir}/vmware-vix/bootstrap
%{_bindir}/vmware-view
%{_bindir}/vmware-view-lib-scan
%{_bindir}/vmware-view-log-collector
%dir %{_prefix}/lib/vmware
%{_prefix}/lib/vmware/libcrypto.so.1.0.2
%{_prefix}/lib/vmware/libssl.so.1.0.2
%{_prefix}/lib/vmware/libudpProxyLib.so
%dir %{_prefix}/lib/vmware/rdpvcbridge
%dir %{_prefix}/lib/vmware/view
%dir %{_prefix}/lib/vmware/view/bin
%{_prefix}/lib/vmware/view/bin/vmware-view
%dir %{_prefix}/lib/vmware/view/vdpService
%{_datadir}/applications/vmware-view.desktop
%{_datadir}/icons/vmware-view.png
%{_datadir}/pixmaps/vmware-view.png
%{_var}/log/vmware

%files mmr
%dir %{_sysconfdir}/vmware/vdp/host_overlay_plugins
%config(noreplace) %{_sysconfdir}/vmware/vdp/host_overlay_plugins/config
%{_prefix}/lib/vmware/view/vdpService/libtsmmrClient.so

%files pcoip
%{_bindir}/vmware-flash-projector
%{_bindir}/vmware-remotemks
%{_bindir}/vmware-remotemks-container
%dir %{_prefix}/lib/pcoip
%dir %{_prefix}/lib/pcoip/vchan_plugins
%{_prefix}/lib/pcoip/vchan_plugins/libmksvchanclient.so
%{_prefix}/lib/pcoip/vchan_plugins/librdpvcbridge.so
%{_prefix}/lib/pcoip/vchan_plugins/libvdpservice.so
%{_prefix}/lib/vmware/libpcoip_client.so
%{_prefix}/lib/vmware/rdpvcbridge/freerdp_plugins.conf
%{_prefix}/lib/vmware/view/vdpService/libmksvchanclient.so
%{_prefix}/lib/vmware/view/vdpService/librdeSvc.so
%{_prefix}/lib/vmware/view/vdpService/libviewMPClient.so
%{_prefix}/lib/vmware/xkeymap

%files rtav
%{_prefix}/lib/pcoip/vchan_plugins/libviewMMDevRedir.so

%files smartcard
%{_prefix}/lib/pcoip/vchan_plugins/libscredirvchanclient.so

%files tsdr
%{_prefix}/lib/vmware/view/vdpService/libtsdrClient.so

%files usb
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/vmware/usbarb.rules
%{_unitdir}/vmware-usbarbitrator.service
%{_unitdir}/vmware-view-usbd.service
%{_bindir}/vmware-usbarbitrator
%{_bindir}/vmware-view-usbd
%dir %{_prefix}/lib/vmware/view/usb
%{_prefix}/lib/vmware/view/usb/vmware-usbarbitrator
%{_prefix}/lib/vmware/view/usb/vmware-view-usbd

%if 0
%files virtual-printing
%{_prefix}/lib/freerdp/tprdp-client.so
%{_prefix}/lib/vmware/rdpvcbridge/tprdp.so
%{_prefix}/lib/vmware/view/virtualPrinting
%{_prefix}/lib/vmware/view/virtualPrinting/conf
%{_prefix}/lib/vmware/view/virtualPrinting/conf/thnuclnt.convs
%{_prefix}/lib/vmware/view/virtualPrinting/conf/thnuclnt.types
%{_prefix}/lib/vmware/view/virtualPrinting/init.d
%{_prefix}/lib/vmware/view/virtualPrinting/init.d/linux
%{_prefix}/lib/vmware/view/virtualPrinting/init.d/linux/thnuclnt
%{_prefix}/lib/vmware/view/virtualPrinting/NameTranslationEx2.reg
%{_prefix}/lib/vmware/view/virtualPrinting/README
%{_prefix}/lib/vmware/view/virtualPrinting/rev.rc
%{_prefix}/lib/vmware/view/virtualPrinting/setup.sh
%{_prefix}/lib/vmware/view/virtualPrinting/thnuSetup_VMW_VHV_Mac.sh
%{_prefix}/lib/vmware/view/virtualPrinting/uninstall.sh
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-NOSSL
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-NOSSL/build.spec
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-NOSSL/thnuchk
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-NOSSL/thnuclnt
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-NOSSL/thnuclntd
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-NOSSL/thnuconf
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-NOSSL/thnucups
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-NOSSL/.thnumod
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-NOSSL/thnurdp
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-vmAppLd
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-vmAppLd/build.spec
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-vmAppLd/thnuchk.so
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-vmAppLd/thnuclntd.so
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-vmAppLd/thnuclnt.so
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-vmAppLd/thnuconf.so
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-vmAppLd/thnucups.so
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-vmAppLd/.thnumod.so
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-vmAppLd/thnurdp.so
%{_prefix}/lib/vmware/view/virtualPrinting/x86_64-linux-vmAppLd/vmappld
%endif

%changelog
* Tue Mar 28 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.4.0.5167967-1
- initial build
