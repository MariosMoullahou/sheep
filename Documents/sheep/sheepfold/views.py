from django.shortcuts import render, get_object_or_404, redirect
from .models import Sheep,BirthEvent,Milk
from sheepfold.forms import SheepForm,SheepingForm,MilkForm

from django.shortcuts import render, redirect
from .forms import SheepingForm
from .models import Sheep


# List all sheep
def homepage(request):
    sheep = Sheep.objects.all()
    return render(request, "homepage.html", {"sheep": sheep})

# Show details for one sheep
def sheep_detail(request, pk):
    sheep = get_object_or_404(Sheep, pk=pk)
    return render(request, "sheep_detail.html", {"sheep": sheep})

# Create a new sheep
def sheep_create(request):
    form = SheepForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("homepage")
    return render(request, "sheep_form.html", {"form": form})

def milking(request):
    form = MilkForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("homepage")
    return render(request, "milking.html", {"form": form})


def lamping(request):
    if request.method == 'POST':
        form = SheepingForm(request.POST)
        if form.is_valid():
            # Create and save the BirthEvent instance (but not M2M fields yet)
            birth_event = form.save(commit=False)
            birth_event.save()

            # ✅ Fix: 'new_lambs' (with 's') must match the input name in your HTML
            new_lamb_names = request.POST.get('new_lambs', '').split(',')

            # Create each lamb and link it to the event
            for name in new_lamb_names:
                name = name.strip()
                if name:
                    lamb = Sheep.objects.create(
                        name=name,
                    )
                    birth_event.lambs.add(lamb)

            # Save existing ManyToMany (if any)
            form.save_m2m()

            return redirect('homepage')
    else:
        form = SheepingForm()

    return render(request, 'lamping.html', {'form': form})

