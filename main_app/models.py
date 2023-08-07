from django.db import models

# Create your models here.
class Biography(models.Model):
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  author = models.TextField(max_length=250)

  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.name} ({self.id})'


