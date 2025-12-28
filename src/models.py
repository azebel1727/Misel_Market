from django.db import models

class ArtItem(models.Model):
    title = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.CharField(max_length=500, default="https://via.placeholder.com/150")
    status = models.CharField(max_length=20, default="Available")

    def __str__(self):
        return self.title