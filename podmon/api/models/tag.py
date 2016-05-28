from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True)

    def __str__(self):
        return "Tag: {}".format(self.name)
