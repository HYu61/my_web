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
    # home_page_info = HomePageFooterContent.objects.get(name='home_page_and_footer_info')
    home_page_info = HomePageFooterContent.objects.filter(name='home_page_and_footer_info').first()
    content = 'Hello -- Please modify it by add one entry with the name "home_page_and_footer_info" in the database'
    footer = '<p class="m-0 text-center text-white">Copyright &copy;-- Please modify it by add one entry with the ' \
             'name "home_page_and_footer_info" in the database</p> '
    if home_page_info is not None:
        content = home_page_info.content
        footer = home_page_info.footer
    result = {
        'home_page_content': content,
        'footer_content': footer
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
