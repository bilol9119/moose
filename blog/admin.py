from django.contrib import admin
from .models import Blog, Contact, Subscriptions, Category, Comment
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'id', 'descrpt1', 'descrpt2')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_solved')
    search_fields = ('name', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subscriptions)
admin.site.register(Comment, CategoryAdmin)
