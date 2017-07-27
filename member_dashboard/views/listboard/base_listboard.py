from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_dashboard.views import ListboardView

from household_dashboard.view_mixins import HouseholdQuerysetViewMixin
from member.model_wrappers import HouseholdMemberModelWrapper
from plot_dashboard.view_mixins import PlotQuerysetViewMixin
from survey import SurveyViewMixin, SurveyQuerysetViewMixin


class BaseListboardView(SurveyViewMixin, AppConfigViewMixin,
                        EdcBaseViewMixin, HouseholdQuerysetViewMixin,
                        PlotQuerysetViewMixin, SurveyQuerysetViewMixin,
                        ListboardView):

    app_config_name = 'member_dashboard'
    navbar_item_selected = 'member_dashboard'
    navbar_name = 'default'
    model = 'member.householdmember'
    model_wrapper_class = HouseholdMemberModelWrapper

    plot_queryset_lookups = ['household_structure', 'household', 'plot']
    household_queryset_lookups = ['household_structure', 'household']

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            k: v for k, v in self.url_names(
                'anonymous_listboard_url_name')})
        return context
