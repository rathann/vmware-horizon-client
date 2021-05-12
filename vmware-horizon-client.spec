%undefine _missing_build_ids_terminate_build
%undefine _debugsource_packages
%undefine _unique_build_ids
%global _no_recompute_build_ids 1
%global cart   CART22FQ1
%global yymm   2103
%global ver    8.2.0
%global rel    17742757
%global fver   %{yymm}-%{ver}-%{rel}
%ifarch x86_64
%global mark64 ()(64bit)
%else
%global mark64 %nil
%endif

Summary: Remote access client for VMware Horizon
Name: vmware-horizon-client
Version: %{yymm}.%{ver}.%{rel}
Release: 2%{?dist}
URL: https://www.vmware.com/products/horizon.html
# Source0 is built by mktarball.sh script, see Source100 comment
Source0: %{name}-%{fver}.tar.zst
Source1: https://docs.vmware.com/en/VMware-Horizon-Client-for-Linux/%{yymm}/rn/horizon-client-linux-%{yymm}-release-notes.html
Source2: https://docs.vmware.com/en/VMware-Horizon-Client-for-Linux/%{yymm}/horizon-client-linux-installation.pdf
Source10: usbarb.rules
Source11: vmware-usbarbitrator.service
Source12: vmware-ftsprhvd.service
Source13: vmware-ftscanhvd.service
Source14: vmware-usbarbitrator.preset
Source15: vmware-ftsprhvd.preset
Source16: vmware-ftscanhvd.preset
# upstream tarball is 0.5GB in size and contains binaries for all arches
# therefore run mktarball.sh before rpmbuild and provide the generated .tar.zstd  as Source0
Source100: vmware-horizon-client-mktarball.sh
Patch0: %{name}-desktop.patch
Patch1: %{name}-fedora.patch
License: VMware
ExclusiveArch: armv7hl x86_64
%ifarch x86_64
BuildRequires: chrpath
BuildRequires: x264-libs%{_isa}
%endif
BuildRequires: desktop-file-utils
BuildRequires: %{_bindir}/execstack
BuildRequires: systemd-rpm-macros
BuildRequires: zstd
Provides: bundled(atk) = 2.28.1
Provides: bundled(atkmm) = 2.22.7
Provides: bundled(boost) = 1.67
Provides: bundled(bzip2) = 1.0.6
Provides: bundled(c-ares) = 1.13.0
Provides: bundled(curl) = 7.74
Provides: bundled(glibmm24) = 2.44.0
Provides: bundled(gtkmm30) = 3.10.1
Provides: bundled(hal) = 0.5.12
Provides: bundled(icu) = 60.2
Provides: bundled(libjpeg-turbo) = 1.4.2
Provides: bundled(libwebrtc) = 90
Provides: bundled(libxml2) = 2.9.9
Provides: bundled(mechanical-fonts) = 1.00
Provides: bundled(openssl) = 1.0.2y
Provides: bundled(opus) = 1.1.4.60
Provides: bundled(pangomm) = 2.34.0
Provides: bundled(speex) = 1.2rc3
Provides: bundled(zlib) = 1.2.11
Provides: %{name}-seamless-window = %{version}-%{release}
Obsoletes: %{name}-seamless-window < 5.2.0.14604769
Requires: %{_bindir}/pidof
Requires: libudev.so.1%{mark64}

%global __provides_exclude_from ^%{_prefix}/lib/(vmware|pcoip)/.*$
%global __requires_exclude ^lib\(atkmm-1\\.6\\.so\\.1\|curl\\.so\\.4\|g\(io\|lib\)mm-2\\.4\\.so\\.1\|g\(dk\|tk\)mm-3\\.0\\.so\\.1\|pangomm-1\\.4\\.so\\.1\|\(crypto\|ssl\)\\.so\\.1\\.0\\.2\|udev\\.so\\.0\|\(cef\|crtbora\|GLESv2\|json_linux-gcc-4.1.1_libmt\|vmware\(base\|-view-usbd\)\)\\.so).*$

%description
Remote access client for VMware Horizon.

Requires Horizon Agent 7.0 or later on the virtual desktop.

%package html5mmr
Summary: HTML5 Multimedia Redirection support plugin for VMware Horizon Client
Provides: bundled(chromium-embedded-framework) = 87.0.4280.20
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
Provides: bundled(libjpeg-turbo) = 2.0.5
Provides: bundled(libsrtp) = 2.2.0
Provides: bundled(openssl) = 1.0.2y
Provides: bundled(webrtc) = 90

%description media-provider
Virtualization Pack for Skype for Business.

%package mmr
Summary: Multimedia Redirection support plugin for VMware Horizon Client
Requires: %{name} = %{version}-%{release}
Requires: gstreamer1-libav%{_isa}
Recommends: gstreamer1-vaapi%{_isa}

%description mmr
Multimedia Redirection support plugin for VMware Horizon Client.

Requires Horizon Agent 7.0 or later on the virtual desktop.

%package pcoip
Summary: PCoIP support plugin for VMware Horizon Client
Requires: libavcodec.so.58%{mark64}
Requires: libavutil.so.56%{mark64}
Requires: %{name} = %{version}-%{release}
Provides: bundled(libpng) = 1.6.37
Provides: bundled(pcoip-soft-clients) = 3.75
Provides: bundled(openssl) = 1.0.2w

%description pcoip
PCoIP support plugin for VMware Horizon Client.

Requires Horizon Agent 7.0.2 or later on the virtual desktop.

%package rtav
Summary: Real-Time Audio-Video support plugin for VMware Horizon Client
Requires: %{name}-pcoip = %{version}-%{release}
Requires: libspeex.so.1%{mark64}
Requires: libtheoradec.so.1%{mark64}
Requires: libtheoraenc.so.1%{mark64}
Requires: x264-libs%{_isa}

%description rtav
Real-Time Audio-Video support plugin for VMware Horizon Client.

Requires Horizon Agent 7.0 or later on the virtual desktop.

%package scannerclient
Summary: Scanner redirection support plugin for VMware Horizon Client
Provides: bundled(scanner_linux) = 2.6.3
%{?systemd_requires}
Requires: %{name} = %{version}-%{release}
Requires: libudev.so.1%{mark64}
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
Requires: libudev.so.1%{mark64}

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

%prep
%if 0%{?fedora}
%setup -q -n %{name}-%{fver}
%else
rm -rf %{name}-%{fver}
zstdmt -dc /builddir/build/SOURCES/%{name}-%{fver}.tar.zst | tar -xof -
%setup -qDT -n %{name}-%{fver}
%endif
%patch0 -p1
%patch1 -p1
cp -p %{S:1} %{S:2} ./
find  . -type f | xargs file | grep ELF | cut -d: -f1 | xargs -l execstack -q |\
  grep ^X | cut -d' ' -f2 | xargs -l execstack -c
pushd %{_target_cpu}
%ifarch x86_64
chrpath -d usr/lib/vmware/view/bin/ftscanhvd
ln -s ../..$(ls -1 /%{_lib}/libx264.so.*) usr/lib/vmware/libx264.so.157.6
%endif
ln -s ../../%{_lib}/libudev.so.1 usr/lib/vmware/libudev.so.0
ln -s ../../../../%{_lib}/pkcs11/opensc-pkcs11.so usr/lib/vmware/view/pkcs11/libopenscpkcs11.so
pushd usr/lib/vmware/view
for v in software vaapi2 vdpau ; do
  mkdir ${v}
  ln -s ../../../../lib64/libavcodec.so.58 ${v}/
  ln -s ../../../../lib64/libavutil.so.56 ${v}/
done
popd
popd

%build

%install
install -dm0755 %{buildroot}{%{_presetdir},%{_unitdir}}

pushd %{_target_cpu}
cp -pr etc usr var %{buildroot}/
popd

desktop-file-validate %{buildroot}%{_datadir}/applications/vmware-view.desktop

install -pm0644 %{S:10} %{buildroot}%{_sysconfdir}/vmware
install -pm0644 %{S:11} %{buildroot}%{_unitdir}
%ifarch x86_64
install -pm0644 %{S:13} %{buildroot}%{_unitdir}
install -pm0644 %{S:12} %{buildroot}%{_unitdir}
install -pm0644 %{S:15} %{buildroot}%{_presetdir}/96-vmware-ftsprhvd.preset
install -pm0644 %{S:16} %{buildroot}%{_presetdir}/96-vmware-ftscanhvd.preset
%endif
install -pm0644 %{S:14} %{buildroot}%{_presetdir}/96-vmware-usbarbitrator.preset

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

%files -f vmware-view.lang
%license %{_docdir}/%{name}/open_source_licenses.txt
%license %lang(de) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-de.txt
%license %{_docdir}/%{name}/VMware-Horizon-Client-EULA-en.txt
%license %lang(es) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-es.txt
%license %lang(fr) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-fr.txt
%license %lang(ja) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-ja.txt
%license %lang(ko) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-ko.txt
%license %lang(zh_CN) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-zh_CN.txt
%license %lang(zh_TW) %{_docdir}/%{name}/VMware-Horizon-Client-EULA-zh_TW.txt
%doc horizon-client-linux-%{yymm}-release-notes.html
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
%{_bindir}/vmware-url-filter
%{_bindir}/vmware-view
%{_bindir}/vmware-view-lib-scan
%{_bindir}/vmware-view-log-collector
%{_bindir}/vmware-view-usbdloader
%dir %{_prefix}/lib/vmware
%attr(0644,root,root) %config(noreplace) %ghost %{_prefix}/lib/vmware/config
%{_prefix}/lib/vmware/view/dct
%dir %{_prefix}/lib/vmware/view/env
%{_prefix}/lib/vmware/view/env/env_utils.sh
%{_prefix}/lib/vmware/view/env/vmware-view.info
%{_prefix}/lib/vmware/libatkmm-1.6.so.1
%{_prefix}/lib/vmware/libcrtbora.so
%{_prefix}/lib/vmware/libcrypto.so.1.0.2
%{_prefix}/lib/vmware/libcurl.so.4
%{_prefix}/lib/vmware/libgiomm-2.4.so.1
%{_prefix}/lib/vmware/libglibmm-2.4.so.1
%{_prefix}/lib/vmware/libssl.so.1.0.2
%{_prefix}/lib/vmware/libudev.so.0
%{_prefix}/lib/vmware/libudpProxyLib.so
%{_prefix}/lib/vmware/libvmwarebase.so
%ifarch x86_64
%{_prefix}/lib/vmware/libgdkmm-3.0.so.1
%{_prefix}/lib/vmware/libgtkmm-3.0.so.1
%{_prefix}/lib/vmware/libpangomm-1.4.so.1
%dir %{_prefix}/lib/vmware/rdpvcbridge
%{_prefix}/lib/vmware/rdpvcbridge/ftnlses3hv.so
%{_prefix}/lib/vmware/liburlFilterPlugin.so
%{_prefix}/lib/vmware/view/bin/vmware-urlFilter
%endif
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
%ifarch x86_64
%{_prefix}/lib/pcoip/vchan_plugins/librdpvcbridge.so
%{_prefix}/lib/vmware/rdpvcbridge/freerdp_plugins.conf
%endif
%{_prefix}/lib/pcoip/vchan_plugins/libvdpservice.so
%{_prefix}/lib/vmware/libpcoip_client.so
%ifarch armv7hl
%{_prefix}/lib/vmware/libpcoip_client_neon.so
%endif
%{_prefix}/lib/vmware/view/client/vmware-remotemks
%{_prefix}/lib/vmware/view/vdpService/libmksvchanclient.so
%{_prefix}/lib/vmware/view/vdpService/librdeSvc.so
%{_prefix}/lib/vmware/view/software
%{_prefix}/lib/vmware/view/vaapi2
%{_prefix}/lib/vmware/view/vdpau
%{_prefix}/lib/vmware/xkeymap

%files smartcard
%{_prefix}/lib/pcoip/vchan_plugins/libscredirvchanclient.so
%dir %{_prefix}/lib/vmware/view/pkcs11
%{_prefix}/lib/vmware/view/pkcs11/libopenscpkcs11.so

%files usb
%attr(0640,root,root) %config(noreplace) %{_sysconfdir}/vmware/usbarb.rules
%{_presetdir}/96-vmware-usbarbitrator.preset
%{_unitdir}/vmware-usbarbitrator.service
%{_bindir}/vmware-usbarbitrator
%dir %{_prefix}/lib/vmware/view/usb
%{_prefix}/lib/vmware/view/usb/libvmware-view-usbd.so
%{_prefix}/lib/vmware/view/vdpService/libusbRedirectionClient.so

%ifarch x86_64
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
%{_prefix}/lib/vmware/view/vdpService/libtsmmrClient.so

%files rtav
%{_prefix}/lib/pcoip/vchan_plugins/libviewMMDevRedir.so
%{_prefix}/lib/vmware/libx264.so.157.6

%files scannerclient
%config(noreplace) /etc/vmware/ftplugins.conf
%{_prefix}/lib/vmware/view/bin/ftscanhvd
%{_presetdir}/96-vmware-ftscanhvd.preset
%{_unitdir}/vmware-ftscanhvd.service

%files serialportclient
%attr(0644,root,root) %config(noreplace) %ghost %{_sysconfdir}/ftsprhv.db
%{_prefix}/lib/vmware/view/bin/ftsprhvd
%{_presetdir}/96-vmware-ftsprhvd.preset
%{_unitdir}/vmware-ftsprhvd.service

%files tsdr
%{_prefix}/lib/vmware/view/vdpService/libtsdrClient.so
%endif

%changelog
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
