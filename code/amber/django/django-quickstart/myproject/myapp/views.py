from django.shortcuts import render

def myview(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'myapp/mytemplate.html', context)
