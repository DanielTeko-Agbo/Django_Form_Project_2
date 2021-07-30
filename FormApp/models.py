from django.db import models

GENDER_CHOICES = [
    ('M','Male'),
    ('F','Female')
]

class Form(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=15, default='Male')
    car = models.CharField(max_length=30)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.car