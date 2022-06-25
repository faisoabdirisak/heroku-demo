from uuid import uuid4
from django.db import models
from users.models import Profile

# Create your models here.

# class Review(models.Model):
   
#     owner=models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
#     review = models.TextField(max_length=500, blank=True)
#     rating = models.FloatField()
#     status = models.BooleanField(default=True)
#     created=models.DateField(auto_now_add=True)
#     id=models.UUIDField(default=uuid4, unique=True, primary_key=True,editable=False)
    

#     # class Meta:
#     #     unique_together = [['owner']]

#     def __str__(self):
#         return self.review