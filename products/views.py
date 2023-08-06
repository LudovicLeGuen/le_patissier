from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Brand, Review
from .forms import ProductForm, ReviewForm


# All copied from Ado Boutique
def all_products(request):
    """ This view shows all products, sorts and searches """

    products = Product.objects.all()
    query = None
    categories = None
    brands = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search criteria")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ This view shows individual product details """

    product = get_object_or_404(Product, pk=product_id)

    # Rating the products
    # Inspired by Code With Stein: https://www.youtube.com/watch?v=8iCqlFyFu2s
    if request.method == "POST":
        rating = request.POST.get('rating', 3)
        body = request.POST.get('body', '')

        if body:
            reviews = Review.objects.filter(created_by=request.user,
                                            product=product
                                            )

            if reviews.count() > 0:
                review = reviews.first()
                review.rating = rating
                review.body = body
                review.save
                messages.success(request,
                                 f'Your { product.name } review is updated'
                                 )

            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    body=body,
                    created_by=request.user,
                )
                messages.success(request,
                                 f'Thank you for reviewing \
                                 the { product.name }.Your review\
                                 will be soon approved by an Administrator')

            return redirect('product_detail', product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


def all_brands(request):
    """ This view shows all the brands """

    brands = Brand.objects.all()
    products = Product.objects.all()
    marks = None
    sort = None
    direction = None

    if request.GET:

        if 'brand' in request.GET:
            marks = request.GET['name'].split(',')
            products = products.filter(mark__name__in=marks)
            mark = Brand.objects.filter(name__in=mark)

    current_sorting = f'{sort}_{direction}'

    context = {
        'brands': brands,
        'products': products,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/all_brands.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not an admin. NO CAN DO!')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to add product. \
                           Please ensure the form is valid.'
                           )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not an admin. NO CAN DO!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'The {product.name} is successfully updated!'
                             )
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           'Failed to update product. \
                            Please ensure the form is valid.'
                           )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing the {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, you are not an admin. NO CAN DO!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'The {product.name} is deleted!')
    return redirect(reverse('products'))
