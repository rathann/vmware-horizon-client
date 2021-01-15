VMware Horizon Client for Linux RPM package for Fedora
======================================================

by Dominik Mierzejewski

Last-Updated: Thu 14 Jan 2021

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
$ git clone https://gitlab.com/greysector/vmware-horizon-client.git
$ cd vmware-horizon-client
$ fedpkg srpm
$ mock -r fedora-33-x86_64-rpmfusion_free vmware-horizon-client-2006.8.0.0.16522670-4.fc33.src.rpm
```

Dependencies
------------
The package unbundles several included libraries and uses system versions
instead:
* cairomm
* libavcodec
* libavutil
* libffi
* libjpeg
* libpcre
* libpng-1.2
* libsigc++
* libx264

Further unbundling will be possible once VMware builds their binaries with
glibmm >= 2.46. See https://gitlab.gnome.org/GNOME/glibmm/-/issues/32 .

As a result, the PCoIP support package depends on FFmpeg from RPM Fusion Free
repository and the Real-Time Audio Video support package depends on x264 from
the same repository. The Multimedia Redirection subpackage depends on the
obsolete gstreamer-0.10 packages, which are provided by the RPM Fusion Free
tainted repo. VMware is supposedly planning to migrate to GStreamer 1.x:
https://communities.vmware.com/t5/Horizon-for-Linux/Horizon-Client-for-Linux-depends-on-obsolete-gstreamer-0-10/m-p/2309349/highlight/true#M469 .

See https://rpmfusion.org/Configuration for information on how to configure RPM
Fusion repositories on your machine.

Known issues
------------
Untested features:
* HTML5 Multimedia Redirection
* Integrated Printing
* Scanner Redirection
* Serial Port Redirection
* Smartcard support
* USB Redirection
* Virtualization Pack for Skype for Business
