"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from todo.views import addBreakfast, addDesert, addDinner, addLunch, addSnack, deleteBreakfast, deleteDesert, deleteDinner, deleteLunch, deleteSnack, displayBreakfast, displayDesert, displayDinner, displayLunch, displaySnack, goHome, todoView, coverImage

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', todoView),
    path('addBreakfast/', addBreakfast),
    path('addLunch/', addLunch),
    path('addDinner/', addDinner),
    path('addDesert/', addDesert),
    path('addSnack/', addSnack),
    path('deleteBreakfast/<int:breakfast_items_id>/', deleteBreakfast),
    path('deleteLunch/<int:lunch_items_id>/', deleteLunch),
    path('deleteDinner/<int:dinner_items_id>/', deleteDinner),
    path('deleteDesert/<int:desert_items_id>/', deleteDesert),
    path('deleteSnack/<int:snack_items_id>/', deleteSnack),
    path('displayBreakfast/', displayBreakfast),
    path('displayLunch/', displayLunch),
    path('displayDinner/', displayDinner),
    path('displayDesert/', displayDesert),
    path('displaySnack/', displaySnack),
    path('goHome/', goHome),

    path('app.png', coverImage),


]