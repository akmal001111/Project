from django.urls import path

from pages.views import *

app_name = "pages"

urlpatterns = [
    path("", home_page_view, name="home"),
    path("contact/", contact_page_view, name="contact"),
    path("blog/", blog_detail, name="blog_detail"),
    path("about/", about_page_view, name="about_page_view"),

]