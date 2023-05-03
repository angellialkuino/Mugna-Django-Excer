"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from exercises import views
from django.urls import path, include
from django.views.generic.base import TemplateView #para sa unsa mn ni

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    path('admin/', admin.site.urls),
    path("math/<int:num1>/<int:num2>", views.mathed2),
    path("math/<int:num1>/<int:num2>/<int:num3>", views.mathed3),
    path("valid-date/<int:year>/<int:month>/<int:day>", views.date_format),

    path("books/", views.book_list, name="book-list"),
    path("books/<int:book_id>", views.book_details, name="book-details"),
    path("author/<int:author_id>", views.author_info, name="author-info"),
    path("classification/", views.classification_list),
    path("classification/<int:classification_id>", views.classification_books, name="classification"),

    path("search-author/", views.search_author, name="search-author"),
    path("search-publisher/", views.search_publisher, name="search-publisher"),

    path("create-publisher/", views.create_publisher, name="create-publisher"),
    path("create-book/", views.create_book, name="create-book"),
    path("create-author/", views.create_author, name="create-author"),


    path("update-publisher/<int:pk>/", views.update_publisher),
    path("update-book/<int:pk>/", views.update_book, name='update-book'),
    path("update-author/<int:pk>/", views.update_author, name='update-author'),

    path("delete-publisher/<int:pk>/", views.delete_publisher),
    path("delete-book/<int:pk>/", views.delete_book),
    path("delete-author/<int:pk>/", views.delete_author, name='delete-author'),



    # path("register/", views.register),
    # path("login/", views.login_view),
    # path("logout/", views.logout_view),


]

