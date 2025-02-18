"""CatOverflow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from CatOverflow import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('question/<int:question_id>', views.question, name='question'),
    path('ask/', views.ask, name='ask'),
    path('hot/', views.hot, name='ask'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
    path('tag/<tag_id>/', views.tag, name='tag'),
    path('logout_view/', views.logout_view, name="logout_view"),
    path('like/', views.like, name="like"),
    path('correct/', views.correct, name="correct"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) \
#                    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
