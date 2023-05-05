from django.db import models
from django.contrib.auth.models import User

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
    email = models.EmailField(verbose_name="e-mail", null=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name="author",
        blank=True,
    )

    def __str__(self):
        return self.first_name

    @property
    def get_user(self):
        if hasattr(self, "user"):
            return self.user
        return None


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        "exercises.Author", on_delete=models.CASCADE, related_name="exercises"
    )
    classification = models.ForeignKey(
        "exercises.Classification",
        on_delete=models.CASCADE,
        related_name="exercises",
        null=True,
    )
    publisher = models.ForeignKey(
        "exercises.Publisher",
        on_delete=models.CASCADE,
        related_name="exercises",
        null=True,
    )

    def __str__(self):
        return self.title
