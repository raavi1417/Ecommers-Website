from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact,Order,orderUpdate
from math import ceil
import json
# Create your views here.
def index(request):
    params={}
    product=Product.objects.all()
   
    allprod=[]
    catprod=Product.objects.values('cat','id')
    cats={item['cat'] for item in catprod}
    for category in cats:
        prod=Product.objects.filter(cat=category)
        n=len(product)
        nslide=n//4 + ceil((n/4)-(n//4))
        allprod.append([prod,range(1,nslide),nslide])
    #params={'no_of_slide':nslide,'range':range(nslide),'product':product}
    #allprod=[[product,range(1,nslide),nslide],
     #        [product,range(1,nslide),nslide]
    #]
    params={'allprod':allprod}
    return render(request,'shop/index.html',params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
     if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST['phone']
        message=request.POST['message']
        if name == "":
            return HttpResponse('''<script>alert("Please Enter Name"); location.href='/shop/contact'</script>''')
        elif email=="":
            return HttpResponse('''<script>alert("Please Enter Email"); location.href='/shop/contact'</script>''')
        elif phone == "":
            return HttpResponse('''<script>alert("Please Enter Mobile"); location.href='/shop/contact.html'</script>''')
        elif message == "":
            return HttpResponse('''<script>alert("Please Enter Message");location.href='/shop/contact.html''')
        else:
            contact=Contact(name=name,email=email,phone=phone,message=message)
            contact.save()
            return HttpResponse('''<script> alert("Thank You");document.location='/shop'</script>''')
     return render(request,'shop/contact.html')

def tracker(request):
    if request.method == 'POST':
        orderId=request.POST['orderId']
        email=request.POST['email']
        try:
            order=Order.objects.filter(order_id=orderId,email=email)
            if len(order)>0:
                update=orderUpdate.objects.filter(order_id=orderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps([updates,order[0].item_json],default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse('{}')
    return render(request,'shop/tracker.html')

def search(request):
     return render(request,'shop/search.html')

def productview(request,myid):
     product=Product.objects.filter(id=myid)
     params={'product':product[0]}
     return render(request,'shop/prod_view.html',params)

def checkout(request):
    if request.method == 'POST':
        item_json=request.POST['item_json']
        name=request.POST['name']
        email=request.POST['email']
        address1=request.POST['address1']
        address2=request.POST['address2']
        city=request.POST['city']
        state=request.POST['state']
        zip_code=request.POST['zip_code']
        phone=request.POST['phone']
        alter_phone=request.POST['alter_phone']
        checkout=Order(item_json=item_json,name=name,email=email,address1=address1,address2=address2,city=city,
            state=state,zip_code=zip_code,phone=phone,alter_phone=alter_phone)
        checkout.save()
        thank=True
        update=orderUpdate(order_id=checkout.order_id,update_desc="Order has been Placed")
        update.save()
        id=checkout.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})

    return render(request,'shop/checkout.html')



