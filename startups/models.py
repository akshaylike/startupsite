from django.db import models

class StartupDetails(models.Model):
  name = models.CharField(max_length=30)
  votes = models.IntegerField(default=0)
