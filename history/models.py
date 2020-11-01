from django.db import models

# Create your models here.

class History(models.Model):
    user = models.ForiegnKey(custom User, ondelete=models.CASCADE)
    heart_beat_rate = models.BigAutoField(max_length=3)
    eye_blink_rate = models.BigAutoField()
    emotion_speech_rate = models.BigAutoField()