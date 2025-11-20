
from django.db import models
class Dataset(models.Model):
    file=models.FileField(upload_to='datasets/')
    uploaded_at=models.DateTimeField(auto_now_add=True)
    original_filename=models.CharField(max_length=255, blank=True)
    summary=models.JSONField(null=True, blank=True)
    row_count=models.IntegerField(default=0)
