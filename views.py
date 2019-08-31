from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User

from .models import Todo
from .forms import TodoForm, RegisterForm, ContactForm
from .tools import send_email


def index(request):

    # Error here we need to fix this!
    form = TodoForm()

    if request.user.is_authenticated is False:
        return render(request, 'main/index.html', {'todo_list': [], 'form': form})

    user = User.objects.get(pk=request.user.id)
    todo_list = user.todo_set.all()
    contacts = user.contact_set.all().order_by('id')
    categories = Category.objects.all()
    return render(request, 'main/index.html', {'todo_list': todo_list, 'form': form, 'categories': categories})

def add(request):
    if request.user.is_authenticated is False:
        messages.warning(request, 'Please register or login to start your Todo List.')
        return redirect('index')

    form = TodoForm(request.POST)
    if form.is_valid():
        if request.POST['text']:
            text = request.POST['text']
            category = request.POST['category_select']
            contacts = request.POST.getlist('contact_select')
            if category:
                new_todo = Todo(text = text, complete = False,
                            username = request.user, category = Category.objects.get(name=category))
            else:
                new_todo = Todo(text = text, complete = False, username = request.user)
            if contacts:
                send_email(contacts, text)
            new_todo.save()
        if 'delcompleted'  in request.POST:
            for todo in Todo.objects.filter(username = request.user):
                if todo.complete:
                    todo.delete()
        if 'delall' in request.POST:
            for todo in Todo.objects.filter(username = request.user):
                todo.delete()
    return redirect('index')

    return redirect('index')

def complete(request, todo_id):
    if request.user.is_authenticated is False:
        messages.warning(request, 'Please register to start your Todo List.')
        return redirect('index')

    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def contacts(request):
    form = ContactForm()
    user = User.objects.get(pk=request.user.id)
    contacts = user.contact_set.all().order_by('id')

    return render(request, 'main/contacts.html', {'form': form, 'contacts': contacts})

def editcontacts(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        new_contact = Contact(first_name = request.POST['first_name'], last_name = request.POST['last_name'],
                        email = request.POST['email'], username = request.user)
        new_contact.save()
        return redirect('contacts')
    return redirect('contacts')

def deletecontact(request, contact_id):
    contact = Contact.objects.get(pk=contact_id)
    contact.delete()

    return redirect('contacts')

def login(request):
    return render(request, 'main/login.html', {'title': 'Login'})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now login!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'main/register.html', {'form': form, 'title': 'Register'})