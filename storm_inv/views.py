from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .models import Snack
from .forms import PersonForm, SnackForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import datetime


def home(request):
    person = Person.objects.all()
    return render(request, 'storm/home.html', {'person': person})


def add_person(request):
    if request.method == 'GET':
        return render(request, 'storm/add_person.html', {'form': PersonForm()})
    else:
        try:
            form = PersonForm(request.POST)
            newperson = form.save(commit=False)
            newperson.user = request.user
            newperson.save()
            return redirect('home')
        except ValueError:
            return render(request, 'storm/add_person.html', {'form': PersonForm(), 'error': 'Bad data passed in'})


def person_home(request, person_pk):
    person = get_object_or_404(Person, pk=person_pk)
    snack = Snack.objects.all()
    rows = 'a'
    if person.movement is not None:
        mov = person.movement.split(',')
        return render(request, 'storm/person.html', {'person': person, 'mov': mov, 'snack': snack, 'rows': rows})
    else:
        return render(request, 'storm/person.html', {'person': person, 'snack': snack, 'rows': rows})


def person_list(request):
    person = Person.objects.all()
    return render(request, 'storm/person_list.html', {'person': person})


def edit_person(request, person_pk):
    person = get_object_or_404(Person, pk=person_pk)
    rows = 'a'
    if request.method == 'GET':
        form = PersonForm(instance=person)
        return render(request, 'storm/edit_person.html', {'person': person, 'form': form, 'rows': rows})
    else:
        try:
            form = PersonForm(request.POST, instance=person)
            form.save()
            return redirect('person_list')
        except ValueError():
            return render(request, 'storm/edit_person.html', {'person': person, 'form': form, 'error': 'Bad info'})


def delete_person(request, person_pk):
    person = get_object_or_404(Person, pk=person_pk)
    if request.method == 'POST':
        person.delete()
        return redirect('person_list')


def inventory_home(request):
    snack = Snack.objects.all()
    return render(request, 'storm/inventory.html', {'snack': snack})


def inventory_list(request):
    snack = Snack.objects.all()
    return render(request, 'storm/edit_inventory.html', {'snack': snack})


def subtract_inventory(request, person_pk, snack_pk):
    person = get_object_or_404(Person, pk=person_pk)
    snack = get_object_or_404(Snack, pk=snack_pk)
    time = datetime.date.today()
    if request.method == "POST":
        person.money -= snack.price
        snack.amount -= 1
        if person.movement is not None:
            toli = person.movement.split(',')
            toli.insert(0,
                        f' Date: {time}  ----  Item: {snack.name} --- Price: ${snack.price}  ----  Account Balance: {person.money}, ')
            person.movement = ', '.join(toli)
            person.save()
            snack.save()
            return redirect('home')
        else:
            person.movement = f' Date: {time}  ----  Item: {snack.name} --- Price: ${snack.price}  ----  Account Balance: {person.money}, '
            person.save()
            snack.save()
            return redirect('home')


def add_inventory(request):
    if request.method == 'GET':
        return render(request, 'storm/add_inventory.html', {'form': SnackForm()})
    else:
        try:
            form = SnackForm(request.POST)
            newperson = form.save(commit=False)
            newperson.user = request.user
            newperson.save()
            return redirect('home')
        except ValueError:
            return render(request, 'storm/add_inventory.html', {'form': SnackForm(), 'error': 'Bad data passed in'})


def delete_inventory(request, snack_pk):
    snack = get_object_or_404(Snack, pk=snack_pk)
    if request.method == 'POST':
        snack.delete()
        return redirect('inventory_list')


def edit_inventory(request, snack_pk):
    snack = get_object_or_404(Snack, pk=snack_pk)
    if request.method == 'GET':
        form = SnackForm(instance=snack)
        return render(request, 'storm/edit_snack.html', {'snack': snack, 'form': form})
    else:
        try:
            form = SnackForm(request.POST, instance=snack)
            form.save()
            return redirect('inventory_list')
        except ValueError():
            return render(request, 'storm/edit_snack.html', {'snack': snack, 'form': form, 'error': 'Bad info'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'storm/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'storm/loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'Username not found...'})
        else:
            login(request, user)
            return redirect('home')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
