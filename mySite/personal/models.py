from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    body = models.TextField()
    signature = models.CharField(max_length=100)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    