from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from courses.models import Course
from pages.forms import ContactForm
from django.views.generic.edit import FormView

# def index(request) :
#     return render(request, 'index.html' )
# def about(request) :
#     return render(request, 'about.html' )

class AboutView(TemplateView) :
    template_name = 'about.html'

class IndexView (TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.filter(available=True).order_by('-date')[:2]
        context['total_course'] = Course.objects.filter(available=True).count()
        # context['total_students'] = User.objects.count()
        return context

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

