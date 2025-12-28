from django.db import models

class ArtItem(models.Model):
    title = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # src/models.py
    image = models.ImageField(upload_to='art_images/', null=True, blank=True) 
    status = models.CharField(max_length=20, default="Available")

    def __str__(self):
        return self.title