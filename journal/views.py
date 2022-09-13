from django.shortcuts import render
from journal.models import Note


def index(request):
    current_notes = Note.objects.all()[:10]

    context = {'current_notes': current_notes}
    return render(request, 'journal/index.html', context)


def a_note(request, note_slug):
    slug_split = note_slug.split('-')
    note_symbol = slug_split[0]
    note_date = slug_split[1] + '-' + slug_split[2] + '-' + slug_split[3]
    current_note = Note.objects.get(
        note_date=note_date,
        note_symbol=note_symbol
    )

    context = {'current_note': current_note}
    return render(request, 'journal/note.html', context)