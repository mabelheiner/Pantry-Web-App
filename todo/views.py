import random
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import breakfast_items, desert_items, dinner_items, lunch_items, snacks_items

# Create your views here.
def todoView(request):
  return render(request, 'index.html')

def addBreakfast(request):
  all_breakfast_items = breakfast_items.objects.all()
  new_item = breakfast_items(content = request.POST['content'])
  new_item.save()
  return render(request, 'breakfast.html', {'all_items' : all_breakfast_items})

def deleteBreakfast(request, breakfast_items_id):
  item_to_delete = breakfast_items.objects.get(id=breakfast_items_id)
  item_to_delete.delete()
  return HttpResponseRedirect('/')

def displayBreakfast(request):
  all_breakfast_items = breakfast_items.objects.all()
  return render(request, 'breakfast.html', {'all_items' : all_breakfast_items})

def addLunch(request):
  all_lunch_items = lunch_items.objects.all()
  new_item = lunch_items(content = request.POST['content'])
  new_item.save()
  return render(request, 'lunch.html', {'all_items' : all_lunch_items})

def deleteLunch(request, lunch_items_id):
  item_to_delete = lunch_items.objects.get(id=lunch_items_id)
  item_to_delete.delete()
  return HttpResponseRedirect('/')

def displayLunch(request):
  all_lunch_items = lunch_items.objects.all() 
  return render(request, 'lunch.html', {'all_items' : all_lunch_items}) 

def addDinner(request):
  all_dinner_items = dinner_items.objects.all()
  new_item = dinner_items(content = request.POST['content'])
  new_item.save()
  return render(request, 'dinner.html', {'all_items' : all_dinner_items})

def deleteDinner(request, dinner_items_id):
  item_to_delete = dinner_items.objects.get(id=dinner_items_id)
  item_to_delete.delete()
  return HttpResponseRedirect('/')

def displayDinner(request):
  all_dinner_items = dinner_items.objects.all() 
  return render(request, 'dinner.html', {'all_items' : all_dinner_items}) 

def addDesert(request):
  all_desert_items = desert_items.objects.all()
  new_item = desert_items(content = request.POST['content'])
  new_item.save()
  return render(request, 'desert.html', {'all_items' : all_desert_items})

def deleteDesert(request, desert_items_id):
  item_to_delete = desert_items.objects.get(id=desert_items_id)
  item_to_delete.delete()
  return HttpResponseRedirect('/')

def displayDesert(request):
  all_desert_items = desert_items.objects.all() 
  return render(request, 'desert.html', {'all_items' : all_desert_items}) 

def addSnack(request):
    all_snack_items = snacks_items.objects.all()
    new_item = snacks_items(content = request.POST['content'])
    new_item.save()
    return render(request, 'snack.html', {'all_items' : all_snack_items})

def deleteSnack(request, snack_items_id):
  item_to_delete = snacks_items.objects.get(id=snack_items_id)
  item_to_delete.delete()
  return HttpResponseRedirect('/')

def displaySnack(request):
  all_snack_items = snacks_items.objects.all() 
  return render(request, 'snack.html', {'all_items' : all_snack_items}) 

def coverImage(request):
    image_data = open("./todo/app.png", "rb").read()
    return HttpResponse(image_data, content_type="image/png")

def goHome(request):
  return render(request, 'index.html')