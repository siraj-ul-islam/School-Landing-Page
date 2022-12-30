import json

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import IndexPage, Program
# Create your views here.


class IndexView(TemplateView):
    template_name = "school_front/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        page = IndexPage.objects.first()
        programs = Program.objects.all()
        context["page"] = page
        context["programs"] = programs
        return context



class ProgramDetailView(DetailView):
    template_name = "school_front/programs/elementary.html"
    model = Program
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        page = IndexPage.objects.first()
        programs = Program.objects.all()
        context["page"] = page
        context["programs"] = programs
        return context

def all_templates(request, template_name):
    template_name = f"school_front/{template_name}"
    return render(request, template_name)


def all_templates_with_dir(request, template_dir, template_name):
    template_name = f"school_front/{template_dir}/{template_name}"
    return render(request, template_name)

def all_templates_with_dir_dir(request, template_dir1, template_dir2, template_name):
    template_name = f"school_front/{template_dir1}/{template_dir2}/{template_name}"
    return render(request, template_name)

def all_templates_with_dir_dir_dir(request, template_dir1,template_dir2,template_dir3, template_name):
    template_name = f"school_front/{template_dir1}/{template_dir2}/{template_dir3}/{template_name}"
    return render(request, template_name)

def all_templates_with_dir_dir_dir_dir(request, template_dir1, template_dir2, template_dir3, template_dir4, template_name):
    template_name = f"school_front/{template_dir1}/{template_dir2}/{template_dir3}/{template_dir4}/{template_name}"
    return render(request, template_name)

class schedule(TemplateView):
    template_name = "school_front/locations/online/schedule.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)

        data = {

            'schooldate':{
                'id': 5328,
                'location_id': 1,
                'name': "Grade 2 Accelerated Nwwwww 2",
                'course_id': 15,
                'curriculum_id': 0,
                'semester_id': 1087,
                'semester_school_period': 20231,
                'availability': "1",
                'class_type': "online",
                'semester': None,
                'status': "spots_1",
                'description': "",
                'link': "parents.russianschool.com\/enroll?branch_id=18&semester_id=1087",
                'start_time': "16:00:00",
                'start_date': "2022-08-27",
                'end_time': "18:00:00",
                'end_date': "2023-06-09",
                'price': 0,
                'lowest_grade': 3,
                'grades': [3],
                'lowest_day': 5,
                'days': [5],
                'timezone_abbr': "",
                'rsm_branch_id': "",
            },
            'schooldate':{
                'id': 5328,
                'location_id': 1,
                'name': "Grade 2 Accelerated Nwwwww 2",
                'course_id': 15,
                'curriculum_id': 0,
                'semester_id': 1087,
                'semester_school_period': 20231,
                'availability': "1",
                'class_type': "online",
                'semester': None,
                'status': "spots_1",
                'description': "",
                'link': "parents.russianschool.com\/enroll?branch_id=18&semester_id=1087",
                'start_time': "16:00:00",
                'start_date': "2022-08-27",
                'end_time': "18:00:00",
                'end_date': "2023-06-09",
                'price': 0,
                'lowest_grade': 3,
                'grades': [3],
                'lowest_day': 5,
                'days': [5],
                'timezone_abbr': "",
                'rsm_branch_id': "",
            },
            'schooldate':{
                'id': 5328,
                'location_id': 1,
                'name': "Grade 2 Accelerated Nwwwww 2",
                'course_id': 15,
                'curriculum_id': 0,
                'semester_id': 1087,
                'semester_school_period': 20231,
                'availability': "1",
                'class_type': "online",
                'semester': None,
                'status': "spots_1",
                'description': "",
                'link': "parents.russianschool.com\/enroll?branch_id=18&semester_id=1087",
                'start_time': "16:00:00",
                'start_date': "2022-08-27",
                'end_time': "18:00:00",
                'end_date': "2023-06-09",
                'price': 0,
                'lowest_grade': 3,
                'grades': [3],
                'lowest_day': 5,
                'days': [5],
                'timezone_abbr': "",
                'rsm_branch_id': "",
            },
            'schooldate':{
                'id': 5328,
                'location_id': 1,
                'name': "Grade 2 Accelerated Nwwwww 2",
                'course_id': 15,
                'curriculum_id': 0,
                'semester_id': 1087,
                'semester_school_period': 20231,
                'availability': "1",
                'class_type': "online",
                'semester': None,
                'status': "spots_1",
                'description': "",
                'link': "parents.russianschool.com\/enroll?branch_id=18&semester_id=1087",
                'start_time': "16:00:00",
                'start_date': "2022-08-27",
                'end_time': "18:00:00",
                'end_date': "2023-06-09",
                'price': 0,
                'lowest_grade': 3,
                'grades': [3],
                'lowest_day': 5,
                'days': [5],
                'timezone_abbr': "",
                'rsm_branch_id': "",
            },


        }
        context["data"] = data
        return context

        # print(data)
        # return render(request, 'school_front/locations/online/schedule.html' ,{'data':data,})



def about_index_page():
    pass