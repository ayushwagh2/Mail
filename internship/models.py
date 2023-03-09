from django.db import models

class Mails(models.Model):
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    ReadAt = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text
