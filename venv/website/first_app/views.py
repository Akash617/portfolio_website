from django.shortcuts import render
from django.http import HttpResponse
from .models import Email_Model

# Create your views here.

def index(request):
    email_count = Email_Model.objects.count()

    context = {
        'email_count': email_count
    }

    return render(request, 'index.html', context=context)
