/ip hotspot profile
add name="WiFiAuth" hotspot-address=192.168.88.1 dns-name=hotspot.local \
    html-directory=hotspot login-by=mac-cookie,http-chap,http-pap \
    http-cookie-lifetime=1d rate-limit=1M/1M

/ip hotspot
add name=WiFiHotspot interface=wlan1 profile=WiFiAuth disabled=no

/ip hotspot walled-garden ip
add action=accept comment="Allow auth server" dst-address=<YOUR_VPS_IP> disabled=no
add action=accept comment="Allow Telegram" dst-address=149.154.160.0/20 disabled=no
add action=accept comment="Allow WhatsApp" dst-address=157.240.0.0/16 disabled=no

/ip hotspot user profile
add name="default" rate-limit=1M/1M shared-users=1

/radius
add service=hotspot address=<YOUR_VPS_IP> secret=<RADIUS_SECRET> \
    timeout=5s disabled=no