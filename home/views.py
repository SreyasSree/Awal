from django.shortcuts import render , get_object_or_404 , redirect
from .models import Category , Product , Order , OrderItem
from .cart import Cart
from .forms import OrderForm



# Create your views here.

def index(request):
    cat = Category.objects.all()
    pro = Product.objects.all()[:4]
    prod = Product.objects.all()


    context ={
        'cat':cat,
        'pro':pro,
        'prod':prod,
    }
    return render(request ,'index.html' , context)

def about(request):
    return render(request ,'about.html')

def product(request,id=None):
    
    if id:
        cate = get_object_or_404(Category,id=id)
        pro = Product.objects.filter(category=cate)
        cat = Category.objects.all()

        context ={
        'cat':cat,
        'pro':pro,
        'cate':cate,
        }

        return render(request , 'product.html',context)

    else:
        pro =Product.objects.all()
        cat =Category.objects.all()

        context ={
        'cat':cat,
        'pro':pro,
        }
        
        return render(request,'product.html',context)


    cat = Category.objects.all()
    pro = Product.objects.all()

    context ={
        'cat':cat,
        'pro':pro,
    }
    return render(request ,'product.html' , context)


def productsingle(request,id):
    cat = Category.objects.all()
    pro = Product.objects.get(id=id)
    prod = Product.objects.all()


    context ={
        'cat':cat,
        'pro':pro,
        'prod':prod,
    }
    return render(request ,'productsingle.html' , context)



def cart(request):
    cat = Category.objects.all()
    pro = Product.objects.all()

    cart = Cart(request)


    context ={
        'cat':cat,
        'pro':pro,
        'cart':cart,
    }
    return render(request ,'cart.html',context)



def cart_add(request,pk):
    cart = Cart(request)
    cart.add(pk)
   

    return redirect('cart')


def cart_remove(request,pk):
    cart = Cart(request)
    cart.remove(pk)
    return redirect('cart')


def checkout(request):
    cart = Cart(request)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                )
            cart.clear()
            return redirect('home:success')
            


    form = OrderForm()

    context = {
        'form':form,
        'cart':cart,
    }
    return render(request , 'checkout.html' , context)