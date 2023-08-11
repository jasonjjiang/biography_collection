from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User


STATUS = (
  ('S', 'Started'),
  ('P', 'Paused'),
  ('F', 'Finished')
)

class Version(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__ (self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('versions_detail', kwargs={'pk': self.id})

# Create your models here.
class Biography(models.Model):
  name = models.CharField(max_length=100)
  title = models.CharField(max_length=100)
  author = models.TextField(max_length=250)
  # Add the M:M relationship
  versions = models.ManyToManyField(Version)
  # Add the foreign key linking to a user instance
  user = models.ForeignKey(User, on_delete=models.CASCADE)


  # Changing this instance method
  # does not impact the database, therefore
  # no makemigrations is necessary
  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'biography_id': self.id})

class Status(models.Model):
  date = models.DateField('Status Date')
  status = models.CharField(
    max_length=1,
    choices=STATUS,
    default=STATUS[0][0]
  )
  # Create a biography_id FK

  biography = models.ForeignKey(
    Biography,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_status_display()} on {self.date}"

  class Meta:
    ordering = ['-date']