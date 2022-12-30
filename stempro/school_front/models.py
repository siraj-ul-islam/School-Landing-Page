from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class IndexPage(models.Model):
    # section 1
    main_heading = models.CharField(_("Main Heading"), max_length=500, default="Building Powerful Minds Through Mathematics")
    main_description = models.TextField(_("Hero Description"), default="""Our award winning K-12 after-school math program has empowered students to achieve excellence for over twenty years.""")
    main_side_image = models.ImageField(_("Side Image"), help_text="Upload PNG", upload_to='uploads', default="https://russianschool-tinypng.s3.us-east-1.amazonaws.com/uploads/home2-min1576261723-2x1583938060-2x.1584953668_1x.png")
    # section 2
    rsm_online = models.CharField(_("Title"), max_length=50, default="RSM Online")
    rsm_phone = models.CharField(_("Phone No"), max_length=50, default="(617) 362 3500")
    rsm_link = models.URLField(_("Link"), max_length=50, default="online.elementary@russianschool.com")
    # section 3
    main_heading_2 = models.CharField(_("Main Heading 2"), max_length=500, default="We use the rigorous study of mathematics as a vehicle to develop our students’ math fluency, intellect, and character, empowering them for life.")
    # section 4
    our_program_heading = models.CharField(_("Header"), max_length=50, default="Our Programs")
    our_program_description = models.TextField(_("Description"), default="""With multiple levels for every grade as well as a selective competitions program, we are able to best serve each child’s development based on his or her knowledge and ability.""")
    # section 5
    our_result_heading = models.CharField(_("Header"), max_length=50, default="Our Results")
    our_result_description = models.TextField(_("Description"), default="""Our students post remarkable scores on math competitions, see higher grades in school, and build a lasting confidence in their math and learning abilities overall.""")


class Result(models.Model):
    page = models.ForeignKey(IndexPage, verbose_name=_("Page"), on_delete=models.CASCADE)
    result_heading = models.TextField(_("Heading"), default="A+")
    description = models.CharField(_("Description"), max_length=50, default="Our students experience soaring confidence and grades")

    def __str__(self):
        return f"{self.result_heading}"

class Review(models.Model):
    page = models.ForeignKey(IndexPage, verbose_name=_("Page"), on_delete=models.CASCADE)
    review_content = models.TextField(_("Review"), default="Students are required to think their way through logic problems that can be resolved only with creative use of the math they’ve learned.")
    reviewer = models.CharField(_("Reviewer"), max_length=50, default="The Boston Globe")

    def __str__(self):
        return f"{self.reviewer}"
    


class Program(models.Model):
    name = models.CharField(_("Program Name"), max_length=150, default="Elementary (K-2)")
    hero_image = models.ImageField(_("Hero Image"), upload_to='uploads', default="static/images/uploads/early-elementary-hero-2880x1428.1575476978_2x.jpg")

    heading_1 = models.CharField(_("Main Heading"), max_length=150, default="Start Early. Learn Deeply.")
    description_1 = models.TextField(_("Main Description"), default="Spark an early interest in mathematics and lay the groundwork for higher level reasoning.")

    heading_2 = models.CharField(_("Sub Heading"), max_length=450, default="We nurture the natural flexibility and curiosity of young minds to spark an interest in math and lay the foundations of higher level reasoning and logical thinking.")
    description_2 = models.TextField(_("Sub Description"), default="Young children are naturally curious, uninhibited, and can easily grasp very complex ideas. Our curriculum and methodology are built with this in mind. Our students learn to work with, and develop an appetite for, challenging mathematical concepts.")
