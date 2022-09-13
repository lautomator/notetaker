from django.urls import path
from . import views

urlpatterns = [
    # /journal/ or /
    path('', views.index, name='index'),
    # /journal/CRK-2022-09-07/
    path('journal/<slug:note_slug>/', views.a_note, name='note'),

    # get all note based on a symbol or based on the date or both
]