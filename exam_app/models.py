from django.db import models

# Create your models here.

class Images(models.Model):
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'images'
