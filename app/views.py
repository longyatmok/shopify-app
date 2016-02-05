from django.shortcuts import render
from shopify_auth.decorators import login_required
import shopify
from app.model.product import *

# Create your views here.
@login_required
def home(request):
    with request.user.session:
        products = Product().get_list()

    return render(request, "app/home.html", {
        'products': products
      })