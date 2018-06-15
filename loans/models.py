from django.db import models


class LoanRequest(models.Model):
    GENDERS = (('M', 'Male'), ('F', 'Female'))

    name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    dni = models.IntegerField()
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=GENDERS)
    amount = models.FloatField()
    approved = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
