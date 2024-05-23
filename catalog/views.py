from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
	return render(request, 'catalog/home.html')


def contacts(request):
	if request.method == 'POST':
		name = request.POST.get['name']
		email = request.POST.get['email']
		message = request.POST.get['message']
		return render(request, 'catalog/contacts.html', {'name': name, 'email': email, 'message': message})
	return render(request, 'catalog/contacts.html')


def products(request):
	product = Product.objects.all
	context = {
		'object_list': product,
		'title': 'Товары'
	}
	return render(request, 'catalog/products.html', context=context)


def product(request, pk):
	context = {
		'object_list': Product.objects.get(pk=pk)
	}
	return render(request, 'catalog/product.html', context=context)
