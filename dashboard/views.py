from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from .models import Myuser
# Create your views here.


def datin(request):    
    return render(request, 'dashboard/datin.html')

def hsi(request):    
    return render(request, 'dashboard/hsi.html')

def rekap(request):    
    return render(request, 'dashboard/rekap.html')


def admin(request):  
    return render(request, 'dashboard/admin.html')

def test(request):  
    return render(request, 'dashboard/test.html')



def adashboard(request):
    users = Myuser.objects.all()
    context = {'users': users}
    return render(request, 'dashboard/adashboard.html', context)

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('adashboard')
    return render(request, 'dashboard/add_user.html')

def edit_user(request, id):
    user = Myuser.objects.get(id=id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.nohp = request.POST.get('nohp')
        user.save()
        return redirect('adashboard')
    context = {'user': user}
    return render(request, 'dashboard/edit_user.html', context)

def delete_user(request, id):
    user = get_object_or_404(Myuser, id=id)
    user.delete()
    return redirect('adashboard')