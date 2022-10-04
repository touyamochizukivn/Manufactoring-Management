from django.shortcuts import render

from core.forms import *


def dashboard(request):
    return render(request, 'dashboard.html')

def component_add(request):
    if request.method == 'POST':
        form = ComponentAdd(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ComponentAdd()
    return render(request, 'component/add.html', {'form': form})

def supplier_add(request):
    if request.method == 'POST':
        form = SupplierAdd(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SupplierAdd()
    return render(request, 'supplier/add.html', {'form': form})
