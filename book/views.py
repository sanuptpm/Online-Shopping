from django.shortcuts import render
from django.shortcuts import redirect
from book.models import Catagory
from book.models import Product 
from book.models import Cart
from book.models import UserProfile
from book.forms import UserRegistrationForm
from book.forms import UserProfileUpdateForm
from book.forms import ChangePasswordForm
from book.forms import ProductForm
from book.forms import OrderCancelForm
from book.forms import CatagoryForm
from book.forms import DeliveyStatusForm
#from book.forms import PincodeForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail


def user_home(request):
    catagory=Catagory.objects.all()
    return render(request,'home.html',{'catagory':catagory})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
def condition(request):
    return render(request,'condition.html')

def add_user(request):
    username = request.POST.get("username")
    email = request.POST.get("emailid")
    password = request.POST.get("password")
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    address = request.POST.get("address")
    phone = request.POST.get("phone")
    print ".........address........",address
    if request.method == 'GET':
        form = UserRegistrationForm() #object creation
    else:
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
              user = User.objects.create_user(username, email, password)
              user.first_name = fname
              user.last_name = lname
              user.save()
              a = UserProfile(user_id=user.id,address=address,phone=phone)
              a.save()
              return redirect('/users/home')
    return render(request, 'registration.html', {'form': form,})
@login_required
def user_account(request):
    return render(request,'account.html')
@login_required
def change_password(request):
    newpassword = request.POST.get("newpassword")
    renewpasssword = request.POST.get("renewpasssword")
    username=request.user.username
    if newpassword == renewpasssword:
        if request.method == 'GET':
            form = ChangePasswordForm()
        else:
            u = User.objects.get(username__exact=username)
            u.set_password(newpassword)
            u.save()
            return redirect('/users/account')
    else:
        return redirect('/change/password/')
    return render(request,'changepassword.html', {'form': form,})


@login_required
def add_product(request):
    cid = request.POST.get("cname")
    if request.method == 'GET':
        form = ProductForm()
    else:
         form = ProductForm(request.POST, request.FILES)
         if form.is_valid():               
                 user=User.objects.get(pk=request.user.id)
                 catagory=Catagory.objects.get(id = cid)        
                 p = Product(pname=request.POST.get("pname"),discription=request.POST.get("discription"),
                                price=request.POST.get("price"),noitem=request.POST.get("noitem"),createdby=user,cid=catagory,
                                photo=request.FILES['photo'])#save photo
                 p.save()
                 return redirect('/users/account/')    
    return render(request, 'addproduct.html', {'form':form})


@login_required
def del_product(request):
    productname=Product.objects.all()
    pname = request.POST.get('dropdown1')
    if request.method == 'GET':
        form = ProductForm()
    else:
        product = Product.objects.get(pname = pname)
        product.delete()
        return redirect('/users/account/')
    return render(request, 'delproduct.html', {'form':form, 'productname':productname})

@login_required
def add_catagory(request):
    cname=request.POST.get('cname')     
    if request.method == 'GET':
        form = CatagoryForm() 
    else:
         form = CatagoryForm(request.POST)
         if form.is_valid():
             u = User.objects.get(pk=request.user.id)
             #u=request.user.id
             u.catagory_set.create(cname=cname,purdate=timezone.now())
             return redirect('/users/account/')
    return render(request, 'addcatagory.html', {'form': form})

@login_required
def del_catagory(request):
    catagoryname=Catagory.objects.all()
    cname = request.POST.get('dropdown1')
    if request.method == 'GET':
        form = CatagoryForm() 
    else:
        catagory = Catagory.objects.get(cname = cname)
        catagory.delete()
        return redirect('/users/account/')
    return render(request, 'delcatagory.html', {'form': form, 'catagoryname':catagoryname})

@login_required
def details(request,products_id):
    user=User.objects.get(pk=request.user.id)
    product=Product.objects.filter(pk=products_id)
    pid=Product.objects.get(pk=products_id)
    item = request.POST.get("noitems")
    if request.method == 'POST':
        print "data added to cart"
        user.cart_set.create(uid = user,pid = pid,noitem = item,purdate = timezone.now(),deldate = timezone.now())
        pid.noitem = pid.noitem - float(item)
        pid.save()
        return redirect('/users/account/')
    return render(request,'details.html',{'product':product})


def products_home(request,catagory_id):
    products=Product.objects.filter(cid=catagory_id)
    return render(request,'producthome.html',{'products':products})

@login_required
def profile_update(request):
    fname = request.POST.get("fname")
    lname = request.POST.get("lname")
    email = request.POST.get("emailid")
    address = request.POST.get("address")
    phone = request.POST.get("phone")
    username=request.user.username
    if request.method == 'GET':
        profile = UserProfileUpdateForm() #object creation

    else:
         profile = UserProfileUpdateForm(request.POST)
         if profile.is_valid():
             user = User.objects.get(pk=request.user.id)
             user.first_name = fname
             user.last_name = lname
             user.email= email
             user.save()
             usr = UserProfile.objects.get(user_id=request.user.id)
             usr.address = address
             usr.phone = phone
             usr.save()
             return redirect('/users/account/')
    return render(request, 'profile.html', {'profile': profile,})
    
@login_required
def personal_details(request):
    user = User.objects.get(pk=request.user.id)
    profile = UserProfile.objects.get(user_id=request.user.id)
    return render(request, 'personaldetails.html', {'profile': profile,'user':user})


@login_required
def my_cart(request):
    carts = Cart.objects.filter(uid = request.user.id).values('pid','noitem','purdate','status')
    #print "........",type(carts)
    products=Product.objects.all()
    return render(request, 'mycart.html', {'carts': carts, 'products': products,})
@login_required
def cancel_order(request):

    cart = Cart.objects.filter(uid = request.user.id).values('pid','noitem','id')
    product=Product.objects.all()
    order = request.POST.get('oname')
    if request.method == 'GET':
        form = OrderCancelForm()
    else:
         form = OrderCancelForm(request.POST)
         if form.is_valid():
            cart = Cart.objects.get(id = order)
            cart.delete()
            return redirect('/users/account/')
    return render(request, 'cancelorder.html', {'cart': cart, 'product': product, 'form':form})

@login_required
def products_delivery(request):
    cart = Cart.objects.all().values('id','uid','pid','noitem','purdate','status')
    product=Product.objects.all()
    userid = Cart.objects.all().values('uid')  
    user = User.objects.all()
    status = request.POST.get("status")
    deliveryid = request.POST.get("deliveryid")
    if request.method == 'GET':
        form = DeliveyStatusForm()
    else:
         form = DeliveyStatusForm(request.POST)
         if form.is_valid():
             cartid = Cart.objects.get(id=deliveryid)          
             cartid.status = status
             cartid.save()
             return redirect('/products/delivary/')
    return render(request, 'delivery.html', {'cart': cart, 'product': product, 'form': form,'user':user})







    
