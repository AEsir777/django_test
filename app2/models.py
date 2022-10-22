from django.db import models

# Create your models here.
class App2(models.Model):
    fileName = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    fileUploaded = models.FileField(upload_to='app2/uploaded_file')

