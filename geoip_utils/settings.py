from django.conf import settings

REQUEST_IP_RESOLVER = getattr(settings, "GEOIP_REQUEST_IP_RESOLVER",
                              "geoip_utils.utils.remote_addr_ip")

CACHE_METHOD = getattr(settings, "GEOIP_CACHE_METHOD", None)
if CACHE_METHOD is None:
    try:
        from django.contrib.gis.utils import GeoIP
    except ImportError:
        from django.contrib.gis.geoip import GeoIP
    CACHE_METHOD = GeoIP.GEOIP_STANDARD
