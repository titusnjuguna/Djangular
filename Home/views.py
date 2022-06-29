from multiprocessing import context
from django.shortcuts import render
from django.template import RequestContext,loader
from django.http import HttpResponse
def my_view(request):
    resp =  request.get('https://api.nytimes.com/svc/archive/v1/1995/7.json')
    articles = resp.json()
    template = loader.get_template('admin/index.html')
    context = RequestContext()
   

    return render(request,{'articles': articles})

