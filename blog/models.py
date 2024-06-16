from django.db import models
from django.utils.text import slugify

class SchoolClass(models.Model):
    """
    Model to create school classes
    """
    class Meta:
        verbose_name_plural = 'School Classes'
    
    name = models.CharField(max_length=100, blank=False, unique=True)
    slug = models.SlugField(max_length=200, blank=True, editable=False, unique=True,)
    description = models.TextField(max_length=2000, blank=True)
    image = models.ImageField(null=True, blank=True)
    weekly_letter = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Generate a slug based on the name
        """
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)