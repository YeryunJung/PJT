from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_POST
from .models import Movie, Genre
from django.http import JsonResponse
from django.shortcuts import get_object_or_404


# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies':movies,
    }
    return render(request, 'movies/index.html', context)


@require_POST
def movie_like(request, movie_pk):
    if request.user.is_authenticated:
        movie = Movie.objects.get(pk=movie_pk)
        user = request.user

        if movie.like_users.filter(pk=user.pk).exists():
            movie.like_users.remove(user)
            is_liked = False
        else:
            movie.like_users.add(user)
            is_liked = True
        context = {
            'is_liked': is_liked,
        }
        return JsonResponse(context)
    return redirect('acctouns:login')

@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)

@require_safe
def recommended(request):
    # 상위 3개 장르 추출
    G = Genre.objects.all()
    G_count = {i.name:0 for i in G}
    if request.user.is_authenticated:
        user = request.user
        movies = user.like_movies.all()
        for movie in movies:
            genre = movie.genres.all()
            for i in genre:
                G_count[i.name] += 1
        new_G = sorted(G_count.items(), key=lambda x: x[1], reverse=True)[:3]
        preferences = [Genre.objects.get(name=i[0]).id for i in new_G]

        movies = Movie.objects.filter(genres__id__in=preferences).order_by('-vote_average')
        movies = list(set(movies))[:10]

    return render(request, 'movies/recommended.html', {'movies': movies})