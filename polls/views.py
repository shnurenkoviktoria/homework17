from django.shortcuts import render, redirect
from django.urls import reverse

from polls.forms import MemoryForm
from polls.models import Memory


def form_image(request):
    if request.method == "POST":
        form = MemoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("show"))
        return render(request, "images_form.html", {"form": form})
    else:
        form = MemoryForm()
        return render(request, "images_form.html", {"form": form})


def images_show(request):
    images = Memory.objects.all()
    return render(request, "images.html", {"images": images})
