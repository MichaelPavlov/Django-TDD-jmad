from django.shortcuts import render

from solos.models import Solo


def index(request):
    qs = Solo.objects.filter(instrument=request.GET.get('instrument', None))

    context = {
        'solos': qs
    }
    return render(request, 'solos/index.html', context)
