from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title[:50]