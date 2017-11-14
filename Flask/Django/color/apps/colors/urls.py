from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.index),
    url(r'^session_words', views.words),
    url(r'^add_word', views. add_word)

]