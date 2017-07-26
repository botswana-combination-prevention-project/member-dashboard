from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'member_dashboard'
    listboard_template_name = 'member_dashboard/listboard.html'
    listboard_url_name = 'member_dashboard:listboard_url'
    base_template_name = 'edc_base/base.html'
    admin_site_name = 'member_admin'
    url_namespace = 'member_dashboard'
    anonymous_listboard_url_name = 'member_dashboard:anonymous_listboard_url'
