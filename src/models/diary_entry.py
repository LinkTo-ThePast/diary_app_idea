from django.db import models

class Diary_Entry(models.Model):
  entry_title = models.CharField(max_length=50)
  entry_text = models.CharField(max_length=500)
