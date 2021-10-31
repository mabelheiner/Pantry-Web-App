from django.db import models

# Create your models here.

class breakfast_items(models.Model):
      content = models.TextField()

class lunch_items(models.Model):
      content = models.TextField()

class dinner_items(models.Model):
      content = models.TextField()

class desert_items(models.Model):
      content = models.TextField()

class snacks_items(models.Model):
      content = models.TextField()
