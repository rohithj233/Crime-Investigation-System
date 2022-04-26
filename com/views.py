from django.shortcuts import render
from .forms import complaint_form


def index(request):
    return render(request, 'index.html')


def complaint(request):
    form = complaint_form()
    if request.method == 'POST':
        form = complaint_form(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}

    return render(request, 'complaint.html', context)
