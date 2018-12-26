from django.views.generic.list import ListView
from .models import Shop

class ShopListView(ListView):
    model = Shop
    paginate_by = 20


