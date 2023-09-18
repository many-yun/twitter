from django.db import models

class Twit(models.Model):
    content = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content


