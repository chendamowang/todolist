# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import TodoList
from .forms import TodoListForm


def index(request):
    if request.POST:
        TodoList.objects.create(
            title = request.POST['title'],
            creator = request.user
        )
        return redirect(reverse('home', args=[]))
    return render(request, 'index.html')


@login_required
def edit(request, todolist_id):
    todolist = get_object_or_404(TodoList, pk=todolist_id)
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            
            todolist.title=request.POST['title']
            todolist.save()
            return redirect(reverse('home', args=[]))
        else:
            return render(request, 'edit_list.html', {'form': form})

    return  render(request, 'edit_list.html', {'form': TodoListForm})

@login_required
def delete(request, todolist_id):
    TodoList.objects.filter(id = todolist_id).delete()
    return redirect(reverse('home', args=[]))

