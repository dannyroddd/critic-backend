from django.db import models

# Create your models here.

class Critic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    food = models.TextField()
    overall = models.TextField()

    def __str__(self):
        return self.title