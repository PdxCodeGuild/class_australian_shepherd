from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Movie

def homepage(request):
    all_movie = Movie.objects.all()
    context = {
        'all_movies': all_movie
    }
    return render(request, 'movie_app/home.html', context)


def new_movie(request):
    # print(request.POST)
    # print(request.POST['name'])

    name = request.POST['name']
    director = request.POST['director']
    release_date = request.POST['release_date']
    in_theatres = bool(request.POST['in_theatres'])
    genre = request.POST['genre']
    
    movie_model = Movie(name=name, director=director, release_date=release_date, in_theatres=in_theatres, genre=genre)
    movie_model.save()

    return redirect('movie_app:homepage')


def edit_movie(request, id):
    # print(request, id, '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    movie_obj = get_object_or_404(Movie, id=id)

    movie_obj.in_theatres = not movie_obj.in_theatres
    movie_obj.save()
    return redirect('movie_app:homepage')

def delete_movie(request, id):
    movie_obj = get_object_or_404(Movie, id=id)
    movie_obj.delete()

    return redirect('movie_app:homepage')
