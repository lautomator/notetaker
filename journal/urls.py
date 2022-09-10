from django.urls import path
from . import views

urlpatterns = [
    # /journal/
    path('', views.index, name='index'),
    # /journal/20220910/ <year/month/day>
    # path('<slug:note_date>/', views.entry, name='entry'),
]