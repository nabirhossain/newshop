from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True,verbose_name='category slug')
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        full_path = [self.name]
        k = self.parent

        while k is not None:
            full_path.append(k.name)
            k = k.parent

        return ' / '.join(full_path[::-1])


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    discount = models.FloatField(default=0, blank=True, null=True)
    number_of_sales = models.PositiveIntegerField(default=0, blank=True, null=True)
    number_of_views = models.PositiveIntegerField(default=0, blank=True, null=True)
    description = models.TextField()
    image = models.ImageField()
    image1 = models.ImageField()
    image2 = models.ImageField()
    slider = models.BooleanField(default=False)
    publish = models.BooleanField(default=True)
    block_review = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'slug': self.slug})

    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent

        for i in range(len(breadcrumb) - 1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i - 1:-1])
        return breadcrumb[-1:0:-1]


