from django.db import models
from django.conf import settings

# STAR_RATING = (
#    ('r1', '1Star'),
#    ('r2', '2Star'),
#    ('r3', '3Star'),
#    ('r4', '4Star'),
#    ('r5', '5Star')
# )


class Review(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    # rating = models.CharField(max_length=300, choices=STAR_RATING) 
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)