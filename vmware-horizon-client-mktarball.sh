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
yymm=2006
version=8.0.0
build=16522670
s4br_ver=11.0.0.614
s4br_bld=16422350
cart=CART21FQ2
# https://my.vmware.com/en/web/vmware/downloads/info/slug/desktop_end_user_computing/vmware_horizon_clients/2006
url=https://download3.vmware.com/software/view/viewclients/${cart}/${name}-${yymm}-${version}-${build}.tar.gz
pushd "$tmp"
curl ${url} | tar xzf -
pushd ${name}-${yymm}-${version}-${build}

install -dm0755 {armv7hl,x86_64}/usr

pushd ARM/armhf
for f in \
  VMware-Horizon-Client-${yymm}-${version}-${build}.armhf.tar.gz \
  VMware-Horizon-PCoIP-${yymm}-${version}-${build}.armhf.tar.gz \
  VMware-Horizon-USB-${yymm}-${version}-${build}.armhf.tar.gz \
; do
  tar xzf ${f} -C ${tmp}/${name}-${yymm}-${version}-${build}/armv7hl/usr --strip-components=1
done
popd
pushd x64
for f in \
  VMware-Horizon-Client-${yymm}-${version}-${build}.x86_64.tar.gz \
  VMware-Horizon-PCoIP-${yymm}-${version}-${build}.x64.tar.gz \
  VMware-Horizon-USB-${yymm}-${version}-${build}.x64.tar.gz \
  VMware-Horizon-html5mmr-${yymm}-${version}-${build}.x64.tar.gz \
  VMware-Horizon-integratedPrinting-${yymm}-${version}-${build}.x64.tar.gz \
  VMware-Horizon-scannerClient-${yymm}-${version}-${build}.x64.tar.gz \
  VMware-Horizon-serialportClient-${yymm}-${version}-${build}.x64.tar.gz \
; do
  tar xzf ${f} -C ${tmp}/${name}-${yymm}-${version}-${build}/x86_64/usr --strip-components=1
done
popd

for target in armv7hl x86_64 ; do
pushd ${target}
install -dm0755 etc/teradici
install -dm0755 etc/vmware{/udpProxy,/vdp/host_overlay_plugins,-vix}
install -dm0755 usr/bin
install -dm0755 usr/lib/vmware/view/pkcs11
install -dm0755 usr/share/doc
install -dm0755 var/log/vmware

mv usr/{doc,share/doc/vmware-horizon-client}
mv usr/lib{,/vmware}/libpcoip_client.so

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
  usr/lib/vmware/libx264.so.157.5 \
  usr/lib/vmware/rdpvcbridge/tprdp.so \
  usr/lib/vmware/view/crtbora \
  usr/lib/vmware/view/integratedPrinting/{integrated-printing-setup.sh,README} \
  usr/lib/vmware/view/{software,vaapi{,2},vdpau} \
  usr/patches \
  usr/README* \

echo 'BINDIR="/usr/bin"' > etc/vmware/bootstrap
echo 'BINDIR="/usr/bin"' > etc/vmware-vix/bootstrap
echo "/usr/lib/pcoip/vchan_plugins/libvdpservice.so" > etc/vmware/vdp/host_overlay_plugins/config

popd
done

pushd armv7hl
mv usr/lib{,/vmware}/libpcoip_client_neon.so
popd

pushd x86_64
mv usr/lib{,/vmware}/libcoreavc_sdk.so
mv {usr/lib/vmware/view/integratedPrinting/prlinuxcupsppd,usr/bin/}
mv usr/vmware/ftplugins.conf etc/vmware
rm -rf usr/vmware
pushd usr/lib/vmware/view/html5mmr
find . -type f | xargs chmod 644
chmod 0755 \
  HTML5VideoPlayer \
  chrome-sandbox \
  {,swiftshader/}lib*.so \

popd
install -dm0755 usr/lib/vmware/mediaprovider
tar xzf ../SkypeForBusiness\ Redirection/VMware-Horizon-Media-Provider-${s4br_ver}-${s4br_bld}.tar.gz\
  -C usr/lib/vmware/mediaprovider\
  --strip-components=2\
  VMware-Horizon-Media-Provider-${s4br_ver}-${s4br_bld}/lin64/\*.so

popd
rm -rf ARM i386 'Printer Redirection' 'SkypeForBusiness Redirection' x64
popd
mv ${name}-${yymm}-${version}-${build} vmware-horizon-client-${yymm}-${version}-${build}
tar -c --use-compress-program=zstdmt \
  -f ${pwd}/vmware-horizon-client-${yymm}-${version}-${build}.tar.zstd \
  vmware-horizon-client-${yymm}-${version}-${build}
popd
