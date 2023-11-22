from django.shortcuts import render
from webapp.cat_stats_db import CatDB


def hello(request):
    return render(request, template_name='hello.html')


def display_info(request):
    if request.method == "POST":
        CatDB.name = request.POST.get('name')
        cat_stats = CatDB.to_dict()
    elif request.method == "GET":
        if request.GET.get('select') is not None:
            CatDB.choose_action(request.GET.get('select'))
            cat_stats = CatDB.to_dict()
    return render(request, template_name='info.html', context=cat_stats)
