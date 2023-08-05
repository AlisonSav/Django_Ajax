from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django_ajax.forms import ContactForm


def index(request):
    return render(request, "django_ajax/index.html")


def contact_us(request, form, template_name):
    data = dict()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data["subject"],
                form.cleaned_data["message"],
                settings.NOREPLY_EMAIL,
                [form.cleaned_data["from_email"]],
                fail_silently=False,
            )
            data["form_is_valid"] = True
        else:
            data["form_is_valid"] = False
    context = {"form": form}
    data["html_form"] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return contact_us(request, form, "django_ajax/partial_contact_create.html")
