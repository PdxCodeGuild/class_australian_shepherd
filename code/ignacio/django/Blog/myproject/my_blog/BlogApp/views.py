from django.shortcuts import render

def home(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'BlogApp/home.html', context)