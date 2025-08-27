from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # AbstractUser already has: username, email, password, first_name, last_name, etc.
    # You can add extra fields if needed
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    is_driver = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)

    def __str__(self):
        return self.username or self.email
