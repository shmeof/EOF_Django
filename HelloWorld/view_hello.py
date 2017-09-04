from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    context_of_template          = {}
    context_of_template['hello'] = 'Hello World!dd'
    return render(request, 'hello.html', context_of_template)
