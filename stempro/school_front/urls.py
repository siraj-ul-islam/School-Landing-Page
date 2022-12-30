from django.urls import path
from . import views as SVF

urlpatterns = [
    path("", SVF.IndexView.as_view(), name="index_page"),
    path("program/<pk>", SVF.ProgramDetailView.as_view(), name="ProgramDetailView"),
    path("schedule/", SVF.schedule.as_view(), name="schedule"),
    path("<template_name>", SVF.all_templates, name="all_templates"),
    path("<template_dir>/<template_name>", SVF.all_templates_with_dir, name="all_templates_dir"),
    path("<template_dir1>/<template_dir2>/<template_name>", SVF.all_templates_with_dir_dir, name="all_templates_dirs"),
    path("<template_dir1>/<template_dir2>/<template_dir3>/<template_name>", SVF.all_templates_with_dir_dir_dir, name="all_templates_dirs"),
    path("<template_dir1>/<template_dir2>/<template_dir3>/<template_dir4>/<template_name>", SVF.all_templates_with_dir_dir_dir_dir, name="all_templates_dirs"),
]
