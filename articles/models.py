from django.db import models

class Article(models.Model):
    title = models.CharField(verbose_name="tytuł", max_length=100)
    headline = models.TextField(verbose_name="nagłówek")
    text = models.TextField(verbose_name="tekst")
    published_at = models.DateTimeField(verbose_name="data publikacji")
    image = models.ImageField(verbose_name="obraz", blank=True)

    categoryID = models.ManyToManyField('Category')
    AuthorID = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return "Article: " + self.title

    class Meta:
        ordering = ["title", "headline"]
        verbose_name = "Artykuł"


class Author(models.Model):
    firstName = models.CharField(verbose_name="Imię", max_length=100)
    lastName = models.CharField(verbose_name="Nazwisko", max_length=100)
    about = models.TextField(verbose_name="O", blank=True)
    image = models.ImageField(verbose_name="Zdjęcie", blank=True)

    def __str__(self):
        return "Autor: " + self.firstName + " " + self.lastName

    class Meta:
        ordering = ["firstName", "lastName"]
        verbose_name = "Autor"


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return "Category: " + self.name

