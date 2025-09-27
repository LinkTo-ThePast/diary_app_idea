from django.db import models
from django.db import models

# Create your models here.

class Diary_Entry(models.Model): 
  entry_field = models.CharField(max_length=2500)
  published_date = models.DateTimeField("date published")
  emotion_descriptors = models.ForeignKey(Emotions) 

class Emotions(models.Model):
  
  EMOTIONS = {
    "happiness",
    "sadness",
    "anger",
    "fear",
    "surprise",
    "disgust"
  }
  
  emotion_name = models.CharField(max_length=25, choices=EMOTIONS)
  emotion_description = models.CharField(max_length=100)
  emotion_value = models.DecimalField(max_digits=1, decimal_places=0)

  
