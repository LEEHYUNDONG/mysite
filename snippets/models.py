from django.db import models

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    studentId = models.CharField(max_length=100, blank=True, default='')
    name = models.TextField()

    
    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return self.title
