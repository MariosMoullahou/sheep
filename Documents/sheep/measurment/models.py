from django.db import models
from sheepfold.models import Sheep

class Measurment(models.Model):
    sheep = models.ForeignKey(
        Sheep,
        on_delete=models.CASCADE,
        related_name="measurements"
    )
    date = models.DateField(auto_now_add=True)
    milk = models.DecimalField(max_digits=5, decimal_places=2, help_text="liter")
    
    def __str__(self):
        return f"{self.sheep.name} - {self.date} ({self.milk} liter)"
