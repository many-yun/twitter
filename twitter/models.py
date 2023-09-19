from django.db import models
from django.contrib.auth.models import User

class Twit(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.content
    
    def get_all_children(self):
        twit_list = list(self.children.all())
        for child in self.children.all():
            twit_list.extend(list(child.get_all_children())) 
        return twit_list



