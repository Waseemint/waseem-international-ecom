from .models import MainCategory, ParentCategory, ChildCategory

def categories_processor(request):
    main_categories = MainCategory.objects.all().order_by('id')
    parent_categories = ParentCategory.objects.all().order_by('id')
    child_categories = ChildCategory.objects.all().order_by('id')

    return {
        'main_categories': main_categories,
        'parent_categories': parent_categories,
        'child_categories': child_categories,
    }
