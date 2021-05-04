from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail
from django.db.models import Q
from .models import MenuItem, Category, OrderModel
# Create your views here.
class Index(View):
	def get(self,request,*args,**kwargs):
		return render(request,'customer/index.html')

class About(View):
	def get(self,request,*args,**kwargs):
		return render(request,'customer/about.html')

class Order(View):
	def get(self, request, *args, **kwargs):
		pizzas = MenuItem.objects.filter(category__name__contains='pizzas')
		desserts = MenuItem.objects.filter(category__name__contains='desserts')
		drinks = MenuItem.objects.filter(category__name__contains='drinks')

		#pass into context
		context =  {
		    'pizzas': pizzas,
		    'desserts': desserts,
		    'drinks': drinks,
		}

		#render the template
		return render(request, 'customer/order.html', context)
	def post(self,request, *args, **kwargs):
		name = request.POST.get('name')
		email = request.POST.get('email')
		street = request.POST.get('street')
		city = request.POST.get('city')
		state = request.POST.get('state')
		zip_code = request.POST.get('zip')

		order_items = {
		     'items':[]
		}

		items = request.POST.getlist('items[]')
		
		for item in items:
			menu_item = MenuItem.objects.get(pk=int(item))
			item_data = {
			    'id':menu_item.pk,
			    'name':menuItem.name,
			    'price':menu_item.price,
			}

			order_items['items'].append(item_data)

			price = 0
			item_ids = []

			for item in order_items['items']:
			    price += item['price']
			    item_ids.append(item[id])

			order = OrderModel.objects.create(
				price=price,
            	name=name,
            	email=email,
            	street=street,
            	city=city,
            	state=state,
            	zip_code=zip_code
			)

			order.items.add(*item_id)
			body = ('Thank you for your order!  Your food is being made and will be delivered soon!\n'
        	f'Your total: {price}\n'
        	'Thank you again for your order!')
        	
			context = {
			    'items': order_items['items'],
			    'price': price
			 }

			return render(request,'customer/order_confirmation.html', context)

class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()

        context = {
            'menu_items': menu_items,
        }

        return render(request, 'customer/menu.html', context)

class MenuSearch(View):
    def get(self, request, *args, **kwargs):
    	query = self.request.GET.get("q")

    	menu_items = MenuItem.objects.filters(
    	
    		
    	)
    	return render(request, 'customer/menu.html',context)






