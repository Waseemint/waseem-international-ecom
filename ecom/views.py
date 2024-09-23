from django.shortcuts import render, redirect
from store.models import Product, ReviewRating
from youtube.models import Video
from ads.models import AdBannerThree, HomePageBannersTwo
from category.models import ParentCategory, ChildCategory
import random

from django.core.mail import send_mail
from django.contrib import messages
from django import forms


def home(request):

    category_child = ChildCategory.objects.filter(home=True)

    reviews = None
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')
    for product in products:
        reviews = ReviewRating.objects.filter(product_id=product.id, status=True)
    videos = Video.objects.all().order_by('-id')
    ad_banner_three = AdBannerThree.objects.all().order_by('-id')
    homepagebanner = HomePageBannersTwo.objects.all().order_by('-id')
    banners = HomePageBannersTwo.objects.all()  # Get first two banners



    context = {'products': products,
               'reviews': reviews,
               'videos':videos,
               'ad_banner_three':ad_banner_three,
               'homepagebanner':homepagebanner,
               'banners':banners,
               'category_child':category_child,
               }
    return render(request, 'home.html',context)



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    mobile = forms.CharField(max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Enter your email address'}))
    order_number = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': 'Enter your order number'}))
    question = forms.ChoiceField(choices=[
        ('', 'Select a question'),
        ('tracking', 'I need help tracking my order'),
        ('exchange', 'I want to return or Exchange my Order'),
        ('payment', 'I can\'t checkout with payment method'),
        ('sale', 'I have a product of sale inquiry'),
        ('login', 'Can you help me with account login'),
        ('other', 'Other'),
    ], required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            mobile = form.cleaned_data['mobile']
            email = form.cleaned_data['email']
            order_number = form.cleaned_data['order_number']
            question = form.cleaned_data['question']
            message = form.cleaned_data['message']

            try:
                send_mail(
                    subject=f"Contact Form Submission: {question}",
                    message=f"Name: {name}\nMobile: {mobile}\nEmail: {email}\nOrder Number: {order_number}\nQuestion: {question}\nMessage: {message}",
                    from_email=email,
                    recipient_list=['waseemint.pk@gmail.com'],  # replace with your email address
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully. We will get back to you soon.')
                return redirect('contact')
            except:
                messages.error(request, 'There was an error sending your message. Please try again later.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

