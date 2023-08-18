from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def index(request):
    """ This view returns the index page """

    return render(request, 'home/index.html')


def legal(request):
    """
    Legal Statement Page
    """
    return render(request, 'home/legal/legal.html')


def terms_conditions(request):
    """
    Terms and conditions Page
    """
    return render(request, 'home/legal/terms_conditions.html')


def privacy_policy(request):
    """
    Privacy policy Page
    """
    return render(request, 'home/legal/privacy_policy.html')


def guarantee(request):
    """
    Guaranty Statement Page
    """
    return render(request, 'home/legal/guarantee.html')


# Copied from VictoriaT87 level_up_loot project
# https://github.com/VictoriaT87/level_up_loot_vt/tree/main
def contact(request):
    """
    View to return Contact Us form
    """

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you, your message is sent. We will contact you shortly."
            )
            return redirect("contact")
        else:
            messages.error(
                request,
                "Form submission failed. Please check the form and try again."
            )
    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, "home/contact.html", context)
