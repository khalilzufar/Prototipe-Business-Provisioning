from django.shortcuts import render

# Create your views here.
def datin(request):    
    return render(request, 'datin.html')

def hsi(request):    
    return render(request, 'dashboard/hsi.html')

def rekap(request):    
    return render(request, 'rekap.html')

