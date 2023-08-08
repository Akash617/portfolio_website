from django import forms
import re

class Email_Form(forms.Form):
    email = forms.CharField(max_length=30, help_text="Enter your email address")

    def clean_email(self):
        data = self.cleaned_data['email']

        # Pattern for matching email names, one or more of (alphanumeric or .)
        email_name_pattern = re.compile("[\w.]+")

        # Pattern for matching domain names
        domain_pattern = re.compile("\w+([-.]\w+)*\.\w+([-.]\w+)*$")

        if data.count("@") != 1:
            raise ValueError('Invalid email - missing or too many @ symbols')

        data = data.split("@")

        if not email_name_pattern.match(data[0]):
            raise ValueError('Invalid email - email name (before the @) is invalid')

        if not domain_pattern.match(data[1]):
            raise ValueError('Invalid email - domain name (after the @) is invalid')

        data = "@".join(data)
        data = data.lower()

        return data



