from django.shortcuts import render
from .models import Movie, Projection, Reservation


def index(request):

    movies = Movie.objects.all()
    projections = [Projection.objects.filter(movie_id=y.id) for y in movies]
    print(projections)
    return render(request, "index.html", locals())
