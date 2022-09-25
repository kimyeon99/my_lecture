from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render

from ..models import Lecture


def index(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    lecture_list = Lecture.objects.all()

    if kw:
        lecture_list = lecture_list.filter(
            Q(name__icontains=kw)
        ).distinct()
    paginator = Paginator(lecture_list, 100)
    page_obj = paginator.get_page(page)
    context = {'lecture_list': page_obj,
               'page': page,
               'kw': kw}

    return render(request, 'lecture/main.html', context)