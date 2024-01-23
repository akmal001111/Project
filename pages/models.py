from django.db import models


class NewModel(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    photo = models.ImageField(upload_to="blogs")
    job = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "New"
        verbose_name_plural = "News"


class BlogModel(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="blogs")
    short_description = models.TextField()
    long_description = models.TextField()
    author = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "blog"
        verbose_name_plural = "blogs"


class GalleriesModel(models.Model):
    title = models.CharField(max_length=30)
    photo = models.ImageField()
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "gallery"
        verbose_name_plural = "galleries"

