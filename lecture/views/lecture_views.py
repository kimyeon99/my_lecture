from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from ..models import Lecture

def show_detail(request):
    return HttpResponse('ㅋㅋㅋ')

def show_title(request):
    # lecture = get_object_or_404(Lecture, pk=lecture_id)
    template = loader.get_template('lecture/main.html')
    lecture_list = Lecture.objects.all()
    context = {'lecture_list':lecture_list}
    # return HttpResponse(template.render(context, request))
    return render(request, 'lecture/main.html', context)

def showDetail(self):
    print(self.age, self.category, self.name, self.totalCredits, self.time, self.room, self.professor, self.campus,
          self.note)

def showTitle(self):
    print(self.age, self.category, self.name, self.totalCredits)
