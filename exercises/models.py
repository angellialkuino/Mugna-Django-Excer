from django.db import models

# Create your models here.

class Classification(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("exercises.Author", on_delete=models.CASCADE, related_name="exercises")
    classification = models.ForeignKey("exercises.Classification", on_delete=models.CASCADE, related_name="exercises")

    def __str__(self):
        return self.title