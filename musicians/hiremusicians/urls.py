from django.urls import path


from . import views

urlpatterns = [
    path('hiremusicians', views.hiremusicians, name="hiremusicians"),

]
