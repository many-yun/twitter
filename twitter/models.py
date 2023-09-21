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
        # twit_list = list(self.children.all()[:1])
        # for child in self.children.all()[:1]:
        #     twit_list.extend(list(child.get_all_children())) 
        # return twit_list
        twit_list = list(self.children.all()[:1])
        if twit_list:
            twit_list.extend(list(twit_list[0].get_all_children())) # extend : 리스트 끝에 항목 추가 (extend와 append의 차이?)
        return twit_list
    
    


# child -> parent
# parent -> children
