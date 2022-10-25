from django.db import models

# Create your models here.
class Projects(models.Model):

    title = models.CharField(max_length = 100, verbose_name = 'Title')
    descriptions = models.TextField(verbose_name = "Descriptions")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    image = models.ImageField(upload_to = "Portfolio")
    url = models.URLField(blank = True, null =True)
