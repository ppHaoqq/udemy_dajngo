from django.db import models

# Create your models here.
class BookModel(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    memo = models.TextField(max_length=400)
    def __str__(self):
        return self.title