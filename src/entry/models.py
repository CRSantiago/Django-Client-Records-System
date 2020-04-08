from django.db import models
from django.urls import reverse

class Entry(models.Model):
    male = 'male'
    female = 'female'
    GENDER_CHOICES = [
        (male, 'male'),
        (female, 'female')
    ]


    FLORIDA = 'FL'
    COLORADO = 'CO'
    ARIZONA = 'AZ'

    STATE_CHOICES = [
        (FLORIDA, 'Florida'),
        (COLORADO, 'Colorado'),
        (ARIZONA, 'Arizona')
    ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    join_date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length = 10, choices=GENDER_CHOICES)
    D_O_B = models.DateField()
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    zipcode = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('entry:entry-detail', kwargs={'id':self.id})