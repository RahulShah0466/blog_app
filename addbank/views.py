from django.shortcuts import render
from .models import BankDetail
from .forms import BankEntry


def bank(request):
    fm=BankEntry()
    return render(request,'home.html', {'form':fm})
    



