from django.db import models
from django.utils import timezone

class Sheep(models.Model):
    name = models.CharField(max_length=100)
    earing = models.CharField(max_length=100, default="no_earring")
    birthdate = models.DateField(auto_now_add=timezone.now)
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    mother = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='children')

    def __str__(self):
        return self.name
    
class BirthEvent(models.Model):
    mother = models.ForeignKey(Sheep, on_delete=models.CASCADE, related_name='birth_events')
    date = models.DateField()
    notes = models.TextField(blank=True)
    lambs = models.ManyToManyField(Sheep, related_name='birth_event', blank=True)

    def __str__(self):
        return f"Birth by {self.mother.name} on {self.date}"
    
class Milk(models.Model):
    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
        related_name="milk"
    )
    date = models.DateField(auto_now_add=True)
    milk = models.DecimalField(max_digits=5, decimal_places=2, help_text="liter")
    
    def __str__(self):
        return f"{self.sheep.name} - {self.date} ({self.milk} liter)"
