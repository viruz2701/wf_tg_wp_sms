/radius incoming
set accept=yes

/radius
add service=hotspot address=10.20.30.40 secret=YourRadiusSecret \
    authentication-port=1812 accounting-port=1813 \
    timeout=10s enabled=yes