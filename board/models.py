from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    update_date = models.DateTimeField(auto_now=True) #현재시각

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]