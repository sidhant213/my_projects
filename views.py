from django.shortcuts import render ,redirect
from django.views import View
from .models import *
from django.contrib.auth.models import User
from .models import customer

from .form import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
# Create your views here.
class ProductView(View):
    def get(self, request): 
        topwears=Product.objects.filter(category='TW')
        bottomwears=Product.objects.filter(category='BW')
        mobiles=Product.objects.filter(category='M')
        laptops=Product.objects.filter(category='L')
        return render(request, 'app/home.html',{'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles, 'laptops': laptops})




@login_required
def home(request):
    return render(request, 'app/home.html')



# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        item_already_in_cart=False
        if request.user.is_authenticated:
          item_already_in_cart=Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request, 'app/productdetail.html', {'product': product,
        'item_already_in_cart':item_already_in_cart})

@login_required
def add_to_cart(request, product_id):
    user = request.user
 
    product = Product.objects.get(id=product_id)
   
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart')  # go to cart page after adding

@login_required
def show_cart(request):
    cart_items = Cart.objects.filter(user=request.user)

    # Calculate totals
    total_amount = 0.0
    amount=0.0
    shipping_amount = 70  # fixed for now
    cart_product = [p for p in Cart.objects.all() if p.user == request.user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        total_amount = amount + shipping_amount
        print(cart_product)
    else:
        total_amount = 0.0
        shipping_amount = 0.0

    # total_amount = 0.0


    # for item in cart_items:
    #     total_amount += item.quantity * item.product.discounted_price


    context = {
        'cart_items': cart_items,
        'amount': amount,
        'total_amount': total_amount,
        'shipping_amount': shipping_amount,
        'final_amount': total_amount + shipping_amount if cart_items else 0
    }
    return render(request, 'app/addtocart.html', context)

def plus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
         

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': amount + shipping_amount
        }
        return JsonResponse(data)

def minus_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        if c.quantity > 1:   # prevent going below 1
            c.quantity -= 1
            c.save()

        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': amount + shipping_amount
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()

        amount = 0.0
        shipping_amount = 70.0
        cart_product = [p for p in Cart.objects.all() if p.user == request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount

        data = {
            'amount': amount,
            'total_amount': amount + shipping_amount
        }
        return JsonResponse(data)
    


def buy_now(request):
 return render(request, 'app/buynow.html')


@login_required
def address(request):
 add=customer.objects.filter(user=request.user)
 return render(request, 'app/address.html', {'add': add, 'active': 'btn-primary'})

@login_required
def orders(request):
 op=OrderPlaced.objects.filter(user=request.user)

 return render(request, 'app/orders.html',{'order_placed':op})


def mobile(request, data=None):
    if data == "Sumsung":
        mobiles = Product.objects.filter(category='M', brand='Sumsung')
    elif data == "Apple":
        mobiles = Product.objects.filter(category='M', brand='Apple')
    elif data == "moto-rola":
        mobiles = Product.objects.filter(category='M', brand='moto-rola')
    elif data == "below":
        mobiles = Product.objects.filter(category='M', discounted_price__lt=1000)
    elif data == "above":
        mobiles = Product.objects.filter(category='M', discounted_price__gt=1000)
    else:
        mobiles = Product.objects.filter(category='M')  # Default case (all mobiles)

    return render(request, 'app/mobile.html', {'mobiles': mobiles})

def laptop(request, data=None):
    if data == "laptop":
        laptops = Product.objects.filter(category='L', brand='Sumsung')
    else:
        laptops = Product.objects.all()  # Default case (all products)

    return render(request, 'app/laptop.html', {'laptops': laptops})

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
   def get(self,request):
      form=CustomerRegistrationForm()
      return render(request,'app/customerregistration.html',{'form':form})
   def post(self,request):
      form=CustomerRegistrationForm(request.POST)
      if form.is_valid():
        messages.success(request,'Congratulations!! Registered Successfully')
        form.save()
        return redirect('customerregistration')
      return render(request,'app/customerregistration.html',{'form':form})

# def checkout(request):
#   user=request.user
#   add=customer.objects.filter(user=user)
#   cart_items=Cart.objects.filter(user=user)
#   amount=0.0
#   shipping_amount=70.0
#   cart_product=[p for p in Cart.objects.all() if p.user==request.user]
#   if cart_product:
#         for p in cart_product:
#             tempamount = (p.quantity * p.product.discounted_price)
#             amount += tempamount
#         total_amount = amount + shipping_amount
#   return render(request,'app/checkout.html',{'add':add,'amount':amount ,'shipping_amount':shipping_amount,'total_amount':total_amount,'cart_items':cart_items})

@login_required
def checkout(request):
    user = request.user
    add = customer.objects.filter(user=user)
    cart_items = Cart.objects.filter(user=user)

    amount = 0.0
    shipping_amount = 70.0
    total_amount = amount + shipping_amount  # ✅ default value

    cart_product = [p for p in Cart.objects.all() if p.user == request.user]

    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity * p.product.discounted_price)
            amount += tempamount
        total_amount = amount + shipping_amount   # ✅ updated value

    return render(request, 'app/checkout.html', {
        'add': add,
        'amount': amount,
        'shipping_amount': shipping_amount,
        'total_amount': total_amount,
        'cart_items': cart_items
    })

def payment_done(request):
    user=request.user
    custid=request.GET.get('custid')
    Customer=customer.objects.get(id=custid)
    cart=Cart.objects.filter(user=user)
    for c in cart:
        OrderPlaced(user=user,customer=Customer,product=c.product,quantity=c.quantity).save()
        c.delete()
    return redirect("orders")



from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # or wherever you want

class profileView(View):
    def get(self, request):
       form = CustomerProfileForm()
       return render(request, 'app/profile.html', {'form': form,'active': 'btn-primary'})
    def post(self, request):
       form = CustomerProfileForm(request.POST)
       if form.is_valid():
           usr= request.user
           # Check if customer already exists
           name=form.cleaned_data['name']
           locality=form.cleaned_data['locality']
           city=form.cleaned_data['city']
           state=form.cleaned_data['state']
           zipcode=form.cleaned_data['zipcode']
           reg=customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
           reg.save()
           messages.success(request, 'Profile Updated Successfully!!')
       return render(request, 'app/profile.html', {'form': form,'active': 'btn-primary'})