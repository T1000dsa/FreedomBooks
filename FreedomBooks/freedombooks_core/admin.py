from django.contrib import admin, messages
from freedombooks_core.models import BookModel, TagsModel
import os
import FreedomBooks.settings as sett
import chardet

@admin.register(BookModel)
class NewAdmin(admin.ModelAdmin):
    fields = ['title', 'slug','text_hook']
    filter_horizontal = ['tags']
    prepopulated_fields = {'slug':('title', )}
    list_display = ('title', 'time_create','text_hook')
    list_display_links =  ('title',)
    list_editable = ('text_hook',)

    ordering = ['id']
    list_per_page = 10
    search_fields = ['title']
    
"""
    @admin.display(description='brief info', ordering='content')
    def brief(self, info:BookModel):
        obj = info
        if obj.text_hook:
            adress = os.path.join(sett.MEDIA_ROOT, str(obj.text_hook.file))
            with open(adress, 'rb') as file:
                detector = chardet.universaldetector.UniversalDetector()
                for line in file:
                    detector.feed(line)
                    if detector.done:
                        break
                detector.close()
            encod = detector.result['encoding']

            with open(adress, encoding=encod) as file:
                text_view = file.read()
            return f'Length of the book in bytes {len(text_view)}b -- {round(len(text_view)/1024, 3)}kb -- {round(len(text_view)/1024**2, 3)}mb'
        else:
            return 'No text'
"""


#admin.site.register(Worker, WorkerAdmin)
# Register your models here.
