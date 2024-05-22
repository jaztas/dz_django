from django.shortcuts import render

def home(request):
	return render(request, 'catalog/home.html')

def contacts(request):
	if request.method == 'POST':
		name = request.POST.get['name']
		email = request.POST.get['email']
		message = request.POST.get['message']
		return render(request, 'catalog/contacts.html', {'name': name, 'email': email, 'message': message})
	return render(request, 'catalog/contacts.html')
