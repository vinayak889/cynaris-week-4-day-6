from django.http import JsonResponse, HttpResponse

def home(request):
    return HttpResponse("<h1>CI/CD Demo App</h1><p>Django is running inside Docker.</p>")

def health(request):
    return JsonResponse({"status": "ok", "service": "django-cicd-demo"})
