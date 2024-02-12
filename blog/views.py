from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Contact, Subscriptions, Comment
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# Create your views here.
import random


def home_view(request):
    if request.method == 'POST':
        subscribe(request)
        return redirect('/')

    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'index.html', context)


def blog_view(request):
    data = request.GET.get('cat')
    if data:
        all_blogs = Blog.objects.filter(category_id=data).order_by('-created_at')
    else:
        all_blogs = Blog.objects.all().order_by('-created_at')

    items_per_page = 3

    paginator = Pagination(all_blogs, items_per_page)

    page_number = request.GET.get('page', 1)

    blogs = paginator.get_page(page_number)

    context = {'page': paginator,  'blogs': blogs}

    return render(request, 'blog.html', context)


def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)  # default to None if not present
        email = request.POST.get('email', None)
        subject = request.POST.get('subject', None)
        message = request.POST.get('message', None)

        # Create a new instance of the Contact model
        data = Contact(name=name, email=email,
                       subject=subject, message=message)
        data.save()

        return redirect('contact')
    return render(request, 'contact.html')


def about_view(request):
    if request.method == "POST":
        subscribe(request)
        return redirect('about')
    return render(request, 'about.html')


def blog_single_view(request, id):
    if request.method == "POST":
        data = request.POST
        obj = Comment.objects.create(post_id=id, name=data.get('name'), email=data.get('email'), message=data.get('message'))
        obj.save()
        return redirect(f"/blog/{id}")
    blog = Blog.objects.filter(id=id).first()
    comment = Comment.objects.filter(post_id=id)
    context = {'blog': blog, 'comments': comment}
    return render(request, 'blog-single.html', context=context)


def subscribe(request):
    email = request.POST.get('email')
    if email:
        try :
            validate_email(email)
        except ValidationError:
            pass
        else:
            # If the email is valid, proceed with saving to the database
            try:
                if Subscriptions.objects.filter(email=email).exists():
                    pass
                else:
                    db = Subscriptions(email=email)
                    db.save()
            except:
                pass


class Pagination:
    def __init__(self, blogs, num):
        self.currpage = 1
        self.ans = []
        blogs = list(blogs)
        n = len(blogs)
        while n - num >= 0:
            box = []
            for i in range(num):
                blog = blogs.pop(0)
                box.append(blog)
            self.ans.append(tuple(box))
            n -= num
        if n > 0:
            self.ans.append(tuple(blogs))

    def get_page(self, page):
        if len(self.ans) >= int(page):
            self.currpage = int(page)
            return self.ans[int(page)-1]

    def has_previous(self):
        if self.currpage - 1 >= 1:
            return True

    def previous(self):
        return self.currpage-1

    def page_range(self):
        page = range(1, len(self.ans)+1)
        return page

    def object_list(self):
        return self.ans

    def curr_page(self):
        return self.currpage

    def has_next(self):
        if self.currpage + 1 <= len(self.ans):
            return True

    def next(self):
        return self.currpage + 1