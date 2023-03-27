from django.contrib.auth.models import AbstractUser
from django.db import models

from triple_choice.db.mixins import AuthorMixin, TimeStampMixin


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    REQUIRED_FIELDS = ['email', 'company_name', 'phone']

    def __str__(self):
        return self.username

