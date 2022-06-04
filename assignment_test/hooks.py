from . import __version__ as app_version

app_name = "assignment_test"
app_title = "Assignment from 8848"
app_publisher = "Aashish Vashisht"
app_description = "Customisations in Item Doctype"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "aashishvashisht6@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/assignment_test/css/assignment_test.css"
# app_include_js = "/assets/assignment_test/js/assignment_test.js"

# include js, css files in header of web template
# web_include_css = "/assets/assignment_test/css/assignment_test.css"
# web_include_js = "/assets/assignment_test/js/assignment_test.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "assignment_test/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
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

# Installation
# ------------

# before_install = "assignment_test.install.before_install"
# after_install = "assignment_test.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "assignment_test.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Item": {
		"validate":[
					"assignment_test.doc_events.item.set_custom_fields_values",
					"assignment_test.doc_events.item.set_conversion_factor",
				],
		
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"assignment_test.tasks.all"
# 	],
# 	"daily": [
# 		"assignment_test.tasks.daily"
# 	],
# 	"hourly": [
# 		"assignment_test.tasks.hourly"
# 	],
# 	"weekly": [
# 		"assignment_test.tasks.weekly"
# 	]
# 	"monthly": [
# 		"assignment_test.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "assignment_test.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "assignment_test.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "assignment_test.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"assignment_test.auth.validate"
# ]

fixtures  = [
		{
			"dt":"Custom Field",
			"filters":{"name":["in",
								[
								"Item-yield",
								"Item-height",
								"Item-width",
								"Item-length",
								"UOM Conversion Detail-formula"
								]
					]}
		},
		{
			"dt":"Item Attribute",
			"filters":{"name":["in",[
									"Width",
									"Height",
									"Yield"
								]
			]}
		}
		
]
