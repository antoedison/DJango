from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    phone = models.BigIntegerField(null=True)
    joined_date = models.DateField(null = True)

    def __str__(self):
        return f'{self.fname} {self.lname}'