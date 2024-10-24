%undefine _missing_build_ids_terminate_build
%undefine _enable_debug_packages
%undefine _unique_build_ids
%global _no_recompute_build_ids 1
%global cart   25FQ2
%global yymm   2406
%global ver    8.13.0
%global rel    9995429239
%global fver   %{yymm}-%{ver}-%{rel}
%global vhc_arch x64
%bcond bundled_ssl 0
%bcond bundled_gtk 1

Summary: Remote access client for VMware Horizon
Name: vmware-horizon-client
Version: %{yymm}.%{ver}.%{rel}
Release: 3%{?dist}
URL: https://docs.omnissa.com/category/VMware-Horizon
# https://customerconnect.omnissa.com/downloads/info/slug/desktop_end_user_computing/vmware_horizon_clients/horizon_8
Source0: https://download3.omnissa.com/software/CART%{cart}_LIN_%{yymm}_TARBALL/VMware-Horizon-Client-Linux-%{yymm}-%{ver}-%{rel}.tar.gz
# https://docs.omnissa.com/pl-PL/bundle/horizon-client-linux-rnV2406/page/HorizonClientLinux-ReleaseNotes.html
Source1: vmware-horizon-client-for-linux-%{yymm}-release-notes.pdf
# https://docs.omnissa.com/pl-PL/bundle/HorizonClientLinuxGuideV2406/page/HorizonClientforLinuxGuide.html
Source2: horizon-client-for-linux-guide-%{yymm}.pdf
Source3: https://docs.broadcom.com/doc/end-user-agreement-english#/end-user-agreement-english.pdf
Source10: usbarb.rules
Source11: vmware-eucusbarbitrator.service
Source14: vmware-eucusbarbitrator.preset
Source15: vmware-ftsprhv.preset
Source16: vmware-ftscanhv.preset
Patch0: %{name}-desktop.patch
License: VMware
ExclusiveArch: x86_64
BuildRequires: chrpath
BuildRequires: desktop-file-utils
BuildRequires: %{_bindir}/execstack
BuildRequires: systemd-rpm-macros
Provides: bundled(atk) = 2.28.1
Provides: bundled(boost) = 1.67
Provides: bundled(bzip2) = 1.0.6
Provides: bundled(c-ares) = 1.13.0
%if %{with bundled_gtk}
Provides: bundled(atkmm30) = 2.22.7
Provides: bundled(gtkmm30) = 3.10.1
Provides: bundled(libsigc++20)
%endif
Provides: bundled(hal) = 0.5.12
Provides: bundled(icu) = 60.2
Provides: bundled(libjpeg-turbo) = 1.4.2
Provides: bundled(libwebrtc) = 90
Provides: bundled(libxml2) = 2.9.9
Provides: bundled(mechanical-fonts) = 1.00
%if %{with bundled_ssl}
Provides: bundled(curl) = 8.5.0
Provides: bundled(openssl) = 3.0.12
%endif
Provides: bundled(opus) = 1.1.4.60
Provides: bundled(speex) = 1.2rc3
Provides: bundled(zlib) = 1.2.11
Provides: %{name}-seamless-window = %{version}-%{release}
Obsoletes: %{name}-media-provider < 2303.8.9.0.21435420
Obsoletes: %{name}-seamless-window < 5.2.0.14604769
Requires: %{_bindir}/pidof
Requires: libudev.so.1()(64bit)

%global __provides_exclude_from ^%{_prefix}/lib/(vmware|pcoip)/.*$
%global __requires_exclude ^lib\(avcodec\\.so\\.60\|avutil\\.so\\.58\|ffi\\.so%{?with_bundled_gtk:\|atkmm-1\\.6\\.so\\.1\|gdkmm-3\\.0\\.so\\.1\|giomm-2\\.4\\.so\\.1\|glibmm-2\\.4\\.so\\.1\|gtkmm-3\\.0\\.so\\.1\|pangomm-1\\.4\\.so\\.1\|sigc-2\\.0\\.so\\.0}%{?with_bundled_ssl:\|\(crypto\|ssl\)\\.so\\.3\|curl\\.so\\.4}\|udev\\.so\\.0\|x264\\.so\\.164\\.5\|\(cef\|clientSdkCPrimitive\|crtbora\|GLESv2\|Microsoft.SlimCV.VBM\|vmware\(base\|-view-usbd\)\)\\.so).*$

%description
Remote access client for VMware Horizon.

Requires Horizon Agent 7.0 or later on the virtual desktop.

%package html5mmr
Summary: HTML5 Multimedia Redirection support plugin for VMware Horizon Client
Provides: bundled(chromium-embedded-framework) = 126.0.6478.127
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

%package mmr
Summary: Multimedia Redirection support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}
Requires: libgstlibav.so()(64bit)
Recommends: gstreamer1-vaapi%{_isa}

%description mmr
Multimedia Redirection support plugin for VMware Horizon Client.

Requires Horizon Agent 7.0 or later on the virtual desktop.

%package pcoip
Summary: PCoIP support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}
Provides: bundled(libavcodec) = 6.1.1
Provides: bundled(libavformat) = 6.1.1
Provides: bundled(libavutil) = 6.1.1
Provides: bundled(libpng) = 1.6.37
Provides: bundled(pcoip-soft-clients) = 3.75

%description pcoip
PCoIP support plugin for VMware Horizon Client.

Requires Horizon Agent 7.0.2 or later on the virtual desktop.

%package rtav
Summary: Real-Time Audio-Video support plugin for VMware Horizon Client
Requires: %{name}-pcoip = %{version}-%{release}
Requires: libspeex.so.1()(64bit)
Requires: libtheoradec.so.1()(64bit)
Requires: libtheoraenc.so.1()(64bit)
Provides: bundled(x264-libs) = 0.164

%description rtav
Real-Time Audio-Video support plugin for VMware Horizon Client.

Requires Horizon Agent 7.0 or later on the virtual desktop.

%package scannerclient
Summary: Scanner redirection support plugin for VMware Horizon Client
Provides: bundled(scanner_linux) = 2.6.3
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
Provides: bundled(serial_linux) = 2.6.3
Requires: %{name} = %{version}-%{release}
Requires: libudev.so.1()(64bit)

%description serialportclient
Serial port redirection support plugin for VMware Horizon Client.

Requires Horizon Agent 7.6 or later on the virtual desktop.

%package smartcard
Summary: SmartCard authentication support plugin for VMware Horizon Client
Requires: %{name}-pcoip = %{version}-%{release}
Requires: opensc%{_isa}

%description smartcard
SmartCard authentication support plugin for VMware Horizon Client.

%package teams
Summary: Media Optimization for Microsoft Teams support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}

%description teams
The Media Optimization for Microsoft Teams redirects audio calls, video calls,
and viewing desktop shares for a seamless experience between the client system
and the remote session without negatively affecting the virtual infrastructure
and overloading the network. Microsoft Teams media processing takes place on the
client machine instead of in the virtual desktop and does not rely on Real-Time
Audio-Video (RTAV).

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

%prep
%setup -q -n VMware-Horizon-Client-Linux-%{yymm}-%{ver}-%{rel}
cp -p %{S:1} %{S:2} %{S:3} ./

%build

%install
install -dm0755 %{buildroot}/etc/teradici
install -dm0755 %{buildroot}/etc/vmware{/udpProxy,/vdp/host_overlay_plugins,-vix}
install -dm0755 %{buildroot}%{_presetdir}
install -dm0755 %{buildroot}%{_unitdir}
install -dm0755 %{buildroot}/usr/lib/vmware/view/pkcs11
install -dm0755 %{buildroot}%{_datadir}/doc
install -dm0755 %{buildroot}/var/log/vmware

pushd x64
for f in \
  VMware-Horizon-Client-%{yymm}-%{ver}-%{rel}.x64.tar.gz \
  VMware-Horizon-PCoIP-%{yymm}-%{ver}-%{rel}.x64.tar.gz \
  VMware-Horizon-USB-%{yymm}-%{ver}-%{rel}.x64.tar.gz \
  VMware-Horizon-html5mmr-%{yymm}-%{ver}-%{rel}.x64.tar.gz \
  VMware-Horizon-integratedPrinting-%{yymm}-%{ver}-%{rel}.x64.tar.gz \
  VMware-Horizon-scannerClient-%{yymm}-%{ver}-%{rel}.x64.tar.gz \
  VMware-Horizon-serialportClient-%{yymm}-%{ver}-%{rel}.x64.tar.gz \
; do
  tar xzf ${f} -C %{buildroot} --strip-components=1
done
popd

pushd %{buildroot}

mv -v usr/lib{,/vmware}/libclientSdkCPrimitive.so
mv -v usr/lib{,/vmware}/libpcoip_client.so
mv -v usr/lib/vmware/view/integratedPrinting/prlinuxcupsppd ./%{_bindir}
mv -v usr/lib/vmware/view/usb/vmware-eucusbarbitrator ./%{_bindir}

pushd usr/lib/vmware/view/html5mmr
find . -type f | xargs chmod 644
popd

chrpath -d usr/lib/vmware/view/bin/ftscanhvd

rm -frv \
  etc/init.d \
  etc/udev \
  usr/lib/vmware/gcc \
%if %{without bundled_ssl}
  usr/lib/vmware/fips.so \
  usr/lib/vmware/libcrypto.so.3 \
  usr/lib/vmware/libcurl.so.4 \
  usr/lib/vmware/libssl.so.3 \
%endif
%if %{without bundled_gtk}
  usr/lib/vmware/libatkmm-1.6.so.1 \
  usr/lib/vmware/libgdkmm-3.0.so.1 \
  usr/lib/vmware/libgiomm-2.4.so.1 \
  usr/lib/vmware/libglibmm-2.4.so.1 \
  usr/lib/vmware/libgtkmm-3.0.so.1 \
  usr/lib/vmware/libpangomm-1.4.so.1 \
  usr/lib/vmware/libsigc-2.0.so.0 \
%endif
  usr/lib/vmware/libcairomm-1.0.so.1 \
  usr/lib/vmware/libpng16.so.16 \
  usr/lib/vmware/libz.so.1 \
  usr/lib/vmware/view/html5mmr/libvulkan.so.1 \
  usr/lib/vmware/view/integratedPrinting/{integrated-printing-setup.sh,README} \
  usr/lib/vmware/view/urlRedirection/install-url-redirection.py \
  usr/lib/vmware/view/vaapi{,2.7} \
  README \
  usr/share/doc/%{name}/patches \
  usr/share/doc/%{name}/scannerClient/README \
  usr/share/doc/%{name}/serialPortClient/README \

find . -type f | xargs file | grep ELF | cut -d: -f1 | xargs chmod 755
%if %{with bundled_gtk}
chrpath -d usr/lib/vmware/libsigc-2.0.so.0
%endif

echo 'BINDIR="%{_bindir}"' > etc/vmware/bootstrap
echo 'BINDIR="%{_bindir}"' > etc/vmware-vix/bootstrap
echo "/usr/lib/pcoip/vchan_plugins/libvdpservice.so" > etc/vmware/vdp/host_overlay_plugins/config

patch -p1 ./%{_datadir}/applications/vmware-view.desktop %{PATCH0}

desktop-file-validate ./%{_datadir}/applications/vmware-view.desktop

install -pm0644 %{S:10} etc/vmware
install -pm0644 %{S:11} ./%{_unitdir}
mv systemd/system/ftsprhv.service ./%{_unitdir}/
mv systemd/system/ftscanhv.service ./%{_unitdir}/
install -pm0644 %{S:15} ./%{_presetdir}/96-ftsprhv.preset
install -pm0644 %{S:16} ./%{_presetdir}/96-ftscanhv.preset
install -pm0644 %{S:14} ./%{_presetdir}/96-vmware-eucusbarbitrator.preset

ln -s ../../%{_lib}/libudev.so.1 usr/lib/vmware/libudev.so.0
ln -s ../../../../%{_lib}/pkcs11/opensc-pkcs11.so usr/lib/vmware/view/pkcs11/libopenscpkcs11.so

popd

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
%systemd_post ftscanhv.service
exit 0

%preun scannerclient
%systemd_preun ftscanhv.service

%postun scannerclient
%systemd_postun_with_restart ftscanhv.service
if [ $1 -eq 0 ]; then
  %{_sbindir}/semodule -r %{name}-scannerclient-rpm || :
fi

%post serialportclient
%systemd_post ftsprhv.service
exit 0

%preun serialportclient
%systemd_preun ftsprhvd.service

%postun serialportclient
%systemd_postun_with_restart ftsprhv.service

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
%systemd_post vmware-eucusbarbitrator.service
exit 0

%preun usb
%systemd_preun vmware-eucusbarbitrator.service

%postun usb
%systemd_postun_with_restart vmware-eucusbarbitrator.service
if [ $1 -eq 0 ]; then
  %{_sbindir}/semodule -r %{name}-usb-rpm || :
fi

%files -f vmware-view.lang
%license end-user-agreement-english.pdf
%license %{_docdir}/%{name}/open_source_licenses.txt
%doc vmware-horizon-client-for-linux-%{yymm}-release-notes.pdf
%doc horizon-client-for-linux-guide-%{yymm}.pdf
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
%dir %{_prefix}/lib/vmware
%attr(0644,root,root) %config(noreplace) %ghost %{_prefix}/lib/vmware/config
%{_prefix}/lib/vmware/view/dct
%dir %{_prefix}/lib/vmware/view/env
%{_prefix}/lib/vmware/view/env/vmware-view.info
%{_prefix}/lib/vmware/libclientSdkCPrimitive.so
%{_prefix}/lib/vmware/libcrtbora.so
%if %{with bundled_ssl}
%{_prefix}/lib/vmware/fips.so
%{_prefix}/lib/vmware/libcrypto.so.3
%{_prefix}/lib/vmware/libcurl.so.4
%{_prefix}/lib/vmware/libssl.so.3
%endif
%if %{with bundled_gtk}
%{_prefix}/lib/vmware/libatkmm-1.6.so.1
%{_prefix}/lib/vmware/libgdkmm-3.0.so.1
%{_prefix}/lib/vmware/libgiomm-2.4.so.1
%{_prefix}/lib/vmware/libglibmm-2.4.so.1
%{_prefix}/lib/vmware/libgtkmm-3.0.so.1
%{_prefix}/lib/vmware/libpangomm-1.4.so.1
%{_prefix}/lib/vmware/libsigc-2.0.so.0
%endif
%{_prefix}/lib/vmware/librtavCliLib.so
%{_prefix}/lib/vmware/libudev.so.0
%{_prefix}/lib/vmware/libudpProxyLib.so
%{_prefix}/lib/vmware/libvmwarebase.so
%{_prefix}/lib/vmware/rdpvcbridge/ftnlses3hv.so
%{_prefix}/lib/vmware/liburlFilterPlugin.so
%{_prefix}/lib/vmware/view/bin/vmware-urlFilter
%{_bindir}/vmware-url-filter
%dir %{_prefix}/lib/vmware/rdpvcbridge
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

%files pcoip
%dir %{_sysconfdir}/teradici
%attr(0644,root,root) %config(noreplace) %ghost %{_sysconfdir}/teradici/pcoip_admin.conf
%attr(0644,root,root) %config(noreplace) %ghost %{_sysconfdir}/teradici/pcoip_admin_defaults.conf
%dir %{_sysconfdir}/vmware/vdp/host_overlay_plugins
%config(noreplace) %{_sysconfdir}/vmware/vdp/host_overlay_plugins/config
%dir %{_prefix}/lib/pcoip
%dir %{_prefix}/lib/pcoip/vchan_plugins
%{_prefix}/lib/pcoip/vchan_plugins/libvdpservice.so
%{_prefix}/lib/pcoip/vchan_plugins/librdpvcbridge.so
%{_prefix}/lib/vmware/rdpvcbridge/freerdp_plugins.conf
%{_prefix}/lib/vmware/libffi.so
%{_prefix}/lib/vmware/libpcoip_client.so
%{_prefix}/lib/vmware/view/client/vmware-remotemks
%{_prefix}/lib/vmware/view/vdpService/libMicrosoft.SlimCV.VBM.so
%{_prefix}/lib/vmware/view/vdpService/libmksvchanclient.so
%{_prefix}/lib/vmware/view/vdpService/librdeSvc.so
%{_prefix}/lib/vmware/view/software
%{_prefix}/lib/vmware/view/vaapi2
%{_prefix}/lib/vmware/view/vdpau
%{_prefix}/lib/vmware/xkeymap

%files rtav
%{_prefix}/lib/pcoip/vchan_plugins/libviewMMDevRedir.so
%{_prefix}/lib/vmware/libx264.so.164.5

%files smartcard
%{_prefix}/lib/pcoip/vchan_plugins/libscredirvchanclient.so
%dir %{_prefix}/lib/vmware/view/pkcs11
%{_prefix}/lib/vmware/view/pkcs11/libopenscpkcs11.so

%files usb
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/vmware/usbarb.rules
%{_presetdir}/96-vmware-eucusbarbitrator.preset
%{_unitdir}/vmware-eucusbarbitrator.service
%{_bindir}/vmware-eucusbarbitrator
%dir %{_prefix}/lib/vmware/view/usb
%{_prefix}/lib/vmware/view/usb/libvmware-view-usbd.so
%{_prefix}/lib/vmware/view/vdpService/libusbRedirectionClient.so

%files html5mmr
%{_prefix}/lib/vmware/view/html5mmr
%{_prefix}/lib/vmware/view/vdpService/libhtml5Client.so

%files integrated-printing
%{_bindir}/prlinuxcupsppd
%dir %{_prefix}/lib/vmware/view/integratedPrinting
%{_prefix}/lib/vmware/view/integratedPrinting/vmware-print-redir-client
%{_prefix}/lib/vmware/view/vdpService/libvmwprvdpplugin.so

%files mmr
%{_prefix}/lib/vmware/view/vdpService/libtsmmrClient.so

%files scannerclient
%config(noreplace) /etc/vmware/ftplugins.conf
%{_prefix}/lib/vmware/view/bin/ftscanhvd
%{_presetdir}/96-ftscanhv.preset
%{_unitdir}/ftscanhv.service

%files serialportclient
%attr(0644,root,root) %config(noreplace) %ghost %{_sysconfdir}/ftsprhv.db
%{_prefix}/lib/vmware/view/bin/ftsprhvd
%{_presetdir}/96-ftsprhv.preset
%{_unitdir}/ftsprhv.service

%files teams
%{_prefix}/lib/vmware/view/vdpService/webrtcRedir

%files tsdr
%{_prefix}/lib/vmware/view/vdpService/libtsdrClient.so

%changelog
* Wed Oct 23 2024 Dominik Mierzejewski <dominik@greysector.net> 2406.8.13.0.9995429239-3
- switch to bundled libsigc++20 (rhbz#2321251)
- drop support for building for armv7hl
- using system cairomm seems to prevent crashes

* Mon Sep 09 2024 Dominik Mierzejewski <dominik@greysector.net> 2406.8.13.0.9995429239-2
- switch to bundled gtkmm, curl and openssl libraries

* Thu Aug 29 2024 Dominik Mierzejewski <dominik@greysector.net> 2406.8.13.0.9995429239-1
- update to 2406 (8.13.0-9995429239)
- update upstream URLs
- rename usbarbitrator service and preset

* Tue Feb 20 2024 Dominik Mierzejewski <dominik@greysector.net> 2312.8.12.0.23149323-1
- update to 2312 (8.12.0-23149323)
- keep bundled CURL and OpenSSL due to missing symbols in Fedora < 40 build

* Thu Nov 09 2023 Dominik Mierzejewski <dominik@greysector.net> 2309.8.11.0.22660930-3
- update to 2309 (8.11.0-22660930)
- unbundle curl and openssl

* Tue Sep 26 2023 Dominik Mierzejewski <dominik@greysector.net> 2306-8.10.0-21964631-3
- unbundle GDK/GTK libraries again, the display errors were unrelated

* Mon Jul 10 2023 Dominik Mierzejewski <dominik@greysector.net> 2306-8.10.0-21964631-2
- retain bundled GDK/GTK libraries to fix display errors

* Fri Jul 07 2023 Dominik Mierzejewski <dominik@greysector.net> 2306-8.10.0-21964631-1
- update to 2306 (8.10.0-21964631)
- drop unnecessary patch
- retain bundled FFmpeg-5.1.2 libraries (but drop those linked with old libva)
- unbundle atkmm, glibmm2.4, gtkmm3.0 (except libgtkmm-3.0.so.1) and pangomm

* Sun Apr 16 2023 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> 2303.8.9.0.21435420-1
- update to 2303 (8.9.0-21435420)
- add missing dependency on opensc to smartcard support subpackage
- drop media-provider subpackage (Skype no longer supported upstream)

* Mon Mar 13 2023 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> 2212.8.8.0.21079016-1
- update to 2212 (8.8.0.21079016)

* Thu Nov 03 2022 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> 2209.8.7.0.20616018-1
- update to 2209 (8.7.0.20616018)
- use upstream systemd service files

* Fri Sep 09 2022 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> 2206.8.6.0.20094634-3
- update gstreamer1 libav plugin dependency to work with both Fedora and RPM Fusion builds

* Wed Aug 24 2022 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> 2206.8.6.0.20094634-2
- put back librtavCliLib.so, it's used by vmware-view via libclientSdkCPrimitive.so

* Mon Aug 08 2022 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> 2206.8.6.0.20094634-1
- update to 2206 (8.6.0.20094634)
- drop unused librtavCliLib.so library
- drop duplicate libhtml5Client.so library

* Thu May 05 2022 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> 2203.8.5.0.19586897-1
- update to 2203 (8.5.0.19586897)

* Mon Mar 21 2022 Dominik 'Rathann' Mierzejewski <dominik@greysector.net> 2111.8.4.0.18957622-3
- stop unbundling libx264, ABI 157 is strictly required

* Fri Dec 03 2021 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 2111.8.4.0.18957622-2
- fix build on ARM: RDP is available, but URL redirection isn't

* Thu Dec 02 2021 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 2111.8.4.0.18957622-1
- update to 2111 (8.4.0.18957622)
- use upstream tarball directly, it was trimmed to 315M

* Tue Jul 20 2021 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 2106.8.3.0.18251983-1
- update to 2106 (8.3.0-18251983)
- include Media Optimization for Microsoft Teams plugin
- rtav is available on ARM

* Wed May 12 2021 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 2103.8.2.0.17742757-2
- add support for building on RHEL/CentOS 8

* Fri Apr 16 2021 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 2103.8.2.0.17742757-1
- update to 2103 (8.2.0.17742757)
- switch manual dependencies to gstreamer1 (finally!)

* Wed Nov 18 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 2006.8.0.0.16522670-4
- fix build on ARM 32-bit (rtav, scannerclient, serialportclient and tsdr are unavailable)
- move vdp config to correct subpackage (pcoip)

* Thu Sep 17 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 2006.8.0.0.16522670-3
- drop freerdp1.2 requirement

* Thu Sep 03 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 2006.8.0.0.16522670-2
- add symlinks to system FFmpeg libraries, they seem to be hardcoded

* Tue Sep 01 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 2006.8.0.0.16522670-1
- update to 2006 (8.0.0.16522670)
- unbundle libx264

* Mon Jun 29 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 5.4.1.15988340-3
- add armv7hl support

* Tue Jun 09 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 5.4.1.15988340-2
- enable services by default

* Wed Jun 03 2020  Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 5.4.1.15988340-1
- update to 5.4.1.15988340
- switch "source" to tarball download
- move most "installation" logic to mktarball script

* Fri Mar 20 2020 Dominik 'Rathann' Mierzejewski <rpm@greysector.net> 5.4.0.15805449-1
- update to 5.4.0 build 15805449
- generate the list of binaries to run execstack on on-the-fly
- update bundled dependency versions
- use correct build time dependency for systemd macros

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
