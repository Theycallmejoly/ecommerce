from django.shortcuts import render, get_object_or_404 , redirect
from .models import Product , Cart , CartItem , Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, CartItemForm

def product_list(reqeust):
    products = Product.objects.all()
    return render (reqeust , 'shop/product_list.html' , {'products':products})

def product_detail(reqeuest , product_id):
    product  = get_object_or_404(Product , id = product_id)
    return render(reqeuest , 'shop/product_detail.html' , {'product':product})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            return redirect('product_list') 
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_detail')



@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        if 'update_quantity' in request.POST:
            item_id = request.POST.get('item_id')
            new_quantity = int(request.POST.get('quantity'))
            cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
            cart_item.quantity = new_quantity
            cart_item.save()
        elif 'remove_item' in request.POST:
            item_id = request.POST.get('item_id')
            cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
            cart_item.delete()
        return redirect('cart_detail')
    
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'shop/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

@login_required
def checkout(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)

    if request.method == 'POST':
        
        order = Order.objects.create(user=request.user)
        for item in cart_items:
            
            order.items.create(
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
        # Clear the cart
        cart_items.delete()
        return redirect('order_confirmation')

    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'shop/checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
    })

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)
    cart_item.delete()
    return redirect('cart_detail')

@login_required
def update_cart(request):
    if request.method == 'POST':
        cart = Cart.objects.get(user=request.user)
        for key, value in request.POST.items():
            if key.startswith('quantity_'):
                item_id = key.split('_')[1]
                quantity = int(value)
                cart_item = get_object_or_404(CartItem, id=item_id)
                if quantity <= 0:
                    cart_item.delete()
                else:
                    cart_item.quantity = quantity
                    cart_item.save()
        return redirect('cart_detail')

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')  # Adjust field name here
    for order in orders:
        order.total_amount = order.items.aggregate(total=Sum('price'))['total']
    return render(request, 'shop/order_history.html', {'orders': orders})