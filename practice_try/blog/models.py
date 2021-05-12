from django.db import models

# Create your models here.
class Post(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=12, default='')

    # def __str__(self):
    #     return self.content


