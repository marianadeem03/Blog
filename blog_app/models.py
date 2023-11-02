from django.db import models
from users.models import User


# Create your models here.

class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        get_latest_by = "order_date"


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=250)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    post_image = models.ImageField(upload_to='images/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"
        get_latest_by = "order_date"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    # CASCADE: When the referenced object is deleted, also delete the objects that have references to
    # it (when you remove a blog post for instance, you might want to delete comments as well).

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"
        get_latest_by = "order_date"
