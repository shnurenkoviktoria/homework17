from django.shortcuts import render, redirect
from django.urls import reverse

from polls.forms import MemoryForm
from polls.models import Memory


def form_image(request):
    form = MemoryForm(request.POST, request.FILES)

    if request.method == "GET":
        form = MemoryForm()
        return render(request, "images_form.html", {"form": form})

    if form.is_valid():
        form.save()
        return redirect(reverse(images_show))
    elif form.is_valid() is False:
        return render(request, "images_form.html", {"form": form, "errors": form.errors})
    return render(request, "images_form.html", {"form": form})


def images_show(request):
    images = Memory.objects.all()
    return render(request, "images.html", {"images": images})
