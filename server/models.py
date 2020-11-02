from django.db import models
from django.forms.models import model_to_dict

class Category(models.Model):
    title = models.CharField(max_length=50, null=False)

    def to_dict(self):
        dictionary = model_to_dict(self)
        return dictionary

class Post(models.Model):
    title = models.CharField(max_length=50, null=False)
    content = models.CharField(max_length=200, null=False)
    datetime = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def to_dict(self):
        dictionary = model_to_dict(self)
        dictionary['datetime'] = str(dictionary['datetime'])
        if dictionary['category']:
            dictionary['category'] = Category.objects.get(id=dictionary['category']).title
        return dictionary