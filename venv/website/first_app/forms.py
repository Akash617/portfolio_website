from django import forms

class Email_Form(forms.Form):
    email = forms.CharField(max_length=30, help_text="Enter your email address")
