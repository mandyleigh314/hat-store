from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import CheckoutForm


def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'shop/product/list.html', {'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})

def checkout(request, id, slug):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            product = get_object_or_404(Product, id=id, available=True)
            order = form.save(commit = False)
            order.product = product
            order.save()
            product.stock -= 1
            product.save()
            return render(request, 'shop/orders/ordercomplete.html',
            {'product': product, 'order': order})
    else:
        product = get_object_or_404(Product, id=id, available=True)
        form = CheckoutForm()
        return render(request,
                  'shop/orders/orderform.html',
                  {'product': product, 'form': form})
