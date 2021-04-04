from django.http import HttpResponse
 
def index(request):
    return HttpResponse('<h2>welcome to victory city</h2')