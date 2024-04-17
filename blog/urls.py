
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (home_view, blog_view, contact_view,
                    about_view, blog_single_view,blog_category_view)


urlpatterns = [
    path('', home_view, name='home'),
    path('blog/', blog_view, name='blog'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('blog/cat/<int:pk>/', blog_category_view, name='blog_category'),
    path('blog/<int:id>/', blog_single_view),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




