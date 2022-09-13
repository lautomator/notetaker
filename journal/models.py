from django.db import models

class Note(models.Model):
    note_date = models.DateField("Date")
    note_symbol = models.CharField("Symbol", max_length=6, null=True)
    note_text = models.TextField("Note", null=True)
    note_action = models.BooleanField("Action Taken", default=False)
    note_archive = models.BooleanField("Archive", default=False)

    @property
    def note_slug(self):
        return self.note_symbol + '-' + str(self.note_date)

    def __str__(self):
        return self.note_symbol + '-' + str(self.note_date)