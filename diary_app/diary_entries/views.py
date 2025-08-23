from django.http import HttpResponse

def index(request):
  return HttpResponse("Hola, estás actualmente en el página de entradas de tu diario.")