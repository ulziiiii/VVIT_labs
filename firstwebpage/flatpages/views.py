from django.shortcuts import render

def home(request):
    return render(request, 'static_handler.html')




#from django.http import HttpResponse
#def home(request):
    #return HttpResponse(u'Hello, World!', content_type="text/plain")



