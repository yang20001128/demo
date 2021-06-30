"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from demo01.views import Author_Create_View, Book_Create_View, Author_Retrieve_View, Book_Retrieve_View
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author_c/', Author_Create_View.as_view()),  # 作者信息添加
    path('book_c/', Book_Create_View.as_view()),  # 作品信息添加
    path('author_r/', Author_Retrieve_View.as_view()),  # 作者信息读取
    path('book_r/', Book_Retrieve_View.as_view()),  # 作品信息读取
    path('dosc/', include_docs_urls()),
]

# from rest_framework.routers import DefaultRouter
# from demo01.views import AuthorView
#
# router = DefaultRouter()
# router.register('author',AuthorView)
# urlpatterns+=router.urls #添加到urlpatterns
