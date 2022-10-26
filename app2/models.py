from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class App2(models.Model):
    fileName = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    fileUploaded = models.FileField(upload_to='app2/uploaded_file')
    # CASCADE: also delete all the notes associated with the user
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files")

