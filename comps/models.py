from django.db import models


class Comp(models.Model):

    class Meta:
        ordering = ['-end_date']

    name = models.CharField(max_length=254)
    size_range = models.TextField()
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    entries = models.DecimalField(max_digits=4, decimal_places=0)
    image_url = models.URLField(max_length=1024)
    image = models.ImageField(null=True, blank=True)
    end_date = models.DateField()

    def __str__(self):
        return self.name
