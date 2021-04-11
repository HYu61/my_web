from django.shortcuts import render
from .models import Certification, HomePageFooterContent
from projects.models import Projects, Categories


def nav_info():
    # project_list=Projects.objects.all().filter(published=True)
    certificates = Certification.objects.all()
    certificates = certificates if certificates.count() > 0 else None
    project_cate = Categories.objects.all()
    result = {
        'cert_list': certificates,
        'cate_list': project_cate,
    }
    return result


def home_page_and_footer_info():
    home_page_info = HomePageFooterContent.objects.get(pk=1)
    result = {
        'home_page_content': home_page_info.content,
        'footer_content': home_page_info.footer
    }
    return result


def index(request):
    project_list = Projects.objects.all().filter(published=True)
    # home_page_info = HomePageContent.objects.get(name='home_page_info')
    # home_page_info = home_page_and_footer_info()
    # display_info = {'home_page_info': home_page_info,'project_list': project_list}
    display_info = {'project_list': project_list}

    display_info.update(nav_info())
    display_info.update(home_page_and_footer_info())

    return render(request, 'index.html', display_info)
