from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ImageForm()
    return render(request, 'upload.html', {'form': form})

def image_display(request):
    if request.method == 'GET':
        imgs = Image.objects.all()
        return render(request, 'display.html', {'Images': imgs})


def success(request):
    return HttpResponse('successfully uploaded')
