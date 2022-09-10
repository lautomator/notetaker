from django.shortcuts import render
from journal.models import Note


def index(request):
    current_notes = Note.objects.all()[:10]

    context = {'current_notes': current_notes}
    return render(request, 'journal/index.html', context)
