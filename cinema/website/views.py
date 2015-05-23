from django.shortcuts import render, get_object_or_404
from .models import Movie, Projection, Reservation


def index(request):

    movies = Movie.objects.all()
    projections = [Projection.objects.filter(movie_id=y.id) for y in movies]
    return render(request, "index.html", locals())

def movies(request):
    movies = Movie.objects.all()
    return render(request, "movies.html", locals())


def projections(request):
    pass


def reservations(request):
    pass

def show_projection(request, projection_id):
    pr_id = request.GET["projection_id"]

#    projection = Projection.objects.get(id=pr_id)
    projection = get_object_or_404(Projection, id=pr_id)

    return render(request, "show_projection.html", locals())
