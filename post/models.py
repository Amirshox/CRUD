from django.contrib.auth.models import User
from django.urls import reverse

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='%Y/%m/%d/')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])