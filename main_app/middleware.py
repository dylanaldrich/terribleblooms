from django.core.cache import cache
from django.http import HttpResponse
import time

class HttpResponseTooManyRequests(HttpResponse):
    status_code = 429

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = 100  # requests
        self.time_window = 60  # seconds

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            return self.get_response(request)

        client_ip = self.get_client_ip(request)
        cache_key = f'rate_limit_{client_ip}'

        # Get the list of request timestamps for this IP
        requests = cache.get(cache_key, [])
        now = time.time()

        # Filter out requests older than time_window
        requests = [req for req in requests if now - req < self.time_window]

        if len(requests) >= self.rate_limit:
            return HttpResponseTooManyRequests("Rate limit exceeded")

        # Add current request timestamp
        requests.append(now)
        cache.set(cache_key, requests, self.time_window)

        return self.get_response(request)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0]
        return request.META.get('REMOTE_ADDR')
