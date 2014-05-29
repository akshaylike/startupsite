from django.db import models

class StartupDetails(models.Model):
  name = models.CharField(max_length=30)
  short_desc = models.CharField(max_length=100)
  votes = models.IntegerField(default=0)
  funding_amount = models.IntegerField(default=0)
  logo = models.ImageField(upload_to='startup_logos',blank=True)

  def __unicode__(self):
    return self.name

class Comment(models.Model):
  name = models.CharField(max_length=30)
  text = models.CharField(max_length=100)
  startup = models.ForeignKey(StartupDetails)
  created_on = models.DateTimeField(auto_now_add=True)
  
  def __unicode__(self):
    return self.text
