from django.shortcuts import render, get_object_or_404
from .models import Projects, Categories
from portfolio.views import nav_info, home_page_and_footer_info


# Create your views here.
def get_project_by_cate(request, cate_name):
    projects_list = Projects.objects.all().filter(cate__cate_name=cate_name)
    result = {'cate_name': cate_name, 'project_list': projects_list}
    result.update(nav_info())
    result.update(home_page_and_footer_info())
    return render(request, 'home.html', result)


def project_detail(request, project_id):
    project = get_object_or_404(Projects, pk=project_id)
    # cate_name = projects.cate
    result = {'project': project}
    result.update(nav_info())
    result.update(home_page_and_footer_info())
    return render(request, 'detail.html', result)
