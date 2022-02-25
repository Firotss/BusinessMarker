from django.db import models

# Create your models here.
class Updates(models.Model):
    comment = models.CharField(max_length=200)
    date = models.CharField(max_length=200)

    def __str__(self) -> str:
        return "{} - {}".format(self.date, self.comment)