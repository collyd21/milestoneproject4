from django.db import models


class Comp(models.Model):

    class Meta:
        ordering = ['-date']

    name = models.CharField(max_length=254)
    size_range = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    entries = models.DecimalField(max_digits=4, decimal_places=0)
    image = models.ImageField(null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
