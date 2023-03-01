from time import timezone
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# un modelo de usuario creado por django
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)  # Guarda la sesion (usando las cookies)
                return redirect('home')
            except:
                return render(request, 'signup.html', {'error': 'This user already exists.'})
        else:
            return render(request, 'signup.html', {'error': 'Passwords no not match.'})


def index(request):
    return render(request, 'index.html', {'username': request.user})


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        # authenticate verifica el usuario y la contraseña

        if user is None:
            return render(request, 'signin.html', {'error': 'The username or password is incorrect.'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def signuot(request):
    logout(request)
    return redirect('home')

@login_required
def tasks(request):
    tasks = []
    if request.method == 'GET':
        tasks = Task.objects.filter(user=request.user)

    else:
        op = request.POST['filter_option']
        if op == '1':  # None
            tasks = Task.objects.filter(user=request.user)
        elif op == '2':  # important
            tasks = Task.objects.filter(user=request.user, important=True)
        elif op == '3':  # Not important
            tasks = Task.objects.filter(user=request.user, important=False)
        elif op == '4':  # Completed
            tasks = Task.objects.filter(
                user=request.user, date_completed__isnull=False)
        elif op == '5':  # Not completed
            tasks = Task.objects.filter(user=request.user, date_completed=None)

    return render(request, 'tasks.html', {'tasks': tasks})

@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': TaskForm})
    else:
        try:
            # Crea un formulario con los datos obtenidos con el metodo POST
            form = TaskForm(request.POST)
            # Si le agegamos el commit=False el formulario solo va a devolver los datos y estos se puedem guardar en una tarea
            new_task = form.save(commit=False)
            # request.user es el usuario actual guardado en las cookies del navegador
            new_task.user = request.user
            new_task.save()  # Ahora solo guardamos la tarea en la base de datos

            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {'form': TaskForm, 'error': 'Please provide a valid data.'})

@login_required
def done_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'GET':
        task.date_completed = timezone.now()
        task.save()

        return redirect('tasks')

@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('tasks')

@login_required
def detail_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    return render(request, 'details_task.html', {'task': task})

@login_required
def edit_task(request, id):
    # El: user=request.user, es necesario ya que desde la dirección de la pagina se puede acceder a las tareas de cualquier usuario
    task = get_object_or_404(Task, id=id, user=request.user)
    if request.method == 'GET':
        form = TaskForm(instance=task)

        return render(request, 'create_task.html', {'form': form, 'task': task})
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()

            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {'form': form, 'task': task, 'error': 'Error updating task'})
