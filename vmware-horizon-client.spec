%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages
%undefine _unique_build_ids
%global _no_recompute_build_ids 1
%global cart   CART20FQ4
%global ver    5.3.0
%global docv   %(n=%{ver}; echo ${n%.0})
%global docvnd %(n=%{docv}; echo ${n/.})
%global rel    15208949

Summary: Remote access client for VMware Horizon
Name: vmware-horizon-client
Version: %{ver}.%{rel}
Release: 1
URL: https://www.vmware.com/products/horizon.html
# https://my.vmware.com/web/vmware/info?slug=desktop_end_user_computing/vmware_horizon_clients/5_0
Source0: https://download3.vmware.com/software/view/viewclients/%{cart}/VMware-Horizon-Client-%{ver}-%{rel}.x64.bundle
Source1: https://docs.vmware.com/en/VMware-Horizon-Client-for-Linux/%{docv}/rn/horizon-client-linux-%{docvnd}-release-notes.html
Source2: https://docs.vmware.com/en/VMware-Horizon-Client-for-Linux/%{docv}/horizon-client-linux-installation.pdf
Source10: usbarb.rules
Source11: vmware-usbarbitrator.service
Source12: vmware-ftsprhvd.service
Source13: vmware-ftscanhvd.service
Patch0: %{name}-desktop.patch
License: VMware
ExclusiveArch: x86_64
BuildRequires: chrpath
BuildRequires: desktop-file-utils
BuildRequires: %{_bindir}/execstack
BuildRequires: %{_bindir}/python
BuildRequires: systemd
Provides: bundled(atk) = 2.28.1
Provides: bundled(atkmm) = 2.22.7
Provides: bundled(boost) = 1.67
Provides: bundled(bzip2) = 1.0.6
Provides: bundled(c-ares) = 1.13.0
Provides: bundled(curl) = 7.66.0
Provides: bundled(glibmm24) = 2.44.0
Provides: bundled(gtkmm30) = 3.10.1
Provides: bundled(hal) = 0.5.12
Provides: bundled(icu) = 60.2
Provides: bundled(libjpeg-turbo) = 1.4.2
Provides: bundled(libpng12) = 1.2.59
Provides: bundled(libwebrtc) = 90
Provides: bundled(libxml2) = 2.9.9
Provides: bundled(mechanical-fonts) = 1.00
Provides: bundled(openssl) = 1.0.2t
Provides: bundled(opus) = 1.1.4.60
Provides: bundled(pangomm) = 2.34.0
Provides: bundled(speex) = 1.2rc3
Provides: bundled(zlib) = 1.2.11
Provides: %{name}-seamless-window = %{version}-%{release}
Obsoletes: %{name}-seamless-window < 5.2.0.14604769
Requires: %{_bindir}/pidof
Requires: libudev.so.1()(64bit)

%global __provides_exclude_from ^%{_prefix}/lib/(vmware|pcoip)/.*$
%global __requires_exclude ^lib\(atkmm-1\\.6\\.so\\.1\|g\(io\|lib\)mm-2\\.4\\.so\\.1\|g\(dk\|tk\)mm-3\\.0\\.so\\.1\|pangomm-1\\.4\\.so\\.1\|\(crypto\|ssl\)\\.so\\.1\\.0\\.2\|udev\\.so\\.0\|\(cef\|crtbora\|GLESv2\|json_linux-gcc-4.1.1_libmt\|vmware\(base\|-view-usbd\)\)\\.so).*$

%description
Remote access client for VMware Horizon.

Requires Horizon Agent 7.0 or later on the virtual desktop.

%package html5mmr
Summary: HTML5 Multimedia Redirection support plugin for VMware Horizon Client
Provides: bundled(chromium-embedded-framework) = 70.0.3538.35
Provides: bundled(webrtc) = 90
Requires: %{name} = %{version}-%{release}

%description html5mmr
HTML5 Multimedia Redirection support plugin for VMware Horizon Client.

Requires Horizon Agent 7.9 or later on the virtual desktop.

%package integrated-printing
Summary: Integrated Printing support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}

%description integrated-printing
Integrated Printing support plugin for VMware Horizon Client.

%package media-provider
Summary: Virtualization Pack for Skype for Business
Requires: %{name} = %{version}-%{release}
Provides: bundled(hidapi) = 0.8.9
Provides: bundled(json-c) = 0.12.1
Provides: bundled(libsrtp) = 2.1.0.0-pre
Provides: bundled(webrtc) = 90

%description media-provider
Virtualization Pack for Skype for Business.

%package mmr
Summary: Multimedia Redirection support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}

%description mmr
Multimedia Redirection support plugin for VMware Horizon Client.

Requires Horizon Agent 7.0 or later on the virtual desktop.

%package pcoip
Summary: PCoIP support plugin for VMware Horizon Client
Requires: freerdp1.2
Requires: libavcodec.so.58()(64bit)
Requires: libavutil.so.56()(64bit)
Requires: %{name} = %{version}-%{release}
Provides: bundled(pcoip-soft-clients) = 3.65
Provides: bundled(openssl) = 1.0.2t

%description pcoip
PCoIP support plugin for VMware Horizon Client.

Requires Horizon Agent 7.0.2 or later on the virtual desktop.

%package rtav
Summary: Real-Time Audio-Video support plugin for VMware Horizon Client
Requires: %{name}-pcoip = %{version}-%{release}

%description rtav
Real-Time Audio-Video support plugin for VMware Horizon Client.

%package scannerclient
Summary: Scanner redirection support plugin for VMware Horizon Client
Provides: bundled(scanner_linux) = 2.3.1.3
%{?systemd_requires}
Requires: %{name} = %{version}-%{release}
Requires: libudev.so.1()(64bit)
Requires(post): %{_sbindir}/semodule
Requires(postun): %{_sbindir}/semodule

%description scannerclient
The Scanner Redirection component allows you to use local scanner devices from a
remote desktop.

Requires Horizon Agent 7.8 or later on the virtual desktop.

%package serialportclient
Summary: Serial port redirection support plugin for VMware Horizon Client
Provides: bundled(serial_linux) = 2.2.1
Requires: %{name} = %{version}-%{release}
Requires: libudev.so.1()(64bit)

%description serialportclient
Serial port redirection support plugin for VMware Horizon Client.

Requires Horizon Agent 7.6 or later on the virtual desktop.

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
Provides: bundled(thinprint) = 10.0.165-HF001

%description virtual-printing
Virtual Printing support plugin for VMware Horizon Client.

%prep
rm -rf %{_builddir}/%{name}-%{version}
bash %{S:0} -x %{_builddir}/%{name}-%{version}
%setup -qDT
cp -p %{S:1} %{S:2} ./
%patch0 -p1
chrpath -d vmware-horizon-scannerclient/bin/ftscanhvd
execstack -c vmware-horizon-media-provider/lib/libV264.so
execstack -c vmware-horizon-media-provider/lib/libVMWMediaProvider.so
execstack -c vmware-horizon-pcoip/pcoip/lib/libcoreavc_sdk.so
pushd vmware-horizon-html5mmr/lib/vmware/view/html5mmr
chmod +x \
  HTML5VideoPlayer \
  chrome-sandbox \
  {,swiftshader/}lib*.so \

popd

%build

%install
install -dm0755 %{buildroot}%{_sysconfdir}/teradici
install -dm0755 %{buildroot}%{_sysconfdir}/vmware{/udpProxy,/vdp/host_overlay_plugins,-vix}
install -dm0755 %{buildroot}%{_bindir}
install -dm0755 %{buildroot}%{_unitdir}
install -dm0755 %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins
install -dm0755 %{buildroot}%{_prefix}/lib/freerdp
install -dm0755 %{buildroot}%{_prefix}/lib/vmware/mediaprovider
install -dm0755 %{buildroot}%{_prefix}/lib/vmware/rdpvcbridge
install -dm0755 %{buildroot}%{_prefix}/lib/vmware/view/{bin,client,usb,pkcs11,{integrated,virtual}Printing,vdpService}
install -dm0755 %{buildroot}%{_prefix}/lib/vmware/xkeymap
install -dm0755 %{buildroot}%{_datadir}/applications
install -dm0755 %{buildroot}%{_datadir}/doc/%{name}
install -dm0755 %{buildroot}%{_datadir}/icons
install -dm0755 %{buildroot}%{_datadir}/pixmaps
install -dm0755 %{buildroot}%{_var}/log/vmware

echo 'BINDIR="%{_bindir}"' > %{buildroot}%{_sysconfdir}/vmware/bootstrap
echo 'BINDIR="%{_bindir}"' > %{buildroot}%{_sysconfdir}/vmware-vix/bootstrap

install -pm0755 vmware-horizon-client/bin/vmware-view{,-lib-scan,-log-collector} %{buildroot}%{_bindir}
cp -pr vmware-horizon-client/share/* %{buildroot}%{_datadir}
install -pm0644 vmware-horizon-client/extras/artwork/linux_view_128x.png %{buildroot}%{_datadir}/icons/vmware-view.png
install -pm0644 vmware-horizon-client/extras/artwork/linux_view_128x.png %{buildroot}%{_datadir}/pixmaps/vmware-view.png
desktop-file-validate %{buildroot}%{_datadir}/applications/vmware-view.desktop
install -pm0755 vmware-horizon-client/lib/vmware/view/bin/vmware-view %{buildroot}%{_prefix}/lib/vmware/view/bin
ln -s %{_libdir}/libudev.so.1 %{buildroot}%{_prefix}/lib/vmware/libudev.so.0
install -pm0644 vmware-horizon-client/doc/{open_source_licenses.txt,VMware-Horizon-Client-EULA*.txt} %{buildroot}%{_datadir}/doc/%{name}

install -pm0755 vmware-horizon-html5mmr/lib/vmware/libjson_linux-gcc-4.1.1_libmt.so %{buildroot}%{_prefix}/lib/vmware
cp -pr vmware-horizon-html5mmr/lib/vmware/view/html5mmr %{buildroot}%{_prefix}/lib/vmware/view
install -pm0755 vmware-horizon-html5mmr/lib/vmware/view/vdpService/libhtml5Client.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService

install -pm0755 vmware-horizon-integrated-printing/bin/prlinuxcupsppd %{buildroot}%{_bindir}
install -pm0755 vmware-horizon-integrated-printing/bin/vmware-print-redir-client %{buildroot}%{_prefix}/lib/vmware/view/integratedPrinting
install -pm0755 vmware-horizon-integrated-printing/lib/vmware/view/vdpService/libvmwprvdpplugin.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService

install -pm0755 vmware-horizon-media-provider/lib/libV264.so %{buildroot}%{_prefix}/lib/vmware/mediaprovider
install -pm0755 vmware-horizon-media-provider/lib/libVMWMediaProvider.so %{buildroot}%{_prefix}/lib/vmware/mediaprovider

echo "%{_prefix}/lib/pcoip/vchan_plugins/libvdpservice.so" > %{buildroot}%{_sysconfdir}/vmware/vdp/host_overlay_plugins/config
install -pm0755 vmware-horizon-mmr/lib/vmware/view/vdpService/libtsmmrClient.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService

install -pm0755 vmware-horizon-pcoip/pcoip/bin/vmware-flash-projector %{buildroot}%{_bindir}
install -pm0755 vmware-horizon-pcoip/pcoip/lib/libcoreavc_sdk.so %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/libpcoip_client.so %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/pcoip/vchan_plugins/lib*.so %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins
cp -pr vmware-horizon-pcoip/pcoip/lib/vmware/{rdpvcbridge,xkeymap} %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/view/client/vmware-remotemks %{buildroot}%{_prefix}/lib/vmware/view/client/
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/view/vdpService/lib*.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/libatkmm-1.6.so.1 %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/libgdkmm-3.0.so.1 %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/libgiomm-2.4.so.1 %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/libglibmm-2.4.so.1 %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/libgtkmm-3.0.so.1 %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/libpangomm-1.4.so.1 %{buildroot}%{_prefix}/lib/vmware

install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/lib{crypto,ssl}.so.1.0.2 %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-pcoip/pcoip/lib/vmware/libudpProxyLib.so %{buildroot}%{_prefix}/lib/vmware

install -pm0755 vmware-horizon-rtav/lib/pcoip/vchan_plugins/libviewMMDevRedir.so %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins

install -pm0644 vmware-horizon-scannerclient/bin/ftplugins.conf %{buildroot}/etc/vmware/ftplugins.conf
install -pm0755 vmware-horizon-scannerclient/bin/ftscanhvd %{buildroot}%{_prefix}/lib/vmware/view/bin
install -pm0755 vmware-horizon-scannerclient/lib/vmware/rdpvcbridge/ftnlses3hv.so %{buildroot}%{_prefix}/lib/vmware/rdpvcbridge
install -pm0644 %{S:13} %{buildroot}%{_unitdir}

install -pm0755 vmware-horizon-seamless-window/lib/vmware/libcrtbora.so %{buildroot}%{_prefix}/lib/vmware
install -pm0755 vmware-horizon-seamless-window/lib/vmware/libvmwarebase.so %{buildroot}%{_prefix}/lib/vmware

install -pm0755 vmware-horizon-serialportclient/bin/ftsprhvd %{buildroot}%{_prefix}/lib/vmware/view/bin
install -pm0755 vmware-horizon-serialportclient/lib/vmware/rdpvcbridge/ftnlses3hv.so %{buildroot}%{_prefix}/lib/vmware/rdpvcbridge
install -pm0644 %{S:12} %{buildroot}%{_unitdir}

install -pm0755 vmware-horizon-smartcard/lib/pcoip/vchan_plugins/libscredirvchanclient.so %{buildroot}%{_prefix}/lib/pcoip/vchan_plugins
ln -s /usr/lib64/pkcs11/opensc-pkcs11.so %{buildroot}%{_prefix}/lib/vmware/view/pkcs11/libopenscpkcs11.so

install -pm0755 vmware-horizon-tsdr/lib/vmware/view/vdpService/libtsdrClient.so %{buildroot}%{_prefix}/lib/vmware/view/vdpService

install -pm0755 vmware-horizon-usb/bin/vmware-view-usbdloader %{buildroot}%{_bindir}
install -pm0755 vmware-horizon-usb/lib/vmware/view/usb/{vmware-usbarbitrator,libvmware-view-usbd.so} %{buildroot}%{_prefix}/lib/vmware/view/usb
install -pm0755 vmware-horizon-usb/lib/vmware/view/vdpService/libusbRedirectionClient.so  %{buildroot}%{_prefix}/lib/vmware/view/vdpService

ln -s ../lib/vmware/view/usb/vmware-usbarbitrator %{buildroot}%{_bindir}
install -pm0644 %{S:10} %{buildroot}%{_sysconfdir}/vmware
install -pm0644 %{S:11} %{buildroot}%{_unitdir}

#install -pm0755 vmware-horizon-virtual-printing/

%find_lang vmware-view

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post scannerclient
TMPDIR=$(%{_bindir}/mktemp -d)
cat >> $TMPDIR/%{name}-scannerclient-rpm.cil << __EOF__
(typeattributeset cil_gen_require init_t)
(typeattributeset cil_gen_require printer_device_t)
(typeattributeset cil_gen_require tmp_t)
(typeattributeset cil_gen_require usb_device_t)
(typeattributeset cil_gen_require v4l_device_t)
(allow init_t tmp_t (sock_file (create setattr unlink)))
(allow init_t printer_device_t (chr_file (open read)))
(allow init_t usb_device_t (chr_file (ioctl open read write)))
(allow init_t v4l_device_t (chr_file (ioctl open read write)))
__EOF__
%{_sbindir}/semodule -i $TMPDIR/%{name}-scannerclient-rpm.cil
rm $TMPDIR/%{name}-scannerclient-rpm.cil
rmdir $TMPDIR
%systemd_post vmware-ftscanhvd.service
exit 0

%preun scannerclient
%systemd_preun vmware-ftscanhvd.service

%postun scannerclient
%systemd_postun_with_restart vmware-ftscanhvd.service
if [ $1 -eq 0 ]; then
  %{_sbindir}/semodule -r %{name}-scannerclient-rpm || :
fi

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
%license %{_docdir}/%{name}/open_source_licenses.txt
%license %lang(de) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-de.txt
%license %{_docdir}/%{name}/VMware-Horizon-Client-EULA-en.txt
%license %lang(es) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-es.txt
%license %lang(fr) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-fr.txt
%license %lang(ja) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-ja.txt
%license %lang(ko) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-ko.txt
%license %lang(zh_CN) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-zh_CN.txt
%license %lang(zh_TW) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-zh_TW.txt
%doc horizon-client-linux-%{docvnd}-release-notes.html
%doc horizon-client-linux-installation.pdf
%dir %{_sysconfdir}/vmware
%config %{_sysconfdir}/vmware/bootstrap
%attr(0644,root,root) %config(noreplace) %ghost %{_sysconfdir}/vmware/config
%attr(0644,root,root) %config(noreplace) %ghost %{_sysconfdir}/vmware/view-keycombos-config
%dir %{_sysconfdir}/vmware/udpProxy
%attr(0644,root,root) %config(noreplace) %ghost %{_sysconfdir}/vmware/udpProxy/config
%dir %{_sysconfdir}/vmware/vdp
%dir %{_sysconfdir}/vmware-vix
%config %{_sysconfdir}/vmware-vix/bootstrap
%{_bindir}/vmware-view
%{_bindir}/vmware-view-lib-scan
%{_bindir}/vmware-view-log-collector
%{_bindir}/vmware-view-usbdloader
%dir %{_prefix}/lib/vmware
%attr(0644,root,root) %config(noreplace) %ghost %{_prefix}/lib/vmware/config
%{_prefix}/lib/vmware/libatkmm-1.6.so.1
%{_prefix}/lib/vmware/libcoreavc_sdk.so
%{_prefix}/lib/vmware/libcrtbora.so
%{_prefix}/lib/vmware/libcrypto.so.1.0.2
%{_prefix}/lib/vmware/libgdkmm-3.0.so.1
%{_prefix}/lib/vmware/libgiomm-2.4.so.1
%{_prefix}/lib/vmware/libglibmm-2.4.so.1
%{_prefix}/lib/vmware/libgtkmm-3.0.so.1
%{_prefix}/lib/vmware/libpangomm-1.4.so.1
%{_prefix}/lib/vmware/libssl.so.1.0.2
%{_prefix}/lib/vmware/libudev.so.0
%{_prefix}/lib/vmware/libudpProxyLib.so
%{_prefix}/lib/vmware/libvmwarebase.so
%dir %{_prefix}/lib/vmware/rdpvcbridge
%{_prefix}/lib/vmware/rdpvcbridge/ftnlses3hv.so
%attr(0644,root,root) %config(noreplace) %ghost %{_prefix}/lib/vmware/settings
%dir %{_prefix}/lib/vmware/view
%dir %{_prefix}/lib/vmware/view/bin
%{_prefix}/lib/vmware/view/bin/vmware-view
%dir %{_prefix}/lib/vmware/view/vdpService
%{_datadir}/applications/vmware-view.desktop
%{_datadir}/icons/vmware-view.png
%{_datadir}/pixmaps/vmware-view.png
%{_datadir}/X11/xorg.conf.d/20-vmware-hid.conf
%{_var}/log/vmware

%files html5mmr
%{_prefix}/lib/vmware/libjson_linux-gcc-4.1.1_libmt.so
%{_prefix}/lib/vmware/view/html5mmr
%{_prefix}/lib/vmware/view/vdpService/libhtml5Client.so

%files integrated-printing
%{_bindir}/prlinuxcupsppd
%dir %{_prefix}/lib/vmware/view/integratedPrinting
%{_prefix}/lib/vmware/view/integratedPrinting/vmware-print-redir-client
%{_prefix}/lib/vmware/view/vdpService/libvmwprvdpplugin.so

%files media-provider
%dir %{_prefix}/lib/vmware/mediaprovider
%{_prefix}/lib/vmware/mediaprovider/libV264.so
%{_prefix}/lib/vmware/mediaprovider/libVMWMediaProvider.so

%files mmr
%dir %{_sysconfdir}/vmware/vdp/host_overlay_plugins
%config(noreplace) %{_sysconfdir}/vmware/vdp/host_overlay_plugins/config
%{_prefix}/lib/vmware/view/vdpService/libtsmmrClient.so

%files pcoip
%dir %{_sysconfdir}/teradici
%attr(0644,root,root) %config(noreplace) %ghost %{_sysconfdir}/teradici/pcoip_admin.conf
%attr(0644,root,root) %config(noreplace) %ghost %{_sysconfdir}/teradici/pcoip_admin_defaults.conf
%{_bindir}/vmware-flash-projector
%dir %{_prefix}/lib/pcoip
%dir %{_prefix}/lib/pcoip/vchan_plugins
%{_prefix}/lib/pcoip/vchan_plugins/librdpvcbridge.so
%{_prefix}/lib/pcoip/vchan_plugins/libvdpservice.so
%{_prefix}/lib/vmware/libpcoip_client.so
%{_prefix}/lib/vmware/rdpvcbridge/freerdp_plugins.conf
%{_prefix}/lib/vmware/view/client/vmware-remotemks
%{_prefix}/lib/vmware/view/vdpService/libmksvchanclient.so
%{_prefix}/lib/vmware/view/vdpService/librdeSvc.so
%{_prefix}/lib/vmware/view/vdpService/libviewMPClient.so
%{_prefix}/lib/vmware/xkeymap

%files rtav
%{_prefix}/lib/pcoip/vchan_plugins/libviewMMDevRedir.so

%files scannerclient
%config(noreplace) /etc/vmware/ftplugins.conf
%{_prefix}/lib/vmware/view/bin/ftscanhvd
%{_unitdir}/vmware-ftscanhvd.service

%files serialportclient
%attr(0644,root,root) %config(noreplace) %ghost %{_sysconfdir}/ftsprhv.db
%{_prefix}/lib/vmware/view/bin/ftsprhvd
%{_unitdir}/vmware-ftsprhvd.service

%files smartcard
%{_prefix}/lib/pcoip/vchan_plugins/libscredirvchanclient.so
%dir %{_prefix}/lib/vmware/view/pkcs11
%{_prefix}/lib/vmware/view/pkcs11/libopenscpkcs11.so

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
* Wed Dec 18 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 5.3.0.15208949-1
- update to 5.3.0 build 15208949
- update bundled components list

* Sun Sep 29 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 5.2.0.14604769-1
- update to 5.2.0 build 14604769
- updated bundled components list
- seamless window support is now mandatory, merge into main package

* Thu Jul 25 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 5.1.0.13956721-3
- own some more optional config files

* Mon Jul 22 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 5.1.0.13956721-2
- include some bundled libraries to fix Seamless Window Feature
- ship both legacy and new remotemks binaries

* Wed Jul 03 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 5.1.0.13956721-1
- update to 5.1.0 build 13956721
- include HTML5 Multimedia Redirection and Integrated Printing features
- update internal Requires filter
- update bundled components list
- mention minimum Horizon Agent version requirements where applicable
- improve smartcard auth support (untested)

* Fri Mar 15 2019 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 5.0.0.12557422-1
- update to 5.0.0 build 12557422
- include Scanner Redirection feature

* Tue Dec 18 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.10.0.11053294-1
- update to 4.10.0 build 11053294

* Fri Nov 23 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.9.0.9507999-4
- drop fedora conditional, master is Fedora only now
- use dist tag as packages are now slightly different

* Fri Oct 26 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.9.0.9507999-3
- move libcoreavc_sdk.so to the main package (required by two others)
- drop libffi.so.5 hack
- own optional config files

* Tue Oct 16 2018 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 4.9.0.9507999-2
- add missing libcoreavc_sdk.so library in pcoip subpackage
- simplify Provides: filtering
- fix unowned dir /usr/lib/vmware/mediaprovider
- use chrpath and execstack only files which need it
- move Seamless Window Feature plugin to a subpackage and patch the wrapper
  to use it only if installed

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
