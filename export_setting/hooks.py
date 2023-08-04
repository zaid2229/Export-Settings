from . import __version__ as app_version
# from  export_setting.export_setting.doctype.export_settings.export_overrides import get_doctype_fields

import frappe
# from  export_setting.export_setting.doctype.export_settings.export_overrides import get_doctype_fields
# from  export_setting.export_setting.doctype.export_settings.apply_export_settings import apply_export_settings



app_name = "export_setting"
app_title = "Export Setting"
app_publisher = "zaid"
app_description = "This App Used to Set preselected fields for export"
app_email = "zaid@standardtouch.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/export_setting/css/export_setting.css"
# app_include_js = "/assets/export_setting/js/export_setting.js"

# include js, css files in header of web template
# web_include_css = ["/assets/export_setting/js/custom_export11.js"]
# web_include_js = "/assets/export_setting/js/ce4.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "export_setting/public/scss/website"
# def boot_session(bootinfo):
#     frappe.core.doctype.data_export.exporter.export_data = get_doctype_fields


# override_whitelisted_methods = {
#     "frappe.core.doctype.data_export.exporter.export_data": get_doctype_fields
# }

# doc_events = {
#     "Data Export": {
#         "before_insert": apply_export_settings,  # Reference your hook function here
#     }
# }

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/data_export1.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}
app_include_js = ["/assets/export_setting/js/dd10.js", "/assets/export_setting/js/cetest9.js"]
web_include_css = ["/assets/export_setting/css/bt.css"]

# doctype_js ={
#     "Data Export" : "public/js/data_export1.js"
# }



# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "/assets/export_setting/js/custom_export10.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "export_setting.utils.jinja_methods",
#	"filters": "export_setting.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "export_setting.install.before_install"
# after_install = "export_setting.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "export_setting.uninstall.before_uninstall"
# after_uninstall = "export_setting.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "export_setting.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"export_setting.tasks.all"
#	],
#	"daily": [
#		"export_setting.tasks.daily"
#	],
#	"hourly": [
#		"export_setting.tasks.hourly"
#	],
#	"weekly": [
#		"export_setting.tasks.weekly"
#	],
#	"monthly": [
#		"export_setting.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "export_setting.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "export_setting.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "export_setting.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["export_setting.utils.before_request"]
# after_request = ["export_setting.utils.after_request"]

# Job Events
# ----------
# before_job = ["export_setting.utils.before_job"]
# after_job = ["export_setting.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"export_setting.auth.validate"
# ]
