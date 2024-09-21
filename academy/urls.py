"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from information.views import home_view, contact_view, who_are_we_view, search_view, register_view, login_view, account_view
from courses.views import courses_view, courses_detail
from blog.views import blog_view, blog_detail
from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', include('information.urls',namespace='information')),
    path('', include('courses.urls',namespace='courses')),   
    path('', include('courses.urls',namespace='courses_detail')),
    path('', include('blog.urls',namespace='blog')),
    path('', include('blog.urls',namespace='blog_detail')),


    path('admin/', admin.site.urls),
]+ debug_toolbar_urls() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

