# Create your views here.

from django.http import HttpResponse,HttpRequest
import datetime

#Vista che permette di ritonare la data e l'ora

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
