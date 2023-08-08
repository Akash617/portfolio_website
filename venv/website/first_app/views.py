from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Email_Model
from .forms import Email_Form
from django.urls import reverse
from django.contrib import messages
import re

# Create your views here.

def index(request):
    email_count = Email_Model.objects.count()

    context = {
        'email_count': email_count
    }

    return render(request, 'index.html', context=context)


def validate_email(request, email):
    # Pattern for matching email names, one or more of (alphanumeric or .)
    email_name_pattern = re.compile("[\w.]+")

    # Pattern for matching domain names
    domain_pattern = re.compile("\w+([-.]\w+)*\.\w+([-.]\w+)*$")

    if email.count("@") != 1:
        messages.error(request, 'Invalid email - missing "@" or too many "@"')
        return ''

    email = email.split("@")

    if not email_name_pattern.match(email[0]):
        messages.error(request, 'Invalid email - email name (before the @) is invalid')
        return ''

    if not domain_pattern.match(email[1]):
        messages.error(request, 'Invalid email - domain name (after the @) is invalid')
        return ''

    email = "@".join(email)
    email = email.lower()

    return email


def enter_email(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = Email_Form(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            email = Email_Model()
            email_value = validate_email(request, form.cleaned_data["email"])

            if not email_value:
                return HttpResponseRedirect("/first_app/enter_email")

            if email.is_email_unique(email_value):
                email.email = email_value
                email.save()
            else:
                messages.error(request, 'Invalid email - email already exists')
                return HttpResponseRedirect("/first_app/enter_email")

            # redirect to a new URL:
            return HttpResponseRedirect("/first_app")

    # If this is a GET (or any other method) create the default form.
    else:
        form = Email_Form()

    context = {
        'form': form,
    }

    return render(request, 'first_app/enter_email.html', context)
