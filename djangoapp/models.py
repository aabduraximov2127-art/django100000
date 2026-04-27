from django.db import models
from django.utils.text import slugify
import uuid
# Create your models here.

class User(models.Model):
    ism=models.CharField(max_length=50,blank=False)
    familya=models.CharField(max_length=50,blank=False)
    yosh=models.PositiveIntegerField(default=15,blank=True)
    phon=models.CharField(max_length=15, null=True, blank=True)
    email=models.EmailField(max_length=100, null=True, blank=True)
    pitcture=models.ImageField(upload_to='images/',default='images/default.jpg',blank=True)
    slug=models.SlugField(blank=True,unique=True)
    
    
    def save(self,*args, **kwargs):
        if not self.slug:
            short_id = str(uuid.uuid4())[:5]
        self.slug = slugify(f"{self.ism}-{self.familya}-{short_id}")
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.ism} {self.familya}' 