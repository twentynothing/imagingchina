
from django.shortcuts import render_to_response

def index(request):
    'Display map'
    return render_to_response('changsha/index.html', {
    })
