from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, OrderForm
from django.core.mail import send_mail

# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            messages.success(request, 'Message Submitted!')
            send_mail(
                'Contact Message received',
                'Checkout the message on the admin panel Now!',
                'info.edunes@gmail.com',
                ['examchecker7@gmail.com'],
                fail_silently=False,
            )
            return redirect('blog-home')
    else:
        form = ContactForm()
    return render(request, 'blog/index.html', {'form': form})


def order_checker(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form_save = form.save()
            send_mail(
                'Order received',
                'Checkout the order on the admin panel Now!',
                'info.edunes@gmail.com',
                ['examchecker7@gmail.com'],
                fail_silently=False,
            )
            return redirect('blog-order-checker')
    else:
        form = OrderForm()
    return render(request, 'blog/checker_order.html', {'form': form})


def payment(request):
    return render(request, 'blog/payment.html')
