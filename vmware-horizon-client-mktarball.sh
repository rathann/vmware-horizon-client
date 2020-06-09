#!/bin/bash

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
name=vmware-view-client-linux
version=5.4.1
build=15988340
s4br_ver=11.0.0.613
s4br_bld=15574653
cart=CART21FQ1
# https://my.vmware.com/web/vmware/info?slug=desktop_end_user_computing/vmware_horizon_clients/5_0
url=https://download3.vmware.com/software/view/viewclients/${cart}/${name}-${version}-${build}.tar.gz
pushd "$tmp"
curl ${url} | tar xzf -
pushd ${name}-${version}-${build}

install -dm0755 usr

pushd x64
for f in \
  VMware-Horizon-Client-${version}-${build}.x86_64.tar.gz \
  VMware-Horizon-PCoIP-${version}-${build}.x64.tar.gz \
  VMware-Horizon-USB-${version}-${build}.x64.tar.gz \
  VMware-Horizon-html5mmr-${version}-${build}.x64.tar.gz \
  VMware-Horizon-integratedPrinting-${version}-${build}.x64.tar.gz \
  VMware-Horizon-scannerClient-${version}-${build}.x64.tar.gz \
  VMware-Horizon-serialportClient-${version}-${build}.x64.tar.gz \
; do
  tar xzf ${f} -C ${tmp}/${name}-${version}-${build}/usr --strip-components=1
done
popd

install -dm0755 etc/teradici
install -dm0755 etc/vmware{/udpProxy,/vdp/host_overlay_plugins,-vix}
install -dm0755 usr/bin
install -dm0755 usr/lib/vmware/mediaprovider
install -dm0755 usr/lib/vmware/view/pkcs11
install -dm0755 usr/share/doc
install -dm0755 var/log/vmware
tar xzf SkypeForBusiness\ Redirection/VMware-Horizon-Media-Provider-${s4br_ver}-${s4br_bld}.tar.gz\
  -C ${tmp}/${name}-${version}-${build}/usr/lib/vmware/mediaprovider\
  --strip-components=2\
  VMware-Horizon-Media-Provider-${s4br_ver}-${s4br_bld}/lin64/\*.so
rm -rf ARM i386 'Printer Redirection' 'SkypeForBusiness Redirection' x64

mv usr/{doc,share/doc/vmware-horizon-client}
mv usr/lib{,/vmware}/libcoreavc_sdk.so
mv usr/lib{,/vmware}/libpcoip_client.so
mv {usr/lib/vmware/view/integratedPrinting/prlinuxcupsppd,usr/bin/}
mv usr/vmware/ftplugins.conf etc/vmware

pushd usr/lib/vmware/view/html5mmr
find . -type f | xargs chmod 644
chmod 0755 \
  HTML5VideoPlayer \
  chrome-sandbox \
  {,swiftshader/}lib*.so \

popd

rm -rf \
  usr/debug \
  usr/init.d \
  usr/lib/vmware/gcc \
  usr/lib/vmware/libcairomm-1.0.so.1 \
  usr/lib/vmware/libffi.so.6 \
  usr/lib/vmware/libjpeg.so.62 \
  usr/lib/vmware/libpcre.so.1 \
  usr/lib/vmware/libpng12.so.0 \
  usr/lib/vmware/libsigc-2.0.so.0 \
  usr/lib/vmware/rdpvcbridge/tprdp.so \
  usr/lib/vmware/view/crtbora \
  usr/lib/vmware/view/integratedPrinting/{integrated-printing-setup.sh,README} \
  usr/lib/vmware/view/{software,vaapi{,2},vdpau} \
  usr/patches \
  usr/README* \
  usr/vmware \

chrpath -d usr/lib/vmware/view/bin/ftscanhvd
find  . -type f | xargs file | grep ELF | cut -d: -f1 | xargs -l execstack -q |\
  grep ^X | cut -d' ' -f2 | xargs -l execstack -c

echo 'BINDIR="/usr/bin"' > etc/vmware/bootstrap
echo 'BINDIR="/usr/bin"' > etc/vmware-vix/bootstrap
echo "/usr/lib/pcoip/vchan_plugins/libvdpservice.so" > etc/vmware/vdp/host_overlay_plugins/config

ln -s ../../lib64/libudev.so.1 usr/lib/vmware/libudev.so.0
ln -s ../../../../lib64/pkcs11/opensc-pkcs11.so usr/lib/vmware/view/pkcs11/libopenscpkcs11.so

popd
mv ${name}-${version}-${build} vmware-horizon-client-${version}.${build}
tar -c --use-compress-program=zstdmt \
  -f ${pwd}/vmware-horizon-client-${version}.${build}.tar.zstd \
  vmware-horizon-client-${version}.${build}
popd
