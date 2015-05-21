from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rating = models.FloatField()

    def __str__(self):
        return self.name


class Projection(models.Model):
    movie = models.ForeignKey(Movie)
    _2D = 1
    _3D = 2
    _4DX = 3
    TYPES = (
        (_2D, '2D'),
        (_3D, '3D'),
        (_4DX, '4DX'),
    )

    type = models.PositiveSmallIntegerField(
        choices=TYPES,
        default=_2D
    )

    date = models.DateField()
    time = models.TimeField()
    hall = models.PositiveSmallIntegerField()

    def __str__(self):
        return ("{} {} {}".format(
        self.movie.name, self.type, self.time))


class Reservation(models.Model):
    username = models.CharField(max_length=64)
    projection = models.ForeignKey(Projection)
    row = models.PositiveSmallIntegerField()
    col = models.PositiveSmallIntegerField()

    def __str__(self):
        return ("{} {} {}".format(self.username, self.row, self.col))
