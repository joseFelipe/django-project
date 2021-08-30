from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def sobre(request):
    return render(request, 'pages/sobre.html')
