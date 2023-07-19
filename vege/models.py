from django.db import models

# Create your models here.
class Receipe(models.Model): #models is a manager here
    receipe_name = models.CharField(max_length=50)
    receipe_description = models.TextField()
    receipe_image = models.ImageField(upload_to="Receipe_Image")
