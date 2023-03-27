from django.db import models
from  django.db import models

class songpopularity(models.Model):
    Highest_Charting_Position =models.IntegerField()
    Number_of_Times_Charted =models.IntegerField()
    Artist_Followers =models.IntegerField()
    Genre =models.IntegerField()
    Danceability =models.IntegerField()
    Energy =models.IntegerField()
    Loudness =models.IntegerField()
    Valence =models.IntegerField()
    Duration =models.IntegerField()
    Tempo =models.IntegerField()
    Liveness =models.IntegerField()
    Acousticness =models.IntegerField()
    Speechiness =models.IntegerField()

def __int__(self):
    return self.age