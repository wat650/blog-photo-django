from django.db import models

# Create your models here.
class Photo(models.Model):
    title = models.CharField(max_length=50, null=False)
    description = models.TextField()
    image = models.ImageField(upload_to='photos/', height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title