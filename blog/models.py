from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))



class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    table_number = models.IntegerField(default=1)  # learned from CI
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('date', 'table_number')

    def __str__(self):
        return f"{self.date} - Table {self.table_number} - {'Booked' if self.booked else 'Available'} by {self.user.username if self.booked else 'N/A'}"


# class Post(models.Model):

#     title = models.CharField(max_length=200, unique=True)
#     slug = models.SlugField(max_length=200, unique=True)
#     author = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="blog_posts"
#     )
#     content = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     status = models.IntegerField(choices=STATUS, default=0)
#     excerpt = models.TextField(blank=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     class Meta:
#         ordering = ["-created_on"]

#     def __str__(self):
#         return f"{self.title} | written by {self.author}"


# class Comment(models.Model):
#     post = models.ForeignKey(
#         Post,
#         on_delete=models.CASCADE,
#         related_name="comments"
#     )
#     author = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="comments_author"
#     )
#     body = models.TextField()
#     approved = models.BooleanField(default=False)
#     created_on = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         ordering = ["created_on"]

#     def __str__(self):
#         return f"Comment {self.body} by {self.author}"


