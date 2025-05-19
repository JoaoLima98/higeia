from django.db import models

# Create your models here.

class Wing(models.Model):
  name = models.CharField(max_length=25, unique=True)
  code = models.CharField(max_length=30, unique=True)
  number_of_beds = models.IntegerField()


  def clean(self):
    if self.number_of_beds < 1:
      raise ValueError("Deve haver pelo menos 1 leito")
  
  def save(self, *args, **kwargs):
    self.clean()
    super().save(*args, **kwargs)

  def __str__(self):
    return f"{self.name} ({self.code})"