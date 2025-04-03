# bookstore/models.py
from django.db import models

class Author(models.Model):
    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Table Number"

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"

class Publisher(models.Model):
    Publisher_Name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Status"

    def __str__(self):
        return self.Publisher_Name

class Topic(models.Model):
    Topic_Name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Accepted/Not"

    def __str__(self):
        return self.Topic_Name

class Book(models.Model):
    Id = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=13, unique=True)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    Topics = models.ManyToManyField(Topic)

    def __str__(self):
       return self.Id