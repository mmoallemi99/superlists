from django.shortcuts import render, redirect

from .models import Item, List


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'list.html', context)


def new_list(request):
    list_ = List.objects.create()
    new_item_text = request.POST['item_text']
    Item.objects.create(text=new_item_text, list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
