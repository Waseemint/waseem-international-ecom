from customkit.models import FooterLink
from customkit.models import Tags, HomeLogo

def footer_links(request):
    return {'footer_links': FooterLink.objects.all()}
def base_tags(request):
    tags = Tags.objects.all().order_by('-id')[:11]
    context = {
        'tags':tags,
    }
    return context


def main_logoo(request):
    logoo = HomeLogo.objects.first()
    context = {
        'logoo_main': logoo,
    }
    return context
