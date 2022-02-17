VMware Horizon Client for Linux RPM package for Fedora
======================================================

by Dominik Mierzejewski

Last-Updated: Thu 02 Dec 2021

Disclaimer
----------
VMware doesn't support running the Horizon Client for Linux on Fedora, only on
RHEL 7.7+ and 8.0+.
VMware Horizon Client EULA does not permit redistribution of their binaries, so
this package exists as spec file, support files and patches only. Help with
obtaining permission from VMware to distribute binaries is welcome.

Building
--------
```
$ git clone https://gitlab.com/greysector/rpms/vmware-horizon-client.git
$ cd vmware-horizon-client
$ spectool -g vmware-horizon-client.spec
$ fedpkg --release f35 srpm
$ mock -r fedora-35-x86_64-rpmfusion_free vmware-horizon-client-2111.8.4.0.18957622-2.fc35.src.rpm
```

Dependencies
------------
The package unbundles several included libraries and uses system versions
instead:
* cairomm
* libavcodec
* libavutil
* libffi
* libpcre
* libpng
* libsigc++
* libx264
* libXss
* zlib

Further unbundling will be possible once VMware builds their binaries with
glibmm >= 2.46. See https://gitlab.gnome.org/GNOME/glibmm/-/issues/32 .

As a result, the PCoIP support package depends on FFmpeg from RPM Fusion Free
repository and the Real-Time Audio Video support package depends on x264 from
the same repository.

See https://rpmfusion.org/Configuration for information on how to configure RPM
Fusion repositories on your machine.

Known issues
------------
Untested features:
* HTML5 Multimedia Redirection
* Integrated Printing
* Media Optimization for Microsoft Teams
* Scanner Redirection
* Serial Port Redirection
* Smartcard support
* USB Redirection
* Virtualization Pack for Skype for Business
