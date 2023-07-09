from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'main/contacts.html')


def categories(request):
    return render(request, 'main/categories.html')


def orders(request):
    return render(request, 'main/orders.html')
