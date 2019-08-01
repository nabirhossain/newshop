from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product





# Create your views here.

def home(request):
    top_level_cats = Category.objects.filter(parent__isnull=True)
    context= {
        'top_level_cats' : top_level_cats
    }
    return render(request, 'product/index.html', context)



def show_category(request,hierarchy= None):
    category_slug = hierarchy.split('/')
    category_queryset = list(Category.objects.all())
    all_slugs = [ x.slug for x in category_queryset ]
    parent = None
    for slug in category_slug:
        if slug in all_slugs:
            parent = get_object_or_404(Category,slug=slug,parent=parent)
        else:
            instance = get_object_or_404(Product, slug=slug)
            breadcrumbs_link = instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs = zip(breadcrumbs_link, category_name)
            return render(request, "product/postDetail.html", {'instance':instance,'breadcrumbs':breadcrumbs})
    return render(request,"product/categories.html",{'post_set':parent.post_set.all(),'sub_categories':parent.children.all()})