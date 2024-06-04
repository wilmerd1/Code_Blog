from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.utils import timezone
from django.utils.text import slugify


class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True)
    titulo= models.CharField(max_length=120)
    subtitulo = models.CharField(max_length=1000, null=True)
    comentario = models.TextField()
    fecha_publicacion = models.DateTimeField(default= timezone.now)
    pub_date_modified = models.DateTimeField('fecha modificacion', auto_now=True)
    etiqueta = TaggableManager()
    imagen = models.ImageField(null=True) 
    slug = models.SlugField(null=True,blank=True)
    
    def __str__(self) -> str:
        return self.titulo
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.titulo)
        super(Post,self).save(*args, **kwargs)
    
    
class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars', null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.user} - {self.imagen}"