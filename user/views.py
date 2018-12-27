from django.shortcuts import render
from django.utils.html import escape
from django.views.decorators.http import require_http_methods
from django_datatables_view.base_datatable_view import BaseDatatableView

from .models import User
from .forms import UserUpdateForm


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


def ranking_view(request):
    return render(request, 'ranking/index.html')


class RankingListJson(BaseDatatableView):
    model = User
    columns = ['', 'ranking_id', 'name', 'points']
    max_display_length = 100

    def render_column(self, row, column):
        if column == 'name':
            return escape(row.name or row.username)
        else:
            return super(RankingListJson, self).render_column(row, column)
