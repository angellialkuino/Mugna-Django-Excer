from django.db import models

# Create your models here.

class Classification(models.Model):
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(verbose_name="e-mail")

    def __str__(self):
        return self.first_name

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey("exercises.Author", on_delete=models.CASCADE, related_name="exercises")
    classification = models.ForeignKey("exercises.Classification", on_delete=models.CASCADE, related_name="exercises")
    publisher = models.ForeignKey("exercises.Publisher", on_delete=models.CASCADE, related_name="exercises")

    def __str__(self):
        return self.title