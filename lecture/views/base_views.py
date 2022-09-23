from django.shortcuts import render


def index(request):
    # page = request.GET.get('page', '1')

    return render(request, 'lecture/main.html')