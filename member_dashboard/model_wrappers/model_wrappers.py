from datetime import date

from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from edc_model_wrapper import ModelWrapper


class HouseholdFormsModelWrapperMixin(ModelWrapper):
    """For models with a FK to household_structure.
    """
    next_url_name = django_apps.get_app_config(
        'enumeration').dashboard_url_name
    next_url_attrs = [
        'household_identifier', 'survey_schedule', 'household_structure']

    @property
    def household_structure(self):
        return self.object.household_structure

    @property
    def household_identifier(self):
        return (self.object.household_structure.
                household.household_identifier)

    @property
    def survey_schedule(self):
        return (self.object.household_structure.
                survey_schedule_object.field_value)

    @property
    def survey_schedule_object(self):
        return (self.object.household_structure.
                survey_schedule_object)


class MemberStatusModelWrapperMixin(ModelWrapper):

    """For models with a FK to household member."""

    next_url_name = django_apps.get_app_config(
        'enumeration').dashboard_url_name
    next_url_attrs = [
        'household_identifier', 'survey_schedule', 'household_member']

    @property
    def household_member(self):
        return str(self.object.household_member.id)

    @property
    def household_identifier(self):
        return (self.object.household_member.
                household_structure.household.household_identifier)

    @property
    def survey_schedule(self):
        return (self.object.household_member.
                household_structure.survey_schedule_object.field_value)

    @property
    def survey_schedule_object(self):
        return (self.object.household_member.
                household_structure.survey_schedule_object)


class AbsentMemberModelWrapper(MemberStatusModelWrapperMixin):

    model = 'member.absentmember'
    querystring_attrs = ['survey_schedule', 'household_member']
    next_url_attrs = ['household_identifier', 'survey_schedule']


class MovedMemberModelWrapper(MemberStatusModelWrapperMixin):

    model = 'member.movedmember'
    querystring_attrs = ['survey_schedule', 'household_member']
    next_url_attrs = ['household_identifier', 'survey_schedule']


class UndecidedMemberModelWrapper(MemberStatusModelWrapperMixin):

    model = 'member.undecidedmember'
    querystring_attrs = ['survey_schedule', 'household_member']
    next_url_attrs = ['household_identifier', 'survey_schedule']


class RefusedMemberModelWrapper(MemberStatusModelWrapperMixin):

    model = 'member.refusedmember'
    querystring_attrs = ['survey_schedule', 'household_member']
    next_url_attrs = ['household_identifier', 'survey_schedule']


class DeceasedMemberModelWrapper(MemberStatusModelWrapperMixin):

    model = 'member.deceasedmember'
    querystring_attrs = ['survey_schedule', 'household_member']
    next_url_attrs = ['household_identifier', 'survey_schedule']


class HtcMemberModelWrapper(MemberStatusModelWrapperMixin):

    model = 'member.htcmember'
    querystring_attrs = ['survey_schedule', 'household_member']
    next_url_attrs = ['household_identifier', 'survey_schedule']


class EnrollmentChecklistModelWrapper(MemberStatusModelWrapperMixin):

    model = 'member.enrollmentchecklist'
    querystring_attrs = ['survey_schedule', 'household_member']
    next_url_attrs = ['household_identifier', 'survey_schedule']


class EnrollmentChecklistAnonymousModelWrapper(MemberStatusModelWrapperMixin):

    model = 'member.enrollmentchecklistanonymous'
    querystring_attrs = ['survey_schedule', 'household_member']
    next_url_attrs = ['household_identifier', 'survey_schedule']
    next_url_name = django_apps.get_app_config(
        'enumeration').anonymous_dashboard_url_name


class HeadOfHouseholdEligibilityModelWrapper(MemberStatusModelWrapperMixin):

    model = 'member.householdheadeligibility'
    querystring_attrs = ['survey_schedule', 'household_member']
    next_url_attrs = ['household_identifier', 'survey_schedule']


class RepresentativeEligibilityModelWrapper(HouseholdFormsModelWrapperMixin):

    model = 'member.representativeeligibility'
    querystring_attrs = ['survey_schedule', 'household_structure']
    next_url_attrs = ['household_identifier', 'survey_schedule']


class HouseholdInfoModelWrapper(HouseholdFormsModelWrapperMixin):

    model = 'member.householdinfo'
    querystring_attrs = ['survey_schedule', 'household_structure']
    next_url_attrs = ['household_identifier', 'survey_schedule']


class HouseholdMemberModelWrapper(ModelWrapper):

    model = 'member.householdmember'
    absent_member_model = 'member.absentmember'
    undecided_member_model = 'member.undecidedmember'
    moved_member_model = 'member.movedmember'
    refused_member_model = 'member.refusedmember'
    deceased_member_model = 'member.deceasedmember'
    htc_member_model = 'member.htcmember'
    enrollment_checklist_model = 'member.enrollmentchecklist'

    next_url_name = django_apps.get_app_config(
        'member_dashboard').listboard_url_name
    querystring_attrs = [
        'household_structure',
        'internal_identifier']
    next_url_attrs = [
        'household_identifier',
        'survey_schedule']

    @property
    def absent_member_model_cls(self):
        return django_apps.get_model(self.absent_member_model)

    @property
    def moved_member_model_cls(self):
        return django_apps.get_model(self.moved_member_model)

    @property
    def undecided_member_model_cls(self):
        return django_apps.get_model(self.undecided_member_model)

    @property
    def refused_member_model_cls(self):
        return django_apps.get_model(self.refused_member_model)

    @property
    def deceased_member_model_cls(self):
        return django_apps.get_model(self.deceased_member_model)

    @property
    def htc_member_model_cls(self):
        return django_apps.get_model(self.htc_member_model)

    @property
    def enrollment_checklist_model_cls(self):
        return django_apps.get_model(self.enrollment_checklist_model)

    @property
    def household_structure(self):
        return self.object.household_structure.id

    @property
    def is_consented(self):
        return self.object.is_consented

    @property
    def household_identifier(self):
        return self.object.household_structure.household.household_identifier

    @property
    def survey_schedule(self):
        return self.object.household_structure.survey_schedule_object.field_value

    @property
    def survey_schedule_object(self):
        return self.object.household_structure.survey_schedule_object

    @property
    def plot_identifier(self):
        return self.object.household_structure.household.plot.plot_identifier

    @property
    def community_name(self):
        return ' '.join(
            self.object.household_structure.household.plot.map_area.split('_'))

    @property
    def absent_members(self):
        return (AbsentMemberModelWrapper(obj)
                for obj in self.object.absentmember_set.all())

    @property
    def today_absent_member(self):
        try:
            absentee_member = self.absent_member_model_cls.objects.get(
                household_member=self.object,
                report_datetime__date=date.today())
            return AbsentMemberModelWrapper(absentee_member)
        except ObjectDoesNotExist:
            return None

    @property
    def new_absent_member(self):
        return AbsentMemberModelWrapper(
            self.absent_member_model_cls(household_member=self.object))

    @property
    def new_moved_member(self):
        return MovedMemberModelWrapper(
            self.moved_member_model_cls(household_member=self.object))

    @property
    def undecided_members(self):
        return (UndecidedMemberModelWrapper(obj)
                for obj in self.object.undecidedmember_set.all())

    @property
    def new_undecided_member(self):
        return UndecidedMemberModelWrapper(
            self.undecided_member_model_cls(household_member=self.object))

    @property
    def refused_member(self):
        try:
            return RefusedMemberModelWrapper(self.object.refusedmember)
        except ObjectDoesNotExist:
            return RefusedMemberModelWrapper(
                self.refused_member_model_cls(household_member=self.object))

    @property
    def deceased_member(self):
        try:
            return DeceasedMemberModelWrapper(self.object.deceasedmember)
        except ObjectDoesNotExist:
            return DeceasedMemberModelWrapper(
                self.deceased_member_model_cls(household_member=self.object))

    @property
    def htc_member(self):
        try:
            return HtcMemberModelWrapper(self.object.htcmember)
        except ObjectDoesNotExist:
            return HtcMemberModelWrapper(
                self.htc_member_model_cls(household_member=self.object))

    @property
    def enrollment_checklist(self):
        try:
            return EnrollmentChecklistModelWrapper(self.object.enrollmentchecklist)
        except ObjectDoesNotExist:
            return EnrollmentChecklistModelWrapper(
                self.enrollment_checklist_model_cls(household_member=self.object))
