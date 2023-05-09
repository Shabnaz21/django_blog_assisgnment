from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    title = models.CharField(max_length= 200,null=True, blank=True)
    slug =models.SlugField(max_length= 150, unique=True, null=True, blank=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "catogries"

    def save(self, *args, **kwargs):
        self.slug =slugify(self.title)
        super().save(*args, **kwargs)
    

class Blog(models.Model):
    status = [
        ('draft','Draft'),
        ('publish', 'Publish')
        ]
        
    
    title = models.CharField(max_length= 200, help_text = "Enter Your Post Title Here",null=True, blank=True)
    slug =models.SlugField(max_length= 150, unique=True, null=True, blank=True)
    content = RichTextField(help_text = "Enter Your Content Here")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True, blank=True)
    post_status = models.CharField(max_length= 10, choices=status, default='draft')
    published = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['published']
        verbose_name_plural = "Blogs"
    
    def save(self, *args, **kwargs):
        self.slug =slugify(self.title)
        super().save(*args, **kwargs)
