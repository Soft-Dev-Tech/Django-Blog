from django.db import models

# Create your managers here


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='pb')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)
