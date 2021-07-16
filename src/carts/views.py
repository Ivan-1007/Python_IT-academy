from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.views.generic import DetailView, DeleteView, View
from .models import Cart, BookInCart
from books.models import Book as BookModel
from django.urls import reverse_lazy

# Create your views here.

class CartView(DetailView):
    template_name = 'carts/cart.html'
    model = Cart

    def get_object(self, queryset=None):        
        cart_id = self.request.session.get('cart_id')
        cart, created = Cart.objects.get_or_create(
            pk=cart_id,
            defaults={
                'customer': self.request.user if self.request.user.pk else None
            },
        )
        if created:
            self.request.session['cart_id'] = cart.pk
        if not cart.customer and self.request.user.pk:
            cart.customer = self.request.user
            cart.save()

        book_id = self.request.GET.get('book_id')
        if book_id:
            book = BookModel.objects.get(pk=book_id)
            book_in_cart, book_created = BookInCart.objects.update_or_create(
                cart=cart,
                book=book,  
                defaults={
                    'unit_price': book.price
                }
            )
            if not book_created:
                book_in_cart.quantity += 1
                book_in_cart.save()
        return cart


class BookInCartDeleteView(DeleteView):
    model = BookInCart
    success_url = reverse_lazy('carts:cart')


class UpdateCartView(View):
    def post(self, request):
        action = self.request.POST.get('submit')

        cart_id = self.request.session.get('cart_id') or self.request.POST.get('cart_id')
        cart = Cart.objects.get(pk=cart_id)
        books_in_cart = cart.books_in_cart.all()
        for k, v in self.request.POST.items():
            if 'quantity' in k:
                pk = int(k.split('_')[1])
                book_in_cart = books_in_cart.get(pk=pk)
                book_in_cart.quantity = v                
                book_in_cart.save()
        if action == 'checkout':
            return HttpResponsePermanentRedirect(reverse_lazy('orders:create'))
        else:
            if self.request.POST.get('next'):
                return HttpResponsePermanentRedirect(reverse_lazy('orders:update', args=[int(request.POST.get('next')), ] ))
            return HttpResponsePermanentRedirect(reverse_lazy('carts:cart'))