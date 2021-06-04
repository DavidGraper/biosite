from django import forms

# from .models import DataPersons, DataPersonAddresses
# from .models import DataPersonKeypadcodes, DataPersonBiologydegreeareas
# from .models import DataPersonBiologydeptjobtitles, DataPersonAffiliatedorganizations
# from .models import DataPersonUalbanyidcardgroup
# from .models import DataPersonPhones
from .models import *

class NewPersonForm(forms.ModelForm):
    class Meta:
        model = DataPersons
        fields = [
            'lastname',
            'firstname',
            'middle',
            'ualbanyempid',
            'ualbanynetid',
            'personaltitleid',
            'birthdate',
            'genderid',
            'ethnicityid',
            'countryoforiginid',
            'nysresident',
        ]


class PersonForm(forms.ModelForm):
    class Meta:
        model = DataPersons
        fields = [
            'lastname',
            'firstname',
            'middle',
            'ualbanyempid',
            'ualbanynetid',
            'personaltitleid',
            'birthdate',
            'genderid',
            'ethnicityid',
            'countryoforiginid',
            'nysresident',
            'persontypeid',
        ]


class AddressForm(forms.ModelForm):
    class Meta:
        model = DataPersonAddresses
        fields = '__all__'


class AdviseeForm(forms.ModelForm):
    class Meta:
        model = DataPersonAcademicadvisor
        fields = '__all__'


class AdvisorForm(forms.ModelForm):
    class Meta:
        model = DataPersonAcademicadvisor
        fields = '__all__'


class AffiliatedOrganizationForm(forms.ModelForm):
    class Meta:
        model = DataPersonAffiliatedorganizations
        fields = '__all__'


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = DataPersonApplications
        fields = '__all__'


class KeypadcodeForm(forms.ModelForm):
    class Meta:
        model = DataPersonKeypadcodes
        fields = [
            'personid',
            'keypadcodeid',
        ]


class LabForm(forms.ModelForm):
    class Meta:
        model = DataPersonLabs
        fields = '__all__'


class BiologydegreeareaForm(forms.ModelForm):
    class Meta:
        model = DataPersonBiologydegreeareas
        fields = '__all__'


class BiologydeptjobtitleForm(forms.ModelForm):
    class Meta:
        model = DataPersonBiologydeptjobtitles
        fields = '__all__'


class CommitteeassignmentForm(forms.ModelForm):
    class Meta:
        model = DataPersonCommitteeassignments
        fields = '__all__'


class EducationForm(forms.ModelForm):
    class Meta:
        model = DataPersonEducation
        fields = '__all__'


class EmailAddressForm(forms.ModelForm):
    class Meta:
        model = DataPersonEmailaddresses
        fields = '__all__'


class KeypadCodeForm(forms.ModelForm):
    class Meta:
        model = DataPersonKeypadcodes
        fields = '__all__'


class OfficehoursForm(forms.ModelForm):
    class Meta:
        model = DataPersonOfficehours
        fields = '__all__'


class PhoneForm(forms.ModelForm):
    class Meta:
        model = DataPersonPhones
        fields = '__all__'


class PublicationForm(forms.ModelForm):
    class Meta:
        model = DataPersonPublications
        fields = '__all__'


class ResearchinfoForm(forms.ModelForm):
    class Meta:
        model = DataPersonResearchinfo
        fields = '__all__'


class RoomForm(forms.ModelForm):
    class Meta:
        model = DataPersonRooms
        fields = '__all__'


class UAlbanyIDCardGroupForm(forms.ModelForm):
    class Meta:
        model = DataPersonUalbanyidcardgroup
        fields = '__all__'


class WebsiteForm(forms.ModelForm):
    class Meta:
        model = DataPersonWebsites
        fields = '__all__'


class ListservForm(forms.ModelForm):
    class Meta:
        model = DataPersonListservs
        fields = '__all__'


class UAlbanyidcardgroupForm(forms.ModelForm):
    class Meta:
        model = DataPersonUalbanyidcardgroup
        fields = [
            'id',
            'personid',
            'ualbanycardgroupid',
            'effective',
            'expires',
            'comment',
            'created',
            'operator',
            'membertype',
        ]


class TelephoneForm(forms.ModelForm):
    class Meta:
        model = DataPersonPhones
        fields = [
            'id',
            'personid',
            'phonetypecode',
            'usphonecode',
            'phonenumber',
            'confidentialityid',
        ]


class CommitteeAssignmentForm(forms.ModelForm):
    class Meta:
        model = DataPersonCommitteeassignments
        fields = '__all__'


class ContactForm1(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()

class ContactForm2(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=False)


class ContactForm3(forms.Form):
    creditcard = forms.CharField(max_length=10)
