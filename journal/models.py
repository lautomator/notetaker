from django.db import models

class Note(models.Model):
    note_date = models.DateField("Date")
    note_symbol = models.CharField("Symbol", max_length=6, null=True)
    note_text = models.TextField("Note", null=True)
    note_action = models.BooleanField("Action Taken", default=False)
    note_archive = models.BooleanField("Archive", default=False)

    def __str__(self):
        return 'Journaled ' + self.note_symbol
