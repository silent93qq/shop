from shop.models import ProductCategory

def category(request):
    return {"category_list": ProductCategory.objects.all()}
