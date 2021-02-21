from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def purchase(request):
    if request.method == "POST":
        quantity_from_form = int(request.POST["quantity"])
        get_product = Product.objects.get(id=request.POST['product_id'])
        total_charge = quantity_from_form * get_product.price
        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    return redirect('/checkout/')

def checkout(request):
    last_order = Order.objects.last()
    total_products = Order.objects.aggregate(Sum('quantity_ordered'))['quantity_ordered__sum']
    total_spent = Order.objects.aggregate(Sum('total_price'))['total_price__sum']
    context = {
        'last_order': last_order,
        'total_products': total_products,
        'total_spent': total_spent
    }
    return render(request, "store/checkout.html", context)