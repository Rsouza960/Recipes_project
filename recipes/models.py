from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):   # noqa: E302
    name = models.CharField(max_length=65,)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=65, verbose_name='titulo')
    description = models.CharField(max_length=165)
    slug = models.SlugField(unique=True)
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=65)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=65)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d', blank=True, default='')   # noqa: E501
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Categoria')  # noqa:E501
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True )  # noqa: E501, E202
    def __str__(self): # noqa: E301, E261
        return self.title   # noqa: W292