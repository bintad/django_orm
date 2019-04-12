from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new_book$', views.new_book),
    url(r'^books/(?P<number>\d+)$', views.show_book),
    url(r'^add_author/(?P<number>\d+)$', views.add_author),
    url(r'^authors$', views.show_authors),
    url(r'^authors/(?P<number>\d+)$', views.author_info),
    url(r'^new_author$', views.new_author),
    url(r'^add_book/(?P<number>\d+)$', views.add_book)
]