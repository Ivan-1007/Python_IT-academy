from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.response import HttpResponseRedirect
from django.views.generic.detail import DetailView
from .models import Order, OrderStatus
from django.views.generic import FormView, ListView, UpdateView, RedirectView, TemplateView
from .forms import OrderForm, OrderManagerForm
from carts.models import Cart
from django.urls.base import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# Create your views here.
class CreateOrderView( FormView):
    
    form_class = OrderForm
    template_name = 'orders/order.html'
    success_url = reverse_lazy('orders:list')

    def get_initial(self):
        user = self.request.user
        if user.is_anonymous:
            return
        profile = user.profile
        pn = profile.phonenumber
        information = f'{profile.country},'
        if profile.city and profile.adress_1 and profile._code:
            information += f'г.{profile.city}, {profile.adress_1}, {profile.post_code}'
        return {'phone_number':pn, 'information':information}
     
    def form_valid(self, form):
        cart_id = self.request.session.get('cart_id')
        cart = Cart.objects.get(pk=cart_id)
        status = OrderStatus.objects.get(name='новый')
        phone_number = form.cleaned_data.get('phone_number')
        information = form.cleaned_data.get('information')
        order = Order.objects.create(
            cart=cart,
            phone_number=phone_number,
            status=status,
            information=information,
        )
        del self.request.session['cart_id']
        print('hello*****************************************************************')
        messages.add_message(self.request, messages.INFO, f'{self.request.user}, Ваш заказ принят!')
        return HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        cart = Cart.objects.get(pk=int(self.request.session.get('cart_id')))
        cnt['object']=cart
        return cnt


class OrderListView(ListView):
    template_name = 'orders/order_list.html'
    model = Order

    def get_context_data(self, **kwargs):
        user = self.request.user
        carts = user.carts.all()
        orders = Order.objects.order_by('-created').filter(cart__in=carts)
        cnt = {'object_list':orders}
        return cnt
    

class OrderManagerListView(PermissionRequiredMixin, ListView):
    template_name = 'orders/manager/order_list.html'
    model = Order
    login_url = '/users/login/'
    permission_required = 'orders.change_order'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created')
        status = self.request.GET.get('status')
        if status:
            queryset = queryset.all().filter(status__pk = status)
        print(queryset)
        return queryset


class OrderManagerUpdateView(PermissionRequiredMixin, UpdateView):
    model = Order
    template_name = 'orders/manager/order_update.html'
    form_class = OrderManagerForm
    success_url = reverse_lazy('orders:m_list')
    permission_required = 'orders.change_order'

    def get_context_data(self, **kwargs):
        cnt = super().get_context_data(**kwargs)
        order_pk = self.kwargs['pk']
        cart = Order.objects.get(pk=order_pk).cart
        cnt['cart'] = cart
        return cnt
    

class CancelOrderView(RedirectView):    
    def post(self, request, *args, **kwargs):
        order_pk = kwargs.get('pk')
        order = Order.objects.get(pk=order_pk)
        order_status = OrderStatus.objects.get(name='отменен')
        order.status = order_status
        order.save()
        return HttpResponseRedirect(reverse_lazy('orders:list'))


class CommentOrderView(DetailView):
    template_name = 'orders/comment.html'
    model = Order
