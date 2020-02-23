from django.shortcuts import render

# Create your views here.
def contract(request):
    return render(request, 'registration/login.html')

def addContract(request):
    return render(request, 'registration/login.html')

def addProperty(request):
    return render(request, 'registration/login.html')
