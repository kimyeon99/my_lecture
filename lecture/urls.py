from django.urls import path

from . import views
from .views import lecture_views, base_views

app_name = 'lecture'

urlpatterns = [
    # path('showDetail/', views.show_detail, name='show_detail'),
    path('show/', lecture_views.show_detail, name='show_detail'),
    path('show/all', lecture_views.show_title, name='show_title'),
]