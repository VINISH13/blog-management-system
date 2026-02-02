from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    content = models.TextField()
    author = models.CharField(max_length=100)

    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




