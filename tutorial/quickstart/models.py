from django.db import models
from pkg_resources import empty_provider

# Create your models here.
class signup(models.Model):
    emailid=models.EmailField(max_length=200,null=True)
    password=models.CharField(max_length=100)

    class Meta:
        db_table="signup"