from django.db import models


class Movies(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rating = models.FloatField()


class Projections(models.Model):
    movie_id = models.ForeignKey(Movies)
    projection_type = models.CharField(max_length=3)
    projection_date = models.DateField()
    projection_time = models.TimeField()


class Reservations(models.Model):
    username = models.CharField(max_length=64)
    projection_id = models.ForeignKey(Projections)
    row = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()
