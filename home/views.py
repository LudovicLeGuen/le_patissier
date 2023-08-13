from django.shortcuts import render, redirect

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
