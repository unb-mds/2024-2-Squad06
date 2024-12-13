from django.utils.deprecation import MiddlewareMixin

class ExampleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print("Request intercepted by middleware.")
