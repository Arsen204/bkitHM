from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_computers, name="main"),
    path('create/', views.create_computer, name="add"),
    path('update/<int:computer_id>', views.update_computer, name="edit"),
    path('delete/<int:computer_id>/', views.delete_computer, name="delete"),
]
