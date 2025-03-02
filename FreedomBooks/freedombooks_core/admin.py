from django.contrib import admin, messages
from freedombooks_core.models import BookModel, TagsModel, TextModel


@admin.register(BookModel)
class NewAdmin(admin.ModelAdmin):
    fields = ['title', 'slug']
    filter_horizontal = ['tags']
    prepopulated_fields = {'slug':('title', )}
    list_display = ('title', 'time_create', 'brief')
    list_display_links =  ('title',)
    ordering = ['id']
    list_per_page = 10
    search_fields = ['title']

    @admin.display(description='brief info', ordering='content')
    def brief(self, info:BookModel):
        if info.text:
            return f'Length of the book in bytes {len(info.text.text)}b -- {round(len(info.text.text)/1024, 3)}kb -- {round(len(info.text.text)/1024**2, 3)}mb'
        else:
            return 'No text'

@admin.register(TextModel)
class NewText(admin.ModelAdmin):
    fields = ['id']
    list_display = ('id', 'brief')
    list_display_links =  ('id',)
    ordering = ['id']
    list_per_page = 5


    @admin.display(description='brief info', ordering='text')
    def brief(self, info:TextModel):
        if info.text:
            return f'Length of the book in bytes {len(info.text.text)}b -- {round(len(info.text.text)/1024, 3)}kb -- {round(len(info.text.text)/1024**2, 3)}mb'
        else:
            return 'No text'
    
#admin.site.register(Worker, WorkerAdmin)
# Register your models here.
