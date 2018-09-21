from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class AccountManager(models.Manager):
    def email_exist(self, email):
        users = User.objects.filter(email=email)
        return True if users else False
 


class Account(User):
    accounts=AccountManager()
    class Meta:
        proxy = True
    
    
