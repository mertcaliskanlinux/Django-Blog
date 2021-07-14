from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = RichTextField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='images/', null=True )

    class Meta:
        ordering = ['-date']


    def __str__(self):
        return self.title