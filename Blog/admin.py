from django.contrib import admin
from .models import Post, Avatar
from django_summernote.admin import SummernoteModelAdmin

admin.site.site_title = "Blog"



class PostAdmin(SummernoteModelAdmin):
    list_display = ['autor', 'titulo', 'subtitulo', 'fecha_publicacion', 'pub_date_modified', 'slug']
    exclude = ['fecha_publicacion','autor',]
    summernote_fields = ('comentario',)

admin.site.register(Post,PostAdmin) 
admin.site.register(Avatar)
