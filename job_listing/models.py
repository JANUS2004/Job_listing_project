from django.db import models

class Job(models.Model):
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=100)  # Like Full-time, Part-time, etc.
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

