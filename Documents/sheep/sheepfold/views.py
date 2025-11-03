from django.shortcuts import render, get_object_or_404, redirect
from .models import Sheep,BirthEvent,Milk
from sheepfold.forms import SheepForm,SheepingForm,MilkForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .forms import SheepingForm
from .serializers import MilkSerializer


def homepage(request):
    sheep = Sheep.objects.all()
    return render(request, "homepage.html", {"sheep": sheep})

def sheep_detail(request, pk):
    sheep = get_object_or_404(Sheep, pk=pk)
    return render(request, "sheep_detail.html", {"sheep": sheep})

def sheep_create(request):
    form = SheepForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("homepage")
    return render(request, "sheep_form.html", {"form": form})

def milking(request):
    form = MilkForm()  # create a new empty form
    milk = Milk.objects.all()  # fetch existing records
    return render(request, "milking.html", {"form": form, "milk": milk})

@api_view(['GET', 'POST'])
def milking_api(request):
    if request.method == 'GET':
        milk = Milk.objects.all()
        serializer = MilkSerializer(milk, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MilkSerializer(data=request.data)  # <- use request.data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def lamping(request):
    if request.method == 'POST':
        form = SheepingForm(request.POST)
        if form.is_valid():
            birth_event = form.save(commit=False)
            birth_event.save()

            new_lamb_names = request.POST.get('new_lambs', '').split(',')

            for name in new_lamb_names:
                name = name.strip()
                if name:
                    lamb = Sheep.objects.create(
                        name=name,
                    )
                    birth_event.lambs.add(lamb)

            form.save_m2m()

            return redirect('homepage')
    else:
        form = SheepingForm()

    return render(request, 'lamping.html', {'form': form})

