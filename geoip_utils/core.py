try:
    from django.contrib.gis.geoip import GeoIP
except ImportError:
    from django.contrib.gis.utils import GeoIP

from django.utils.functional import LazyObject

from .utils import get_ip_of_request
from .settings import CACHE_METHOD


class GeoIPHandler(LazyObject):

    def _setup(self):
        self._wrapped = GeoIP(cache=self.cache_method)

    @property
    def cache_method(self):
        if CACHE_METHOD == 'memory':
            return GeoIP.GEOIP_MEMORY_CACHE
        elif CACHE_METHOD == 'check':
            return GeoIP.GEOIP_CHECK_CACHE
        elif CACHE_METHOD == 'index':
           return GeoIP.GEOIP_INDEX_CACHE
        elif CACHE_METHOD == 'mmap':
           return GeoIP.GEOIP_MMAP_CACHE
        else:
           return GeoIP.GEOIP_STANDARD

geoip = GeoIPHandler()


def get_country(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.country(ip)


def get_city(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.city(ip)


def get_lat_lon(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.lat_lon(ip)


def get_country_code(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.country_code(ip)


def get_country_name(request):
    ip = get_ip_of_request(request)
    if ip:
        return geoip.country_name(ip)
