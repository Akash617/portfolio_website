from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Email_Model
from .forms import Email_Form
from django.urls import reverse

# Create your views here.

def index(request):
    email_count = Email_Model.objects.count()

    context = {
        'email_count': email_count
    }

    return render(request, 'index.html', context=context)


def enter_email(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Email_Form(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            email = Email_Model()
            if email.is_email_unique(form.cleaned_data["email"]):
                email.email = form.cleaned_data["email"]
                email.save()
            else:
                raise ValueError('Invalid email - email already exists')

            # redirect to a new URL:
            return HttpResponseRedirect("/first_app")

    # If this is a GET (or any other method) create the default form.
    else:
        form = Email_Form()

    context = {
        'form': form,
    }

    return render(request, 'first_app/enter_email.html', context)
