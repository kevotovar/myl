from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from . import models
from .forms import UserUpdateForm

# Create your views here.
@require_http_methods(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'profile/index.html', {
        'form': form
    })
