from datetime import date

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from .forms import *

from .filters import PersonFilter
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin, SingleTableView

from django.contrib.auth.decorators import login_required

from .tables import PersonTable

import io
from django.http import FileResponse





from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors

from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak, Image, Spacer, Table, TableStyle)
from reportlab.lib.pagesizes import portrait
from reportlab.lib.pagesizes import letter

from reportlab.platypus import Table, TableStyle
from datetime import date

from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet

from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

# multipage form section
from django.http import HttpResponseRedirect
from formtools.wizard.views import SessionWizardView

FORMS = [
    # ('info', ContactForm1),
    # ('message', ContactForm2),
    # ('creditcard', ContactForm3),
    ('newstudent0', NewStudent0),
    ('newstudent1', NewStudent1),
    ('newstudent2', NewStudent2),
    # ('newstudent3', NewStudent3),
    # ('newstudent4', NewStudent4),
    # ('newstudent5', NewStudent5),
]

TEMPLATES = {
    # 'info': 'keypadcodes/contact_info.html',
    # 'info': 'keypadcodes/newstudent0.html',
    # 'message': 'keypadcodes/contact_message.html',
    # 'creditcard': 'keypadcodes/contact_creditcard.html',
    'newstudent0': 'keypadcodes/newstudent0.html',
    'newstudent1': 'keypadcodes/newstudent1.html',
    'newstudent2': 'keypadcodes/newstudent2.html',
    # 'newstudent3': 'keypadcodes/newstudent3.html',
    # 'newstudent4': 'keypadcodes/newstudent4.html',
    # 'newstudent5': 'keypadcodes/newstudent5.html',
}


class ContactWizard(SessionWizardView):

    # file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'files_temp'))
    instance = None

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def get_form_instance(self, step):
        """
        get ModelForm
        """
        if self.instance is None:
            self.instance = DataPersons()
        return self.instance


    def done(self, form_list, **kwargs):

        self.instance.save() # save data

        return render(self.request, 'keypadcodes\done.html', {
            'form_data': [form.cleaned_data for form in form_list]
        })


    # def done(self, form_list, **kwargs):
    #
    #     self.instance.save() # save data
    #
    #     form_data = [form.cleaned_data for form in form_list]
    #
    #     print('#####')
    #     print('Lastname: %s' % form_data[0]['lastname'])
    #
    #     return render(self.request, 'keypadcodes\done.html', {
    #         'form_data': form_data
    #     })
        # return HttpResponseRedirect('/keypadcodes/people/')

def do_something_with_the_form_data(form_list):
    """
    Do something, such as sending mail
    """
    form_data = [form.cleaned_data for form in form_list]

    print('#####')
    print('Subject: %s' % form_data[0]['subject'])
    print('Sender: %s' % form_data[0]['sender'])
    print('Message: %s' % form_data[1]['message'])
    print('#####')


# end multipage form section


class BiologydeptjobtitleDeleteView(generic.DeleteView):
    model = DataPersonBiologydeptjobtitles
    template_name = "keypadcodes/personbiologydeptjobtitle_delete.html"

    def get_object(self):
        obj = super().get_object()
        return obj

    def get_success_url(self):
        post = self.get_object()
        return "/keypadcodes/person/" + str(post.personid.id)

# Create functions


@login_required
def createAddress(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = AddressForm(initial=initial_data)

    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'action':'Create', 'manager': request.user.groups.filter(name='DB Managers').exists()  }
    return render(request, 'keypadcodes/personaddress_create.html', context)


@login_required
def createAdvisee(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'advisorid':person,
        }
    form = AdviseeForm(initial=initial_data)

    if request.method == 'POST':
        form = AdviseeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personadvisee_create.html', context)


@login_required
def createAdvisor(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'adviseeid':person,
        }
    form = AdvisorForm(initial=initial_data)

    if request.method == 'POST':
        form = AdvisorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personadvisor_create.html', context)


@login_required
def createAffiliatedOrganization(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = AffiliatedOrganizationForm(initial=initial_data)

    if request.method == 'POST':
        form = AffiliatedOrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personaffiliatedorganization_create.html', context)


@login_required
def createApplication(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = ApplicationForm(initial=initial_data)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personapplication_create.html', context)


@login_required
def createBiologyDegreeArea(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = BiologydegreeareaForm(initial=initial_data)
    #
    if request.method == 'POST':
        form = BiologydegreeareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personbiologydegreearea_create.html', context)


@login_required
def createBiologyDeptJobTitle(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        'active':1,
        'activated':date.today(),
        }
    form = BiologydeptjobtitleForm(initial=initial_data)

    if request.method == 'POST':
        form = BiologydeptjobtitleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personbiologydeptjobtitle_create.html', context)


@login_required
def createCommitteeAssignment(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = CommitteeAssignmentForm(initial=initial_data)

    if request.method == 'POST':
        form = CommitteeAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personcommitteeassignment_create.html', context)


@login_required
def createEducation(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = EducationForm(initial=initial_data)

    if request.method == 'POST':
        form = EducationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personeducation_create.html', context)


@login_required
def createEmailAddress(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = EmailAddressForm(initial=initial_data)

    if request.method == 'POST':
        form = EmailAddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personemailaddress_create.html', context)


@login_required
def createKeypadcode(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = KeypadCodeForm(initial=initial_data)

    if request.method == 'POST':
        form = KeypadCodeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personkeypadcode_create.html', context)


@login_required
def createLab(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = LabForm(initial=initial_data)

    if request.method == 'POST':
        form = LabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personlab_create.html', context)


@login_required
def createListserv(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = ListservForm(initial=initial_data)

    if request.method == 'POST':
        form = ListservForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personlistserv_create.html', context)


@login_required
def createOfficeHours(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = OfficehoursForm(initial=initial_data)

    if request.method == 'POST':
        form = OfficehoursForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personofficehours_create.html', context)


@login_required
def createPhone(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = PhoneForm(initial=initial_data)

    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personphone_create.html', context)


@login_required
def createPublication(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = PublicationForm(initial=initial_data)

    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personpublication_create.html', context)


@login_required
def createResearchinfo(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = ResearchinfoForm(initial=initial_data)

    if request.method == 'POST':
        form = ResearchinfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personresearchinfo_create.html', context)


@login_required
def createRoom(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = RoomForm(initial=initial_data)

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personroom_create.html', context)


@login_required
def createUAlbanyIDCardGroup(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = UAlbanyIDCardGroupForm(initial=initial_data)

    if request.method == 'POST':
        form = UAlbanyIDCardGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personualbanyidcardgroup_create.html', context)


@login_required
def createWebsite(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    initial_data = {
        'personid':person,
        }
    form = WebsiteForm(initial=initial_data)

    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))

    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personwebsite_create.html', context)


# Update functions


@login_required
def updateAddress(request, address_id):
    address = DataPersonAddresses.objects.get(id=address_id)
    person = address.personid
    form = AddressForm(instance=address)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'action':'Edit' }
    return render(request, 'keypadcodes/personaddress_create.html', context)


@login_required
def updateAdvisee(request, advisee_id):
    advisee = DataPersonAcademicadvisor.objects.get(id=advisee_id)
    form = AdviseeForm(instance=advisee)
    if request.method == 'POST':
        form = AdviseeForm(request.POST, instance=advisee)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(advisee.advisorid.id))
    context = {'form':form, 'lastname':advisee.advisorid.lastname, 'firstname':advisee.advisorid.firstname }
    return render(request, 'keypadcodes/personadvisee_create.html', context)


@login_required
def updateAdvisor(request, advisor_id):
    advisor = DataPersonAcademicadvisor.objects.get(id=advisor_id)
    form = AdvisorForm(instance=advisor)
    if request.method == 'POST':
        form = AdvisorForm(request.POST, instance=advisor)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(advisor.adviseeid.id))
    context = {'form':form, 'lastname':advisor.adviseeid.lastname, 'firstname':advisor.adviseeid.firstname }
    return render(request, 'keypadcodes/personadvisor_create.html', context)


@login_required
def updateAffiliatedOrganization(request, affiliatedorganization_id):
    affiliatedorganization = DataPersonAffiliatedorganizations.objects.get(id=affiliatedorganization_id)
    person = affiliatedorganization.personid
    form = AffiliatedOrganizationForm(instance=affiliatedorganization)
    if request.method == 'POST':
        form = AffiliatedOrganizationForm(request.POST, instance=affiliatedorganization)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personaffiliatedorganization_create.html', context)


@login_required
def updateApplication(request, application_id):
    application = DataPersonApplications.objects.get(id=application_id)
    person = application.personid
    form = ApplicationForm(instance=application)
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personapplication_create.html', context)


@login_required
def updateBiologyDegreeArea(request, biologydegreearea_id):
    biologydegreearea = DataPersonBiologydegreeareas.objects.get(id=biologydegreearea_id)
    person = biologydegreearea.personid
    form = BiologydegreeareaForm(instance=biologydegreearea)
    if request.method == 'POST':
        form = BiologydegreeareaForm(request.POST, instance=biologydegreearea)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personbiologydegreearea_create.html', context)


@login_required
def updateBiologyDeptJobTitle(request, biologydeptjobtitle_id):
    biologydeptjobtitle = DataPersonBiologydeptjobtitles.objects.get(id=biologydeptjobtitle_id)
    person = biologydeptjobtitle.personid
    form = BiologydeptjobtitleForm(instance=biologydeptjobtitle)
    if request.method == 'POST':
        form = BiologydeptjobtitleForm(request.POST, instance=biologydeptjobtitle)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personbiologydeptjobtitle_create.html', context)


@login_required
def updateCommitteeAssignment(request, committeeassignment_id):
    committeeassignment = DataPersonCommitteeassignments.objects.get(id=committeeassignment_id)
    person = committeeassignment.personid
    form = CommitteeassignmentForm(instance=committeeassignment)
    if request.method == 'POST':
        form = CommitteeassignmentForm(request.POST, instance=committeeassignment)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personcommitteeassignment_create.html', context)


@login_required
def updateEducation(request, education_id):
    education = DataPersonEducation.objects.get(id=education_id)
    person = education.personid
    form = EducationForm(instance=education)
    if request.method == 'POST':
        form = EducationForm(request.POST, instance=education)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personeducation_create.html', context)


@login_required
def updateEmailaddress(request, emailaddress_id):
    emailaddress = DataPersonEmailaddresses.objects.get(id=emailaddress_id)
    person = emailaddress.personid
    form = EmailaddressForm(instance=emailaddress)
    if request.method == 'POST':
        form = EmailaddressForm(request.POST, instance=emailaddress)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personemailaddress_create.html', context)


@login_required
def updateKeypadcode(request, keypadcode_id):
    keypadcode = DataPersonKeypadcodes.objects.get(id=keypadcode_id)
    person = keypadcode.personid
    form = KeypadcodeForm(instance=keypadcode)
    if request.method == 'POST':
        form = KeypadcodeForm(request.POST, instance=keypadcode)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personkeypadcode_create.html', context)


@login_required
def updateLab(request, lab_id):
    lab = DataPersonLabs.objects.get(id=lab_id)
    person = lab.personid
    form = LabForm(instance=lab)
    if request.method == 'POST':
        form = LabForm(request.POST, instance=lab)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personlab_create.html', context)


@login_required
def updateListserv(request, listserv_id):
    listserv = DataPersonListservs.objects.get(id=listserv_id)
    person = listserv.personid
    form = ListservForm(instance=listserv)
    if request.method == 'POST':
        form = ListservForm(request.POST, instance=listserv)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personlistserv_create.html', context)


@login_required
def updateOfficeHours(request, officehours_id):
    officehours = DataPersonOfficehours.objects.get(id=officehours_id)
    person = officehours.personid
    form = OfficehoursForm(instance=officehours)
    if request.method == 'POST':
        form = OfficehoursForm(request.POST, instance=officehours)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personofficehours_create.html', context)


@login_required
def updatePerson(request, person_id):
    person = DataPersons.objects.get(id=person_id)
    form = PersonForm(instance=person)
    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'action':'Update' }
    return render(request, 'keypadcodes/person_create.html', context)


@login_required
def updatePhone(request, phone_id):
    phone = DataPersonPhones.objects.get(id=phone_id)
    person = phone.personid
    form = PhoneForm(instance=phone)
    if request.method == 'POST':
        form = PhoneForm(request.POST, instance=phone)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personphone_create.html', context)


@login_required
def updatePublication(request, publication_id):
    publication = DataPersonPublications.objects.get(id=publication_id)
    person = publication.personid
    form = PublicationForm(instance=publication)
    if request.method == 'POST':
        form = PublicationForm(request.POST, instance=publication)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personpublication_create.html', context)


@login_required
def updateResearchinfo(request, researchinfo_id):
    researchinfo = DataPersonResearchinfo.objects.get(id=researchinfo_id)
    person = researchinfo.personid
    form = ResearchinfoForm(instance=researchinfo)
    if request.method == 'POST':
        form = ResearchinfoForm(request.POST, instance=researchinfo)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personresearchinfo_create.html', context)


@login_required
def updateRoom(request, room_id):
    roominfo = DataPersonRooms.objects.get(id=room_id)
    person = roominfo.personid
    form = RoomForm(instance=roominfo)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=roominfo)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personroom_create.html', context)


@login_required
def updateUAlbanyIDCardGroup(request, ualbanyidcardgroup_id):
    ualbanyidcardgroupinfo = DataPersonUalbanyidcardgroup.objects.get(id=ualbanyidcardgroup_id)
    person = ualbanyidcardgroupinfo.personid
    form = UAlbanyIDCardGroupForm(instance=ualbanyidcardgroupinfo)
    if request.method == 'POST':
        form = UAlbanyIDCardGroupForm(request.POST, instance=ualbanyidcardgroupinfo)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personualbanyidcardgroup_create.html', context)


@login_required
def updateWebsite(request, website_id):
    websiteinfo = DataPersonWebsites.objects.get(id=website_id)
    person = websiteinfo.personid
    form = WebsiteForm(instance=websiteinfo)
    if request.method == 'POST':
        form = WebsiteForm(request.POST, instance=websiteinfo)
        if form.is_valid():
            form.save()
            return redirect('/keypadcodes/person/' + str(person.id))
    context = {'form':form, 'lastname':person.lastname, 'firstname':person.firstname, 'manager': request.user.groups.filter(name='DB Managers').exists() }
    return render(request, 'keypadcodes/personwebsite_create.html', context)


# Delete functions


@login_required
def deleteAddress(request, address_id):
    address = DataPersonAddresses.objects.get(id=address_id)
    person = address.personid
    if request.method == "POST":
        address.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'address':address}
    return render(request, 'keypadcodes/personaddress_delete.html', context)


@login_required
def deleteAdvisee(request, advisee_id):
    advisee = DataPersonAcademicadvisor.objects.get(id=advisee_id)
    if request.method == "POST":
        advisee.delete()
        return redirect('/keypadcodes/person/' + str(advisee.advisorid.id))
    context = {'advisee':advisee}
    return render(request, 'keypadcodes/personadvisee_delete.html', context)


@login_required
def deleteAdvisor(request, advisor_id):
    advisor = DataPersonAcademicadvisor.objects.get(id=advisor_id)
    if request.method == "POST":
        advisor.delete()
        return redirect('/keypadcodes/person/' + str(advisor.adviseeid.id))
    context = {'advisor':advisor}
    return render(request, 'keypadcodes/personadvisor_delete.html', context)


@login_required
def deleteAffiliatedOrganization(request, affiliatedorganization_id):
    affiliatedorganization = DataPersonAffiliatedorganizations.objects.get(id=affiliatedorganization_id)
    person = affiliatedorganization.personid
    if request.method == "POST":
        affiliatedorganization.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'affiliatedorganization':affiliatedorganization}
    return render(request, 'keypadcodes/personaffiliatedorganization_delete.html', context)


@login_required
def deleteApplication(request, application_id):
    application = DataPersonApplications.objects.get(id=application_id)
    person = application.personid
    if request.method == "POST":
        application.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'application':application}
    return render(request, 'keypadcodes/personapplication_delete.html', context)


@login_required
def deleteBiologyDegreeArea(request, biologydegreearea_id):
    biologydegreearea = DataPersonBiologydegreeareas.objects.get(id=biologydegreearea_id)
    person = biologydegreearea.personid
    if request.method == "POST":
        biologydegreearea.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'biologydegreearea':biologydegreearea}
    return render(request, 'keypadcodes/personbiologydegreearea_delete.html', context)


@login_required
def deleteBiologyDeptJobTitle(request, biologydeptjobtitle_id):
    biologydeptjobtitle = DataPersonBiologydeptjobtitles.objects.get(id=biologydeptjobtitle_id)
    person = biologydeptjobtitle.personid
    if request.method == "POST":
        biologydeptjobtitle.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'biologydeptjobtitle':biologydeptjobtitle}
    return render(request, 'keypadcodes/personbiologydeptjobtitle_delete.html', context)


@login_required
def deleteCommitteeAssignment(request, committeeassignment_id):
    committeeassignment = DataPersonCommitteeassignments.objects.get(id=committeeassignment_id)
    person = committeeassignment.personid
    if request.method == "POST":
        committeeassignment.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'committeeassignment':committeeassignment}
    return render(request, 'keypadcodes/personcommitteeassignment_delete.html', context)


@login_required
def deleteEducation(request, education_id):
    education = DataPersonEducation.objects.get(id=education_id)
    person = education.personid
    if request.method == "POST":
        education.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'education':education}
    return render(request, 'keypadcodes/personeducation_delete.html', context)


@login_required
def deleteEmailaddress(request, emailaddress_id):
    emailaddress = DataPersonEmailaddresses.objects.get(id=emailaddress_id)
    person = emailaddress.personid
    if request.method == "POST":
        emailaddress.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'emailaddress':emailaddress}
    return render(request, 'keypadcodes/personemailaddress_delete.html', context)


@login_required
def deleteKeypadcode(request, keypadcode_id):
    keypadcode = DataPersonKeypadcodes.objects.get(id=keypadcode_id)
    person = keypadcode.personid
    if request.method == "POST":
        keypadcode.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'keypadcode':keypadcode}
    return render(request, 'keypadcodes/personkeypadcode_delete.html', context)


@login_required
def deleteLab(request, lab_id):
    lab = DataPersonLabs.objects.get(id=lab_id)
    person = lab.personid
    if request.method == "POST":
        lab.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'lab':lab}
    return render(request, 'keypadcodes/personlab_delete.html', context)


@login_required
def deleteListserv(request, listserv_id):
    listserv = DataPersonListservs.objects.get(id=listserv_id)
    person = listserv.personid
    if request.method == "POST":
        listserv.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'listserv':listserv}
    return render(request, 'keypadcodes/personlistserv_delete.html', context)


@login_required
def deleteOfficeHours(request, officehours_id):
    officehours = DataPersonOfficehours.objects.get(id=officehours_id)
    person = officehours.personid
    if request.method == "POST":
        officehours.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'officehours':officehours}
    return render(request, 'keypadcodes/personofficehours_delete.html', context)


@login_required
def deletePhone(request, phone_id):
    phone = DataPersonPhones.objects.get(id=phone_id)
    person = phone.personid
    if request.method == "POST":
        phone.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'phone':phone}
    return render(request, 'keypadcodes/personphone_delete.html', context)


@login_required
def deletePublication(request, publication_id):
    publication = DataPersonPublications.objects.get(id=publication_id)
    person = publication.personid
    if request.method == "POST":
        publication.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'publication':publication}
    return render(request, 'keypadcodes/personpublication_delete.html', context)


@login_required
def deleteResearchinfo(request, researchinfo_id):
    researchinfo = DataPersonResearchinfo.objects.get(id=researchinfo_id)
    person = researchinfo.personid
    if request.method == "POST":
        researchinfo.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'researchinfo':researchinfo}
    return render(request, 'keypadcodes/personresearchinfo_delete.html', context)


@login_required
def deleteRoom(request, room_id):
    room = DataPersonRooms.objects.get(id=room_id)
    person = room.personid
    if request.method == "POST":
        room.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'room':room}
    return render(request, 'keypadcodes/personroom_delete.html', context)


@login_required
def deleteUAlbanyIDCardGroup(request, ualbanyidcardgroup_id):
    ualbanyidcardgroup = DataPersonUalbanyidcardgroup.objects.get(id=ualbanyidcardgroup_id)
    person = ualbanyidcardgroup.personid
    if request.method == "POST":
        ualbanyidcardgroup.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'ualbanyidcardgroup':ualbanyidcardgroup}
    return render(request, 'keypadcodes/personualbanyidcardgroup_delete.html', context)


@login_required
def deleteWebsite(request, website_id):
    website = DataPersonWebsites.objects.get(id=website_id)
    person = website.personid
    if request.method == "POST":
        website.delete()
        return redirect('/keypadcodes/person/' + str(person.id))
    context = {'website':website}
    return render(request, 'keypadcodes/personwebsite_delete.html', context)


# General Display Pages

@login_required
def IndexView(request):
    template_name = "keypadcodes/index.html"
    context = {'manager': request.user.groups.filter(name='DB Managers').exists(),}
    return render(request, template_name, context)


@login_required
def PeopleView(request):
    person_list = DataPersons.objects.all().order_by('lastname')
    person_filter = PersonFilter(request.GET, queryset=person_list)
    context = {'manager': request.user.groups.filter(name='DB Managers').exists(), 'filter': person_filter }
    return render(request, 'keypadcodes/people.html', context)


@login_required
def person(request, person_id):
    person = get_object_or_404(DataPersons, pk=person_id)
    advisees = DataPersonAcademicadvisor.objects.filter(advisorid=person.id)
    advisors = DataPersonAcademicadvisor.objects.filter(adviseeid=person.id)
    context = {'person' : person, 'advisees' : advisees, 'advisors' : advisors, 'lastname':person.lastname, 'firstname':person.firstname,
     'manager': request.user.groups.filter(name='DB Managers').exists()}
    return render(request, 'keypadcodes/person.html', context)

def reportView(request):

    # Create a file-like buffer to receive PDF data
    buf = io.BytesIO()
    #
    # Create the PDF simpledoctemplate object using the buffer as its "file"
    doc = SimpleDocTemplate(
    buf,
    rightMargin=inch/2,
    leftMargin=inch/2,
    topMargin=inch/2,
    bottomMargin=inch/2,
    pagesize=letter,
    )

    # p = canvas.Canvas(buf)
    # p.drawString(100, 100, "Hello world.")
    # p.showPage()
    # p.save()
    #
    # buf.seek(0)

    flowables = []
    style = getSampleStyleSheet()
    yourStyle = ParagraphStyle('yourtitle',
                           fontName="Helvetica-Bold",
                           fontSize=16,
                           parent=style['Heading2'],
                           alignment=1,
                        spaceAfter=14)
    # P0 = Paragraph('''<b>A pa<font color=red>r</font>a<i>graph</i></b><super><font color=yellow>1</font></super>''', yourStyle)
    # flowables.append(P0)

    psDetalle = ParagraphStyle('Resumen', fontSize=9, leading=14, justifyBreaks=1, alignment=TA_CENTER,
                               justifyLastLine=1)
    text = "BIOLOGY DEPARTMENT DIRECTORY"
    paragraphReportSummary = Paragraph(text, psDetalle)
    spacer = Spacer(30, 20)

    flowables.append(paragraphReportSummary)

    flowables.append(spacer)

    flowables.append(generatePDFdirectory())

    doc.build(flowables)

    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='hello.pdf')


def dataEntry(request):
    form = NewPersonForm()
    context = {'form':form, 'manager': request.user.groups.filter(name='DB Managers').exists()}
    return render(request, 'keypadcodes/dataentry.html', context)

def reports(request):
    context = {'manager': request.user.groups.filter(name='DB Managers').exists()}
    return render(request, 'keypadcodes/reports.html', context)

# Report generation
def generatePDFdirectory():

    directoryentries = [
    ["Office", "Office Phone", "Name", "Lab Affiliation", "Lab Phone", "Email Address"]]

    # Temp - Get all users for simple directory
    person_list = DataPersons.objects.all().order_by('lastname')

    for person in person_list:

        # Put together simple directory
        person_office = ""
        person_officephone = ""
        person_name = ""
        person_labaffiliation = ""
        person_labphone = ""
        person_emailaddress = ""

        person_name = "{0}, {1}".format(person.lastname, person.firstname)
        for phone in DataPersonPhones.objects.filter(personid = person.id):
            if phone.phonetypecode.phoneclassname == 'Office':
                person_officephone = phone.phonenumber
            if phone.phonetypecode.phoneclassname == 'Lab':
                person_labphone = phone.phonenumber
        for emailaddress in DataPersonEmailaddresses.objects.filter(personid = person.id):
            if emailaddress.emailaddressclassid.emailclassname == 'University':
                person_emailaddress = emailaddress.emailaddress
        for labaffil in DataPersonLabs.objects.filter(personid = person.id):
            person_labaffiliation = labaffil.labid
        for room in DataPersonRooms.objects.filter(personid = person.id):
            print("Room = '{0}'".format(room.roomusetype))
            if room.roomusetype.roomtype == 'Office':
                person_office = room

        directoryentries.append([person_office, person_officephone, person_name, person_labaffiliation, person_labphone, person_emailaddress,])


    # ["LS 20331","7-4448","Agris, Paul","LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ["LS 20331", "7-4448", "Agris, Paul", "LS 1074", "1-8809", "pagris@albany.edu"],
    # ]


    # buffer = SimpleDocTemplate(pdffilename)
    # doc.pagesize = portrait(letter)

    table = Table(directoryentries)

    style = TableStyle([
        ('BACKGROUND', (0, 0), (5, 0), colors.mediumpurple),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        # ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
        # ('FONTSIZE', (0,0), (-1,0), 12),
        # ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ])

    table.setStyle(style)

    rowNumb = len(directoryentries)
    for i in range(1, rowNumb):
        if i % 2 == 0:
            bc = colors.white
        else:
            bc = colors.whitesmoke

        ts = TableStyle(
            [('BACKGROUND', (0, i), (-1, i), bc)]
        )
        table.setStyle(ts)

    elems = []

    # psDetalle = ParagraphStyle('Resumen', fontSize=9, leading=14, justifyBreaks=1, alignment=TA_CENTER,
    #                            justifyLastLine=1)
    # text = "BIOLOGY DEPARTMENT DIRECTORY"
    # paragraphReportSummary = Paragraph(text, psDetalle)
    # spacer = Spacer(30, 20)
    # elems.append(paragraphReportSummary)
    #
    # elems.append(spacer)
    #
    # elems.append(table)

    # doc.build(elems)

    # return doc

    return table



# Obsolete pages

class PersonCreateView(generic.CreateView):
    template_name = 'keypadcodes/person_create.html'
    form_class = PersonForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class PersonUpdateView(generic.UpdateView):
    template_name = 'keypadcodes/person_create.html'
    form_class = PersonForm

    def get_object(self):
        id_ = self.kwargs.get("pk")
        return get_object_or_404(DataPersons, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
