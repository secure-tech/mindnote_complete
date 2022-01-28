from django.db import models
from .validators import *
# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=100,validators=[validate_no_hash])
    content = models.TextField(validators=[validate_no_hash])
    feeling = models.CharField(max_length=80,validators=[validate_no_numbers])
    score = models.IntegerField(validators=[validate_score])
    dt_created = models.DateTimeField(verbose_name="Date Created")

    def __str__(self) -> str:
        return self.title