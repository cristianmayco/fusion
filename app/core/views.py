from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Service, Employee, Feature
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['services'] = Service.objects.order_by('?').all()
        context['employees'] = Employee.objects.order_by('?').all()
        context['features'] = Feature.objects.order_by('?').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_email()
        messages.success(self.request, 'Email successfully sent')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error sending the e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
