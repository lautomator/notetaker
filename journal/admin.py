from django.contrib import admin
from .models import Note

class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'note_date',
        'note_symbol',
        'note_text',
        'note_action',
        'note_archive'
    )

admin.site.register(Note, NoteAdmin)

