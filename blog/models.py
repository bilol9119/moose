from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=50)
    work = models.CharField(max_length=50)

    img = models.ImageField(upload_to='posts/')
    title = models.CharField(max_length=200)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    descrpt1 = models.TextField()
    descrpt2 = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, default=1)
    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField()

    is_solved = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Subscriptions(models.Model):
    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

