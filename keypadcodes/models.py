
import datetime

from django.utils import timezone
from django.db import models
from django.urls import reverse


class CodeAddresstypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    addresstype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_addresstypes'

    def __str__(self):
        return self.addresstype


class CodeApplicationEvaluation(models.Model):
    id = models.BigAutoField(primary_key=True)
    evaluation = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_application_evaluation'

    def __str__(self):
        return self.evaluation


class CodeApplicationRejectionreason(models.Model):
    id = models.BigAutoField(primary_key=True)
    rejectionreason = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'code_application_rejectionreason'

    def __str__(self):
        return self.rejectionreason


class CodeApplicationResponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    applicationresponse = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_application_response'

    def __str__(self):
        return self.applicationresponse

class CodeBiologyDegreearea(models.Model):
    id = models.BigAutoField(primary_key=True)
    degreearea = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'code_biology_degreearea'

    def __str__(self):
        return self.degreearea


class CodeBiologyDegreetype(models.Model):
    id = models.BigAutoField(primary_key=True)
    degreetype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_biology_degreetype'

    def __str__(self):
        return self.degreetype


class CodeBiologyPersontypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    persontype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_biology_persontypes'

    def __str__(self):
        return self.persontype


class CodeCities(models.Model):
    id = models.BigAutoField(primary_key=True)
    cityname = models.CharField(max_length=100)
    stateid = models.ForeignKey('CodeStates', models.DO_NOTHING, db_column='stateid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code_cities'


class CodeCommittees(models.Model):
    id = models.BigAutoField(primary_key=True)
    committeetypeid = models.ForeignKey('CodeCommitteetypes', models.DO_NOTHING, db_column='committeetypeid', blank=True, null=True)
    committeename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code_committees'

    def __str__(self):
        return self.committeename


class CodeCommitteetypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    committeetype = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code_committeetypes'


class CodeConfidentialitylevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    confidentialitylevel = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_confidentialitylevel'

    def __str__(self):
        return self.confidentialitylevel


class CodeCorrespondencetype(models.Model):
    id = models.BigAutoField(primary_key=True)
    correspondencetype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_correspondencetype'


class CodeCountries(models.Model):
    id = models.BigAutoField(primary_key=True)
    countryname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_countries'

    def __str__(self):
        return self.countryname


class CodeEmailaddresstypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    emailclassname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_emailaddresstypes'

    def __str__(self):
        return self.emailclassname


class CodeEthnicity(models.Model):
    id = models.BigAutoField(primary_key=True)
    ethnicity = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_ethnicity'

    def __str__(self):
        return self.ethnicity


class CodeGender(models.Model):
    id = models.BigAutoField(primary_key=True)
    gender = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_gender'

    def __str__(self):
        return self.gender


class CodeJobtitles(models.Model):
    id = models.BigAutoField(primary_key=True)
    jobtypeid = models.ForeignKey('CodeJobtypes', models.DO_NOTHING, db_column='jobtypeid')
    jobtitle = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_jobtitles'

    def __str__(self):
        return self.jobtitle


class CodeJobtypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    jobtype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_jobtypes'


class CodeKeypadcodetypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    keypadcodetype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_keypadcodetypes'


class CodePersonaltitles(models.Model):
    id = models.BigAutoField(primary_key=True)
    personaltitle = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'code_personaltitles'

    def __str__(self):
        return self.personaltitle


class CodePhonetypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    phoneclassname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_phonetypes'

    def __str__(self):
        return self.phoneclassname


class CodeRoomtypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    roomtype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_roomtypes'

    def __str__(self):
        return self.roomtype


class CodeSemesters(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.CharField(max_length=4)
    semester = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'code_semesters'

    def __str__(self):
        return self.semester + " " + self.year


class CodeStates(models.Model):
    id = models.BigAutoField(primary_key=True)
    stateabbreviation = models.CharField(max_length=4)
    statename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_states'

    def __str__(self):
        return self.statename


class CodeSupervisiontypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    supervisiontype = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_supervisiontypes'


class CodeUniversitybuildings(models.Model):
    id = models.BigAutoField(primary_key=True)
    buildingabbreviation = models.CharField(max_length=5)
    buildingname = models.CharField(max_length=100)
    address0 = models.CharField(max_length=50, blank=True, null=True)
    address1 = models.CharField(max_length=50, blank=True, null=True)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    address3 = models.CharField(max_length=50, blank=True, null=True)
    address4 = models.CharField(max_length=50, blank=True, null=True)
    cityid = models.BigIntegerField(blank=True, null=True)
    stateid = models.ForeignKey(CodeStates, models.DO_NOTHING, db_column='stateid', blank=True, null=True)
    countryid = models.ForeignKey(CodeCountries, models.DO_NOTHING, db_column='countryid', blank=True, null=True)
    zip = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code_universitybuildings'

    def __str__(self):
        return self.buildingname


class CodeUniversitydepartments(models.Model):
    id = models.BigAutoField(primary_key=True)
    departmentname = models.CharField(max_length=100, verbose_name="Department Name")

    class Meta:
        managed = False
        db_table = 'code_universitydepartments'


class CodeWebsitetypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    websitetypename = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'code_websitetypes'

    def __str__(self):
        return self.websitetypename


class DataAdvisorAdvisees(models.Model):
    id = models.BigAutoField(primary_key=True)
    advisorid = models.BigIntegerField(verbose_name="Advisor")
    adviseeid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='adviseeid', verbose_name="Advisee")

    class Meta:
        managed = False
        db_table = 'data_advisor_advisees'


class DataApplicationCorrespondence(models.Model):
    id = models.BigAutoField(primary_key=True)
    applicationid = models.ForeignKey('DataPersonApplications', models.DO_NOTHING, db_column='applicationid')
    correspondencetypeid = models.ForeignKey(CodeCorrespondencetype, models.DO_NOTHING, db_column='correspondencetypeid')
    correspondencedate = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'data_application_correspondence'


class DataApplicationRejectionreasons(models.Model):
    id = models.BigAutoField(primary_key=True)
    applicationid = models.ForeignKey('DataPersonApplications', models.DO_NOTHING, db_column='applicationid')
    rejectionreasonid = models.ForeignKey(CodeApplicationRejectionreason, models.DO_NOTHING, db_column='rejectionreasonid')

    class Meta:
        managed = False
        db_table = 'data_application_rejectionreasons'


class DataDepartmentcommitteeHeads(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    committeeid = models.ForeignKey('DataDepartmentcommittees', models.DO_NOTHING, db_column='committeeid')

    class Meta:
        managed = False
        db_table = 'data_departmentcommittee_heads'


class DataDepartmentcommitteeMembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    committeeid = models.ForeignKey('DataDepartmentcommittees', models.DO_NOTHING, db_column='committeeid')

    class Meta:
        managed = False
        db_table = 'data_departmentcommittee_members'


class DataDepartmentcommittees(models.Model):
    id = models.BigAutoField(primary_key=True)
    committeename = models.CharField(max_length=50)
    committeecategory = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_departmentcommittees'


class DataDepartmentpositionHolders(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.BigIntegerField()
    committeeid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'data_departmentposition_holders'


class DataDepartmentpositions(models.Model):
    id = models.BigAutoField(primary_key=True)
    positionname = models.CharField(max_length=50)
    positioncategory = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_departmentpositions'


class DataEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    blurb = models.CharField(max_length=50)
    title = models.TextField(blank=True, null=True)
    eventstart = models.DateTimeField()
    eventend = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    titleurl = models.TextField(blank=True, null=True)
    locationurl = models.TextField(blank=True, null=True)
    linkedpdfwebsitepath = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_events'


class DataJobtypecategoryKeypadcodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    jobtypecategoryid = models.BigIntegerField()
    keypadcodeid = models.ForeignKey('DataKeypadcodes', models.DO_NOTHING, db_column='keypadcodeid')

    class Meta:
        managed = False
        db_table = 'data_jobtypecategory_keypadcodes'


class DataKeypadcodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    roomid = models.ForeignKey('DataRooms', models.DO_NOTHING, db_column='roomid')
    keypadcodetypeid = models.ForeignKey(CodeKeypadcodetypes, models.DO_NOTHING, db_column='keypadcodetypeid')
    keypadusercode = models.CharField(max_length=2)
    keypadcodevalue = models.CharField(max_length=7)
    dateprogrammed = models.DateTimeField()
    notes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_keypadcodes'

    def __str__(self):
        return self.roomid.buildingid.buildingname + " " + self.roomid.roomnumber


class DataLabRooms(models.Model):
    id = models.BigAutoField(primary_key=True)
    labid = models.ForeignKey('DataLabs', models.DO_NOTHING, db_column='labid')
    roomid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'data_lab_rooms'


class DataLabs(models.Model):
    id = models.BigAutoField(primary_key=True)
    namedlab = models.BooleanField(verbose_name="Named Lab")
    labname = models.CharField(max_length=50, verbose_name="Lab Name")

    class Meta:
        managed = False
        db_table = 'data_labs'

    def __str__(self):
        return self.labname


class DataListservs(models.Model):
    id = models.BigAutoField(primary_key=True)
    listservname = models.CharField(max_length=50, )
    lastupdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_listservs'

    def __str__(self):
        return self.listservname


class DataPersonAcademicadvisor(models.Model):
    id = models.BigAutoField(primary_key=True)
    advisorid = models.ForeignKey('DataPersons', models.DO_NOTHING, related_name='advisor', db_column='advisorid', verbose_name='Advisor')
    adviseeid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='adviseeid', verbose_name='Advisee')
    startdate = models.DateTimeField(blank=True, null=True, verbose_name='Start Date')
    enddate = models.DateTimeField(blank=True, null=True, verbose_name='End Date')

    class Meta:
        managed = False
        db_table = 'data_person_academicadvisor'


class DataPersonActive(models.Model):
    personid = models.OneToOneField('DataPersons', models.DO_NOTHING, db_column='personid', primary_key=True)
    activeinbiologydept = models.BooleanField(blank=True, null=True, verbose_name='Active in Biology Department')
    activatedinbiologydept = models.DateTimeField(blank=True, null=True, verbose_name='Date Activated in Biology Department')
    deactivatedinbiologydept = models.DateTimeField(blank=True, null=True, verbose_name='Date Deactivated in Biology Department')
    activeinuniversity = models.BooleanField(blank=True, null=True, verbose_name="Active at University")
    activatedinuniversity = models.DateTimeField(blank=True, null=True, verbose_name='Date Activated at University')
    deactivatedinuniversity = models.DateTimeField(blank=True, null=True, verbose_name='Date Deactivated at University')

    class Meta:
        managed = False
        db_table = 'data_person_active'


class DataPersonAddresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    addresstypeid = models.ForeignKey(CodeAddresstypes, models.DO_NOTHING, db_column='addresstypeid', verbose_name="Address Type")
    address0 = models.CharField(max_length=100, verbose_name="Address")
    address1 = models.CharField(max_length=100, verbose_name="Addt'l Address (1)", blank=True, null=True)
    address2 = models.CharField(max_length=100, verbose_name="Addt'l Address (2)", blank=True, null=True)
    address3 = models.CharField(max_length=100, verbose_name="Addt'l Address (3)", blank=True, null=True)
    address4 = models.CharField(max_length=100, verbose_name="Addt'l Address (4)", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="City", blank=True, null=True)
    stateid = models.ForeignKey(CodeStates, models.DO_NOTHING, db_column='stateid', verbose_name="State", blank=True, null=True)
    countryid = models.ForeignKey(CodeCountries, models.DO_NOTHING, db_column='countryid', verbose_name="Country", blank=True, null=True)
    zip = models.CharField(max_length=50, verbose_name="Zip Code", blank=True, null=True)
    confidentialitylevelid = models.ForeignKey(CodeConfidentialitylevel, models.DO_NOTHING, db_column='confidentialitylevelid', verbose_name="Confidentiality Level")

    class Meta:
        managed = False
        db_table = 'data_person_addresses'


class DataPersonAffiliatedorganizations(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    affiliatedorganizationdepartment = models.TextField(verbose_name="Affliated Organization or Department")
    address0 = models.CharField(max_length=150, verbose_name="Address")
    address1 = models.CharField(max_length=150, verbose_name="Addt'l Address (1)", blank=True, null=True)
    address2 = models.CharField(max_length=150, verbose_name="Addt'l Address (2)", blank=True, null=True)
    address3 = models.CharField(max_length=150, verbose_name="Addt'l Address (3)", blank=True, null=True)
    address4 = models.CharField(max_length=150, verbose_name="Addt'l Address (4)", blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True, verbose_name='City')
    stateid = models.ForeignKey(CodeStates, models.DO_NOTHING, db_column='stateid', blank=True, null=True, verbose_name='State')
    countryid = models.ForeignKey(CodeCountries, models.DO_NOTHING, db_column='countryid', blank=True, null=True, verbose_name='Country')

    class Meta:
        managed = False
        db_table = 'data_person_affiliatedorganizations'


class DataPersonApplications(models.Model):
    id = models.BigAutoField(primary_key=True)
    semesterid = models.ForeignKey(CodeSemesters, models.DO_NOTHING, db_column='semesterid', verbose_name="Year/Semester")
    degreetypeid = models.ForeignKey(CodeBiologyDegreetype, models.DO_NOTHING, db_column='degreetypeid', verbose_name="Degree Type")
    degreeareaid = models.ForeignKey(CodeBiologyDegreearea, models.DO_NOTHING, db_column='degreeareaid', verbose_name="Degree Area")
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    applicationreceipt = models.DateTimeField(blank=True, null=True, verbose_name='Date Application Received')
    applicationacknowledged = models.DateField(blank=True, null=True, verbose_name='Date Application Acknowledged')
    quantraw = models.IntegerField(blank=True, null=True, verbose_name='Quant Raw Score')
    quantpercentile = models.IntegerField(blank=True, null=True, verbose_name='Quant Percentile')
    verbalraw = models.IntegerField(blank=True, null=True, verbose_name='Verbal Raw')
    verbalpercentile = models.IntegerField(blank=True, null=True, verbose_name='Verbal Percentile')
    writtenraw = models.IntegerField(blank=True, null=True, verbose_name='Written Raw')
    writtenpercentile = models.IntegerField(blank=True, null=True, verbose_name='Written Percentile')
    gpa = models.FloatField(blank=True, null=True, verbose_name='GPA')
    toefl = models.IntegerField(blank=True, null=True, verbose_name='TOEFL')
    ielts = models.IntegerField(blank=True, null=True, verbose_name='IELTS')
    committeeevaluationid = models.ForeignKey(CodeApplicationEvaluation, models.DO_NOTHING, db_column='committeeevaluationid', blank=True, null=True, verbose_name='Committee Evaluation')
    applicantresponseid = models.ForeignKey(CodeApplicationResponse, models.DO_NOTHING, db_column='applicantresponseid', blank=True, null=True, verbose_name='Applicant Response')
    committeedecisiondate = models.DateTimeField(blank=True, null=True, verbose_name='Date of Committee Decision')
    evaluationacknowledged = models.DateTimeField(blank=True, null=True, verbose_name='Date Evaluation Acknowledged')
    notes = models.TextField(blank=True, null=True, verbose_name='Notes')

    class Meta:
        managed = False
        db_table = 'data_person_applications'


class DataPersonBiologydegreeareas(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    biologydegreeareaid = models.ForeignKey(CodeBiologyDegreearea, models.DO_NOTHING, db_column='biologydegreeareaid', verbose_name='Biology Degree Area')

    class Meta:
        managed = False
        db_table = 'data_person_biologydegreeareas'

    def __str__(self):
        return self.biologydegreeareaid


class DataPersonBiologydeptjobtitles(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    jobtitleid = models.ForeignKey(CodeJobtitles, models.DO_NOTHING, db_column='jobtitleid', verbose_name='Job Title')
    active = models.BooleanField(verbose_name='Active')
    activated = models.DateTimeField(blank=True, null=True, verbose_name='Date Activated')
    deactivated = models.DateTimeField(blank=True, null=True, verbose_name='Date Deactivated')

    class Meta:
        managed = False
        db_table = 'data_person_biologydeptjobtitles'


class DataPersonCommitteeassignments(models.Model):
    id = models.BigAutoField(primary_key=True)
    committeeassignmentid = models.ForeignKey(CodeCommittees, models.DO_NOTHING, db_column='committeeassignmentid')
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    startdate = models.DateTimeField(blank=True, null=True, verbose_name='Start Date')
    enddate = models.DateTimeField(blank=True, null=True, verbose_name='End Date')
    chair = models.BooleanField(blank=True, null=True, verbose_name='Committee Chair')

    class Meta:
        managed = False
        db_table = 'data_person_committeeassignments'


class DataPersonEducation(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    institution = models.CharField(max_length=100, blank=True, null=True, verbose_name="Institution")
    degree = models.CharField(max_length=50, blank=True, null=True, verbose_name="Degree")
    gradyear = models.CharField(max_length=4, blank=True, null=True, verbose_name="Graduation Year")
    ordinal = models.IntegerField(blank=True, null=True, verbose_name="Order")

    class Meta:
        managed = False
        db_table = 'data_person_education'


class DataPersonEmailaddresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    emailaddressclassid = models.ForeignKey(CodeEmailaddresstypes, models.DO_NOTHING, db_column='emailaddressclassid', verbose_name="Type of Email Address")
    emailaddress = models.CharField(max_length=50, verbose_name="Email Address")
    confidentialityid = models.ForeignKey(CodeConfidentialitylevel, models.DO_NOTHING, db_column='confidentialityid', verbose_name="Confidentiality Level")

    class Meta:
        managed = False
        db_table = 'data_person_emailaddresses'


class DataPersonKeypadcodes(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid', blank=True, null=True)
    keypadcodeid = models.ForeignKey(DataKeypadcodes, models.DO_NOTHING, db_column='keypadcodeid', verbose_name='Keypad Code')

    class Meta:
        managed = False
        db_table = 'data_person_keypadcodes'


class DataPersonLabs(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    labid = models.ForeignKey(DataLabs, models.DO_NOTHING, db_column='labid',verbose_name='Lab')

    class Meta:
        managed = False
        db_table = 'data_person_labs'


class DataPersonListservs(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    listservid = models.ForeignKey(DataListservs, models.DO_NOTHING, db_column='listservid', verbose_name='Listserv Name')

    class Meta:
        managed = False
        db_table = 'data_person_listservs'


class DataPersonOfficehours(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    semesterid = models.ForeignKey(CodeSemesters, models.DO_NOTHING, db_column='semesterid', verbose_name='Semester/Year')
    officehourstext = models.CharField(max_length=200,verbose_name="Office Hours")

    class Meta:
        managed = False
        db_table = 'data_person_officehours'


class DataPersonPhones(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    phonetypecode = models.ForeignKey(CodePhonetypes, models.DO_NOTHING, db_column='phonetypecode', verbose_name='Telephone Type')
    usphonecode = models.BooleanField(verbose_name='U.S. Telephone Number')
    phonenumber = models.CharField(max_length=50, blank=True, null=True, verbose_name='Telephone Number')
    confidentialityid = models.ForeignKey(CodeConfidentialitylevel, models.DO_NOTHING, db_column='confidentialityid', verbose_name='Confidentiality Level')

    class Meta:
        managed = False
        db_table = 'data_person_phones'


class DataPersonPublications(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    journal = models.CharField(max_length=100)
    volumeinfo = models.TextField(blank=True, null=True)
    pubdate = models.DateField()
    title = models.TextField()
    authorlist = models.TextField()
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_person_publications'


class DataPersonResearchinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    researchqualifications = models.TextField(blank=True, null=True, verbose_name="Research Qualifications")  # This field type is a guess.
    researchinterest = models.TextField(blank=True, null=True, verbose_name="Research Interest")  # This field type is a guess.
    lastupdated = models.DateTimeField(blank=True, null=True, verbose_name="Last Updated")

    class Meta:
        managed = False
        db_table = 'data_person_researchinfo'


class DataPersonResearchsupervisor(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    semesterid = models.ForeignKey(CodeSemesters, models.DO_NOTHING, db_column='semesterid')

    class Meta:
        managed = False
        db_table = 'data_person_researchsupervisor'
        unique_together = (('personid', 'semesterid'),)


class DataPersonRooms(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    roomid = models.ForeignKey('DataRooms', models.DO_NOTHING, db_column='roomid',verbose_name='Room')
    roomusetype = models.ForeignKey(CodeRoomtypes, models.DO_NOTHING, db_column='roomusetype', blank=True, null=True, verbose_name='Room Type')

    class Meta:
        managed = False
        db_table = 'data_person_rooms'

    def __str__(self):
        return ("{0}{1}".format(self.roomid.buildingid.buildingabbreviation, self.roomid.roomnumber))

class DataPersonUalbanyidcardgroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    ualbanycardgroupid = models.ForeignKey('DataUalbanyidcardgroups', models.DO_NOTHING, db_column='ualbanycardgroupid', verbose_name="UAlbany Card Group")
    effective = models.DateTimeField(blank=True, null=True, verbose_name="Date Effective")
    expires = models.DateTimeField(blank=True, null=True, verbose_name="Date Expires")
    comment = models.CharField(max_length=50, blank=True, null=True, verbose_name="Comment")
    created = models.DateTimeField(blank=True, null=True, verbose_name="Date Created")
    operator = models.CharField(max_length=50, blank=True, null=True, verbose_name="Operator")
    membertype = models.CharField(max_length=50, blank=True, null=True, verbose_name="Member Type")

    class Meta:
        managed = False
        db_table = 'data_person_ualbanyidcardgroup'

    def __str__(self):
        return (self.ualbanycardgroupid.patrongroup)


class DataPersonUniversityjobtitles(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    universityjobtitleid = models.ForeignKey(CodeJobtitles, models.DO_NOTHING, db_column='universityjobtitleid')

    class Meta:
        managed = False
        db_table = 'data_person_universityjobtitles'


class DataPersonWebsites(models.Model):
    id = models.BigAutoField(primary_key=True)
    personid = models.ForeignKey('DataPersons', models.DO_NOTHING, db_column='personid')
    websitetypecode = models.ForeignKey(CodeWebsitetypes, models.DO_NOTHING, db_column='websitetypecode', verbose_name='Website Type')
    websiteurl = models.CharField(max_length=150, blank=True, null=True, verbose_name='Website URL')
    confidentialityid = models.ForeignKey(CodeConfidentialitylevel, models.DO_NOTHING, db_column='confidentialityid', verbose_name="Confidentiality Level")

    class Meta:
        managed = False
        db_table = 'data_person_websites'


class DataPersons(models.Model):
    id = models.BigAutoField(primary_key=True)
    lastname = models.CharField(max_length=50, verbose_name="Lastname")
    firstname = models.CharField(max_length=50, verbose_name="Firstname", blank=True, null=True)
    middle = models.CharField(max_length=50, verbose_name="Middle Name/Initial", blank=True, null=True)
    ualbanyempid = models.CharField(max_length=50, verbose_name="UAlbany Employee ID", blank=True, null=True)
    ualbanynetid = models.CharField(max_length=50, verbose_name="UAlbany Net ID", blank=True, null=True)
    persontypeid = models.ForeignKey(CodeBiologyPersontypes, models.DO_NOTHING, db_column='persontypeid', verbose_name="Person Type", blank=True, null=True)
    personaltitleid = models.ForeignKey(CodePersonaltitles, models.DO_NOTHING, db_column='personaltitleid', verbose_name="Addressed As", blank=True, null=True)
    birthdate = models.DateTimeField(verbose_name="Birthdate", blank=True, null=True)
    genderid = models.ForeignKey(CodeGender, models.DO_NOTHING, db_column='genderid', verbose_name="Gender", blank=True, null=True)
    ethnicityid = models.ForeignKey(CodeEthnicity, models.DO_NOTHING, db_column='ethnicityid', verbose_name="Ethnicity", blank=True, null=True)
    countryoforiginid = models.ForeignKey(CodeCountries, models.DO_NOTHING, db_column='countryoforiginid', verbose_name="Country of Origin", blank=True, null=True)
    nysresident = models.BooleanField(verbose_name="NYS Resident", blank=True, null=True)

    # advisors = DataPersonAcademicadvisor.objects.filter(advisorid=id)
    # advisees = DataPersonAcademicadvisor.objects.filter(adviseeid=id)

    class Meta:
        managed = False
        db_table = 'data_persons'

    def __str__(self):
        return (self.lastname)

    def get_absolute_url(self):
        return f"/keypadcodes/person/{self.id}/"


class DataPrinterUsage(models.Model):
    id = models.BigAutoField(primary_key=True)
    printerid = models.BigIntegerField(blank=True, null=True)
    dateperiod = models.TextField()
    userid = models.BigIntegerField(blank=True, null=True)
    pagecount = models.IntegerField()
    printername = models.CharField(max_length=50)
    username = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'data_printer_usage'


class DataPrinters(models.Model):
    id = models.BigAutoField(primary_key=True)
    printername = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'data_printers'


class DataRooms(models.Model):
    id = models.BigAutoField(primary_key=True)
    buildingid = models.ForeignKey(CodeUniversitybuildings, models.DO_NOTHING, db_column='buildingid')
    roomnumber = models.CharField(max_length=50)
    parentroomid = models.BigIntegerField(blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_rooms'

    def __str__(self):
        return (self.buildingid.buildingname + " " + self.roomnumber)


class DataUalbanyidcardgroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    patrongroup = models.CharField(max_length=50, verbose_name='Patron Group')
    description0 = models.CharField(max_length=100, blank=True, null=True)
    description1 = models.CharField(max_length=100, blank=True, null=True)
    description2 = models.CharField(max_length=100, blank=True, null=True)
    description3 = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_ualbanyidcardgroups'

    def __str__(self):
        return (self.patrongroup)
