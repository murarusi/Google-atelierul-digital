from django.db import models

type = (("FULLTIME", "FULLTIME"), ("PART-TIME", "PART-TIME"), ("HIBRID", "HIBRID"))


# Create your models here.
class Jobs(models.Model):
    type = models.CharField(max_length=100, choices=type)
    title = models.CharField(max_length=150)
    url = models.CharField(max_length=100)
    description = models.TextField()
    how_to_apply = models.TextField()
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.title} - {self.description}"
