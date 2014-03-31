from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from forms import ContactForm
from models import Customer, Ambassador, Campaign, Point
from django.core.mail import send_mail
# Create your views here.


class CustomerCreateView(CreateView):
    model = Customer
    fields = ['company_name', 'description', 'contact_person']
    template_name_suffix = '_create_form'


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['company_name', 'description', 'contact_person']
    template_name_suffix = '_update_form'


class CustomerDeleteView(DeleteView):
    model = Customer
    fields = ['company_name', 'description', 'contact_person']
    template_name_suffix = '_delete_form'


class CampaignCreateView(CreateView):
    model = Campaign
    fields = ['company', 'money_pool', 'description']
    template_name_suffix = '_create_form'


class CampaignUpdateView(UpdateView):
    model = Campaign
    fields = ['company', 'money_pool', 'description']
    template_name_suffix = '_update_form'


class CampaignDeleteView(DeleteView):
    model = Campaign
    fields = ['company', 'money_pool', 'description']
    template_name_suffix = '_delete_form'


class AmbassadorCreateView(CreateView):
    model = Ambassador
    fields = ['name', 'twitter', 'facebook', 'google_plus', 'instagram', 'snapchat', 'pinterest']
    template_name_suffix = '_create_form'


class AmbassadorUpdateView(UpdateView):
    model = Ambassador
    fields = ['name', 'twitter', 'facebook', 'google_plus', 'instagram', 'snapchat', 'pinterest']
    template_name_suffix = '_update_form'


class AmbassadorDeleteView(DeleteView):
    model = Ambassador
    fields = ['name', 'twitter', 'facebook', 'google_plus', 'instagram', 'snapchat', 'pinterest']
    template_name_suffix = '_delete_form'


class PointsCreateView(CreateView):
    model = Point
    fields = ['campaign', 'ambassador', 'points']
    template_name_suffix = '_create_form'


class PointsUpdateView(UpdateView):
    model = Point
    fields = ['campaign', 'ambassador', 'points']
    template_name_suffix = '_update_form'


class PointsDeleteView(DeleteView):
    model = Point
    fields = ['campaign', 'ambassador', 'points']
    template_name_suffix = '_delete_form'


class ContactFormView(FormView):
    template_name = 'core/contact.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        cd = form.cleaned_data
        subject = cd['subject']
        message = cd['message']
        sender = cd['sender']
        cc_myself = cd['cc_myself']

        recipients = ['nemesisesq@gmail.com']
        if cc_myself:
            recipients.append(cc_myself)

        send_mail(subject, message, sender, recipients)
        return super(ContactFormView, self).form_valid(form)