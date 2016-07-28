from django.shortcuts import render

from solos.models import Solo


def index(request):
    qs = []

    if request.GET.keys():
        qs = Solo.objects.all()

        if request.GET.get('instrument', None):
            qs = qs.filter(
                instrument=request.GET.get(
                    'instrument', None
                )
            )

        if request.GET.get('artist', None):
            qs = qs.filter(
                instrument=request.GET.get(
                    'artist', None
                )
            )

    context = {
        'solos': qs
    }
    return render(request, 'solos/index.html', context)
