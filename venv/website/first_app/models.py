from django.db import models
from django.urls import reverse

# Create your models here.

class Email_Model(models.Model):
    email = models.EmailField(max_length=30, help_text="Email address")

    def is_email_unique(self, input_email):
        duplicate_email = Email_Model.objects.filter(email=input_email)

        if not duplicate_email:
            return True
        return False


    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        """Returns the URL to access a particular instance of the model."""
        return reverse('model-detail-view', args=[str(self.id)])

