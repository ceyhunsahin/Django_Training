# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from courses.models import Course
from pages.forms import ContactForm
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.admin import User

# def index(request) :
#     return render(request, 'index.html' )


class AboutView(TemplateView) :
    template_name = 'about.html'

class IndexView (TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True).order_by('-date')[:2]
        context['total_course'] = Course.objects.filter(available=True).count()
        context['total_students'] = User.objects.count()

        return context

class ContactFormView(SuccessMessageMixin,FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = "We received your request"

    def form_valid(self, form):
        form.save()
        form.send_email ()
        return super().form_valid(form)

