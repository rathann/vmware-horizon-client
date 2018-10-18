%undefine _missing_build_ids_terminate_build
%if 0%{?fedora}
%undefine _debugsource_packages
%undefine _unique_build_ids
%global _no_recompute_build_ids 1
%endif
%global cart   CART19FQ3
%global ver    4.9.0
%global docv   %(n=%{ver}; echo ${n%.0})
%global docvnd %(n=%{docv}; echo ${n/.})
%global rel    9507999

Summary: Remote access client for VMware Horizon
Name: vmware-horizon-client
Version: %{ver}.%{rel}
Release: 2
URL: https://www.vmware.com/products/horizon.html
# https://my.vmware.com/en/web/vmware/info/slug/desktop_end_user_computing/vmware_horizon_clients/4_0
Source0: https://download3.vmware.com/software/view/viewclients/%{cart}/VMware-Horizon-Client-%{ver}-%{rel}.x64.bundle
Source1: https://docs.vmware.com/en/VMware-Horizon-Client-for-Linux/%{docv}/rn/horizon-client-linux-%{docvnd}-release-notes.html
Source2: https://docs.vmware.com/en/VMware-Horizon-Client-for-Linux/%{docv}/horizon-client-linux-installation.pdf
Source10: usbarb.rules
Source11: vmware-usbarbitrator.service
Source12: vmware-ftsprhvd.service
Patch0: %{name}-desktop.patch
License: VMware
ExclusiveArch: x86_64
BuildRequires: chrpath
BuildRequires: desktop-file-utils
BuildRequires: execstack
BuildRequires: systemd
Provides: bundled(atk) = 1.9.0
Provides: bundled(atk) = 1.30.0
Provides: bundled(boost) = 1.61
Provides: bundled(bzip2) = 1.0.6
Provides: bundled(c-ares) = 1.13.0
Provides: bundled(curl) = 7.56.0
Provides: bundled(glibmm) = 2.44.0
Provides: bundled(gtkmm) = 2.20.1
Provides: bundled(hal) = 0.5.12
Provides: bundled(hidapi) = 0.8.9
Provides: bundled(icu) = 56.1
Provides: bundled(icu) = 60.1
Provides: bundled(json-c) = 0.12.1
Provides: bundled(libjpeg-turbo) = 1.4.2
Provides: bundled(libpng12) = 1.2.57
Provides: bundled(libsrtp) = 2.1.0.0-pre
Provides: bundled(libwebrtc) = 90
Provides: bundled(libxml2) = 2.9.6
Provides: bundled(mechanical-fonts) = 1.00
Provides: bundled(openssl) = 1.0.2m
Provides: bundled(opus) = 1.0.1
Provides: bundled(opus) = 1.1.4.60
Provides: bundled(speex) = 1.2rc3
Provides: bundled(zlib) = 1.2.3
Provides: bundled(zlib) = 1.2.8
Provides: bundled(atk) = 1.30.0
Requires: libudev.so.1()(64bit)

%global __provides_exclude_from ^%{_prefix}/lib/(vmware|pcoip)/.*$
%global __requires_exclude ^lib\(crtbora\\.so\|\(crypto\|ssl\)\\.so\\.1\\.0\\.2\|ffi\\.so\\.5\|udev\\.so\\.0\|vmware\(base\|-view-usbd\)\\.so).*$

%description
Remote access client for VMware Horizon.

%package media-provider
Summary: Virtualization Pack for Skype for Business
Requires: %{name} = %{version}-%{release}

%description media-provider
Virtualization Pack for Skype for Business.

%package mmr
Summary: Multimedia Redirection support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}

%description mmr
Multimedia Redirection support plugin for VMware Horizon Client.

%package pcoip
Summary: PCoIP support plugin for VMware Horizon Client
Requires: freerdp1.2
Requires: libffi.so.6()(64bit)
Requires: %{name} = %{version}-%{release}
Provides: bundled(pcoip-soft-clients) = 3.51

%description pcoip
PCoIP support plugin for VMware Horizon Client.

%package rtav
Summary: Real-Time Audio-Video support plugin for VMware Horizon Client
Requires: %{name}-pcoip = %{version}-%{release}

%description rtav
Real-Time Audio-Video support plugin for VMware Horizon Client.

%package serialportclient
Summary: Serial port redirection support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}
Requires: libudev.so.1()(64bit)

%description serialportclient
Serial port redirection support plugin for VMware Horizon Client.

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
BuildRequires: systemd
%{?systemd_requires}
Requires: %{name} = %{version}-%{release}
Requires(post): %{_sbindir}/semodule
Requires(postun): %{_sbindir}/semodule

%description usb
USB Redirection support plugin for VMware Horizon Client.

%package virtual-printing
Summary: Virtual Printing support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}
Provides: bundled(thinprint) = 10.0.155

%description virtual-printing
Virtual Printing support plugin for VMware Horizon Client.

%prep
rm -rf %{_builddir}/%{name}-%{version}
bash %{S:0} -x %{_builddir}/%{name}-%{version}
%setup -qDT
cp -p %{S:1} %{S:2} ./
%patch0 -p1
chrpath -d vmware-horizon-pcoip/pcoip/lib/vmware/libcairomm-1.0.so.1
chrpath -d vmware-horizon-pcoip/pcoip/lib/vmware/libgiomm-2.4.so.1
chrpath -d vmware-horizon-pcoip/pcoip/lib/vmware/libglibmm-2.4.so.1
chrpath -d vmware-horizon-pcoip/pcoip/lib/vmware/libgtkmm-2.4.so.1
execstack -c vmware-horizon-media-provider/lib/libV264.so
execstack -c vmware-horizon-media-provider/lib/libVMWMediaProvider.so
execstack -c vmware-horizon-pcoip/pcoip/lib/libcoreavc_sdk.so

%build

%install
install -dm0755 %{buildroot}%{_sysconfdir}/vmware{/vdp/host_overlay_plugins,-vix}
install -dm0755 %{buildroot}%{_bindir}
install -dm0755 %{buildroot}%{_unitdir}
install -dm0755 %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins
install -dm0755 %{buildroot}%{_prefix}/lib/freerdp
install -dm0755 %{buildroot}%{_prefix}/lib/vmware/mediaprovider
install -dm0755 %{buildroot}%{_prefix}/lib/vmware/rdpvcbridge
install -dm0755 %{buildroot}%{_prefix}/lib/vmware/view/{bin,usb,pkcs11,virtualPrinting,vdpService}
install -dm0755 %{buildroot}%{_prefix}/lib/vmware/xkeymap
install -dm0755 %{buildroot}%{_datadir}/applications
install -dm0755 %{buildroot}%{_datadir}/icons
install -dm0755 %{buildroot}%{_datadir}/pixmaps
install -dm0755 %{buildroot}%{_var}/log/vmware

echo 'BINDIR="%{_bindir}"' > %{buildroot}%{_sysconfdir}/vmware/bootstrap
echo 'BINDIR="%{_bindir}"' > %{buildroot}%{_sysconfdir}/vmware-vix/bootstrap

install -pm0755 vmware-horizon-client/bin/vmware-view{,-lib-scan,-log-collector,-usbdloader} %{buildroot}%{_bindir}
cp -pr vmware-horizon-client/share/* %{buildroot}%{_datadir}
install -pm0644 vmware-horizon-client/extras/artwork/linux_view_128x.png %{buildroot}%{_datadir}/icons/vmware-view.png
install -pm0644 vmware-horizon-client/extras/artwork/linux_view_128x.png %{buildroot}%{_datadir}/pixmaps/vmware-view.png
desktop-file-validate %{buildroot}%{_datadir}/applications/vmware-view.desktop
install -pm0755 vmware-horizon-client/lib/vmware/view/bin/vmware-view %{buildroot}%{_prefix}/lib/vmware/view/bin
ln -s %{_libdir}/libudev.so.1 %{buildroot}%{_prefix}/lib/vmware/libudev.so.0
ln -s %{_libdir}/libffi.so.6 %{buildroot}%{_prefix}/lib/vmware/libffi.so.5

install -pm0755 vmware-horizon-media-provider/lib/libV264.so %{buildroot}%{_prefix}/lib/vmware/mediaprovider
install -pm0755 vmware-horizon-media-provider/lib/libVMWMediaProvider.so %{buildroot}%{_prefix}/lib/vmware/mediaprovider

echo "%{_prefix}/lib/pcoip/vchan_plugins/libvdpservice.so" > %{buildroot}%{_sysconfdir}/vmware/vdp/host_overlay_plugins/config
install -pm0755 vmware-horizon-mmr/lib/vmware/view/vdpService/libtsmmrClient.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService

install -pm0755 vmware-horizon-pcoip/pcoip/bin/vmware-flash-projector %{buildroot}%{_bindir}
install -pm0755 vmware-horizon-pcoip/pcoip/bin/vmware-remotemks{,-container} %{buildroot}%{_bindir}
install -pm0755 vmware-horizon-pcoip/pcoip/lib/libcoreavc_sdk.so %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/libpcoip_client.so %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/pcoip/vchan_plugins/lib*.so %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins
ln %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins/libmksvchanclient.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService/libmksvchanclient.so
cp -pr vmware-horizon-pcoip/pcoip/lib/vmware/{rdpvcbridge,xkeymap} %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/view/vdpService/lib*.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService

install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/lib{crypto,ssl}.so.1.0.2 %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/libudpProxyLib.so %{buildroot}%{_prefix}/lib/vmware

install -pm0755 vmware-horizon-rtav/lib/pcoip/vchan_plugins/libviewMMDevRedir.so %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins

install -pm0755 vmware-horizon-seamless-window/vmware-view-crtbora %{buildroot}%{_prefix}/lib/vmware/view/bin
install -pm0755 vmware-horizon-seamless-window/lib/vmware/libcrtbora.so %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-seamless-window/lib/vmware/libvmwarebase.so %{buildroot}%{_prefix}/lib/vmware

install -pm0755 vmware-horizon-serialportclient/bin/ftsprhvd %{buildroot}%{_prefix}/lib/vmware/view/bin
install -pm0755 vmware-horizon-serialportclient/lib/vmware/rdpvcbridge/ftnlses3hv.so %{buildroot}%{_prefix}/lib/vmware/rdpvcbridge
install -pm0644 %{S:12} %{buildroot}%{_unitdir}

install -pm0755 vmware-horizon-smartcard/lib/pcoip/vchan_plugins/libscredirvchanclient.so %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins

install -pm0755 vmware-horizon-tsdr/lib/vmware/view/vdpService/libtsdrClient.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService

install -pm0755 vmware-horizon-usb/bin/{vmware-usbarbitrator,libvmware-view-usbd.so} %{buildroot}%{_prefix}/lib/vmware/view/usb
install -pm0755 vmware-horizon-usb/lib/vmware/view/vdpService/libusbRedirectionClient.so  %{buildroot}%{_prefix}/lib/vmware/view/vdpService

ln -s %{_prefix}/lib/vmware/view/usb/vmware-usbarbitrator %{buildroot}%{_bindir}
install -pm0644 %{S:10} %{buildroot}%{_sysconfdir}/vmware
install -pm0644 %{S:11} %{buildroot}%{_unitdir}

#install -pm0755 vmware-horizon-virtual-printing/

%find_lang vmware-view

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post serialportclient
%systemd_post vmware-ftsprhvd.service
exit 0

%preun serialportclient
%systemd_preun vmware-ftsprhvd.service

%postun serialportclient
%systemd_postun_with_restart vmware-ftsprhvd.service

%post usb
TMPDIR=$(%{_bindir}/mktemp -d)
cat >> $TMPDIR/%{name}-usb-rpm.cil << __EOF__
(typeattributeset cil_gen_require init_t)
(typeattributeset cil_gen_require var_log_t)
(typeattributeset cil_gen_require vmware_log_t)
(typeattributeset cil_gen_require vmware_sys_conf_t)
(allow init_t var_log_t (file (create unlink)))
(allow init_t vmware_log_t (file (getattr unlink)))
(allow init_t vmware_sys_conf_t (dir (add_name remove_name write)))
(allow init_t vmware_sys_conf_t (file (create rename setattr unlink write)))
__EOF__
%{_sbindir}/semodule -i $TMPDIR/%{name}-usb-rpm.cil
rm $TMPDIR/%{name}-usb-rpm.cil
rmdir $TMPDIR
%systemd_post vmware-usbarbitrator.service
exit 0

%preun usb
%systemd_preun vmware-usbarbitrator.service

%postun usb
%systemd_postun_with_restart vmware-usbarbitrator.service
if [ $1 -eq 0 ]; then
  %{_sbindir}/semodule -r %{name}-usb-rpm || :
fi

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
%doc horizon-client-linux-%{docvnd}-release-notes.html
%doc horizon-client-linux-installation.pdf
%dir %{_sysconfdir}/vmware
%config %{_sysconfdir}/vmware/bootstrap
%dir %{_sysconfdir}/vmware/vdp
%dir %{_sysconfdir}/vmware-vix
%config %{_sysconfdir}/vmware-vix/bootstrap
%{_bindir}/vmware-view
%{_bindir}/vmware-view-lib-scan
%{_bindir}/vmware-view-log-collector
%{_bindir}/vmware-view-usbdloader
%dir %{_prefix}/lib/vmware
%{_prefix}/lib/vmware/libcrtbora.so
%{_prefix}/lib/vmware/libcrypto.so.1.0.2
%{_prefix}/lib/vmware/libssl.so.1.0.2
%{_prefix}/lib/vmware/libudev.so.0
%{_prefix}/lib/vmware/libudpProxyLib.so
%{_prefix}/lib/vmware/libvmwarebase.so
%dir %{_prefix}/lib/vmware/rdpvcbridge
%dir %{_prefix}/lib/vmware/view
%dir %{_prefix}/lib/vmware/view/bin
%{_prefix}/lib/vmware/view/bin/vmware-view
%{_prefix}/lib/vmware/view/bin/vmware-view-crtbora
%dir %{_prefix}/lib/vmware/view/pkcs11
%dir %{_prefix}/lib/vmware/view/vdpService
%{_datadir}/applications/vmware-view.desktop
%{_datadir}/icons/vmware-view.png
%{_datadir}/pixmaps/vmware-view.png
%{_datadir}/X11/xorg.conf.d/20-vmware-hid.conf
%{_var}/log/vmware

%files media-provider
%dir %{_prefix}/lib/vmware/mediaprovider
%{_prefix}/lib/vmware/mediaprovider/libV264.so
%{_prefix}/lib/vmware/mediaprovider/libVMWMediaProvider.so

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
%{_prefix}/lib/vmware/libcoreavc_sdk.so
%{_prefix}/lib/vmware/libffi.so.5
%{_prefix}/lib/vmware/libpcoip_client.so
%{_prefix}/lib/vmware/rdpvcbridge/freerdp_plugins.conf
%{_prefix}/lib/vmware/view/vdpService/libmksvchanclient.so
%{_prefix}/lib/vmware/view/vdpService/librdeSvc.so
%{_prefix}/lib/vmware/view/vdpService/libviewMPClient.so
%{_prefix}/lib/vmware/xkeymap

%files rtav
%{_prefix}/lib/pcoip/vchan_plugins/libviewMMDevRedir.so

%files serialportclient
%attr(0644,root,root) %config(noreplace) %ghost %{_sysconfdir}/ftsprhv.db
%{_prefix}/lib/vmware/view/bin/ftsprhvd
%{_prefix}/lib/vmware/rdpvcbridge/ftnlses3hv.so
%{_unitdir}/vmware-ftsprhvd.service

%files smartcard
%{_prefix}/lib/pcoip/vchan_plugins/libscredirvchanclient.so

%files tsdr
%{_prefix}/lib/vmware/view/vdpService/libtsdrClient.so

%files usb
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/vmware/usbarb.rules
%{_unitdir}/vmware-usbarbitrator.service
%{_bindir}/vmware-usbarbitrator
%dir %{_prefix}/lib/vmware/view/usb
%{_prefix}/lib/vmware/view/usb/vmware-usbarbitrator
%{_prefix}/lib/vmware/view/usb/libvmware-view-usbd.so
%{_prefix}/lib/vmware/view/vdpService/libusbRedirectionClient.so

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
* Tue Oct 16 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.9.0.9507999-2
- add missing libcoreavc_sdk.so library in pcoip subpackage
- simplify Provides: filtering
- fix unowned dir /usr/lib/vmware/mediaprovider
- use chrpath and execstack only files which need it

* Mon Oct 01 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.9.0.9507999-1
- update to 4.9.0 build 9507999
- include Serial Port Redirection feature

* Fri Jul 13 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.8.0.8518891-1
- update to 4.8.0 build 8518891

* Thu Feb 08 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.7.0.7395152-1
- update to 4.7.0 build 7395152
- include Seamless Window Feature in the main package
- update bundled components list
- add SELinux policy for usbarbitrator

* Thu Nov 23 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.6.0.6617224-1
- update to 4.6.0 build 6617224
- update bundled components list
- install 128px icon
- add media-provider subpackage (Virtualization Pack for Skype for Business)
- include /usr/lib/vmware/view/pkcs11 empty dir to silence error messages
- drop and work around libudev.so.0 and libffi.so.5 dependencies

* Thu Jul 27 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.5.0.5650368-1
- update to 4.5.0 build 5650368
- update source URL and bundled components
- work around debugedit bug

* Tue Mar 28 2017 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.4.0.5167967-1
- initial build
