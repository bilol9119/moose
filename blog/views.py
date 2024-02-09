from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Contact, Subscriptions, Comment
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
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

    paginator = Paginator(all_blogs, items_per_page)

    page_number = request.GET.get('page', 1)

    page = paginator.get_page(page_number)

    context = {'page': page,  'blogs': page.object_list}

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


