VMware Horizon Client for Linux RPM package for Fedora
======================================================

by Dominik Mierzejewski

Last-Updated: Wed 23 Oct 2024

Disclaimer
----------
VMware doesn't support running the Horizon Client for Linux on Fedora, only on
RHEL 8.10 and 9.4.
VMware Horizon Client EULA does not permit redistribution of their binaries, so
this package exists as spec file, support files and patches only. Help with
obtaining permission from Broadcom to distribute binaries is welcome.

Building
--------
```
$ git clone https://gitlab.com/greysector/rpms/vmware-horizon-client.git
$ cd vmware-horizon-client
$ spectool -g vmware-horizon-client.spec
$ fedpkg --release f40 srpm
$ mock -r fedora-40-x86_64 vmware-horizon-client-2406.8.13.0.9995429239-3.fc40.src.rpm
```

Dependencies
------------
The package unbundles several included libraries and uses system versions
instead:
* cairomm
* curl
* libpng
* openssl
* zlib
* vulkan-loader

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
