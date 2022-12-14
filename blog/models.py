from django.db import models


class Blogs(models.Model):
    title = models.CharField(max_length=75)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
