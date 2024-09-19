from django.db import models


# Create your models here.
class Posts(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/no_image.png')
    url = models.CharField(max_length=500, default="")
    date_posted = models.DateField(auto_now_add=True)