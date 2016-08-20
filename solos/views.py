from django.shortcuts import render
from django.views.generic import DetailView

from solos.models import Solo


def index(request):
    qs = []

    if request.GET.keys():
        qs = Solo.objects.all()

        if request.GET.get('instrument', None):
            qs = qs.filter(instrument=request.GET.get('instrument', None))

        if request.GET.get('artist', None):
            qs = qs.filter(artist=request.GET.get('artist', None))

    context = {
        'solos': qs
    }
    return render(request, 'solos/index.html', context)


# class SoloDetailView(DetailView):
#     model = Solo

def solo_detail(request, album, track, artist):
    context = {
        'solo': Solo.objects.get(slug=artist, track__slug=track, track__album__slug=album)
    }
    return render(request, 'solos/solo_detail.html', context)
