from django.db import models
from django.db import models

# Create your models here.


class Emotions(models.Model):
  
  EMOTIONS_CUSTOM_CODE = [
    ("HP", "happines"),
    ("SN", "sadness"),
    ("AG", "anger"),
    ("FR", "fear"),
    ("SP", "surprise"),
    ("DG", "disgust")
  ]
  
  emotions_custom_code = models.CharField(max_length=2, choices=EMOTIONS_CUSTOM_CODE)
  emotion_name = models.CharField(max_length=25)
  emotion_description = models.CharField(max_length=100)
  

class Diary_Entry(models.Model): 
  entry_field = models.CharField(max_length=2500)
  published_date = models.DateTimeField("date published")
  emotion_descriptors = models.ManyToManyField(Emotions, db_table="diary_entry_emotions") 


  
