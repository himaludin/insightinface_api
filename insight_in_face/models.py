from django.db import models

class FaceModel(models.Model):
    photo = models.ImageField(upload_to='photos/')
    device_id = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    satisfaction = models.FloatField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'faces'