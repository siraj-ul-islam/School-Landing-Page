from django.contrib import admin
from .models import IndexPage, Program, Result, Review

class ReviewInllineAdmin(admin.TabularInline):
    model = Review
    extra = 0
    fields = ("review_content", "reviewer")

class ResultInllineAdmin(admin.TabularInline):
    model = Result
    extra = 0
    fields = ("result_heading","description")


@admin.register(IndexPage)
class IndexPageAdmin(admin.ModelAdmin):
    '''Admin View for IndexPage'''

    list_display = ('main_heading','rsm_phone')
    inlines = [
        ResultInllineAdmin,
        ReviewInllineAdmin,
    ]

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    '''Admin View for Program'''

    list_display = ('heading_1',)
    # inlines = [
    #     ResultInllineAdmin,
    #     ReviewInllineAdmin,
    # ]