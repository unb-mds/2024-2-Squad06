from django.http import JsonResponse

def example_view(request):
    return JsonResponse({"message": "Hello from Django!"})
