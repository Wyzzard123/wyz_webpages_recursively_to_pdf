"""
This is an example of how to download documents from a given topic and organise them into folders.

This uses Dynatrace's Setup and Configuration page as an example. See https://www.dynatrace.com/robots.txt which allows web crawling of the pages below.
"""

from linkpdfs import *

######COMMON##############################
root_html_page = "https://www.dynatrace.com"
max_depth = 1000
filter = "suffix"
attribute='href'
html_tag='a'

config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
options={'javascript-delay': 1000}
current_depth = 0



######TOPICS##############################

######(1) SETUP AND CONFIGURATION######
folder_name = "(1) Setup and Configuration"

# DYNATRACE ONEAGENT
start_html_page = 'https://www.dynatrace.com/support/help/setup-and-configuration/dynatrace-oneagent/'
file_name = "(1) Dynatrace OneAgent"
regex_link_filter=r"/support/help/setup-and-configuration/dynatrace-oneagent/(?!.*feed\.xml)"

download_all_pdf(start_html_page, root_html_page, file_name, folder_name, filter, regex_link_filter, max_depth, attribute, html_tag, config, options, current_depth, links=[], link_set=set())

# DYNATRACE ACTIVEGATE
start_html_page = 'https://www.dynatrace.com/support/help/setup-and-configuration/dynatrace-activegate/'
file_name = "(2) Dynatrace ActiveGate"
regex_link_filter=r"/support/help/setup-and-configuration/dynatrace-activegate/(?!.*feed\.xml)"

download_all_pdf(start_html_page, root_html_page, file_name, folder_name, filter, regex_link_filter, max_depth, attribute, html_tag, config, options, current_depth, links=[], link_set=set())

# DYNATRACE INTEGRATIONS - DYNATRACE MODULES AND THIRD PARTY INTEGRATIONS
start_html_page = 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/'
file_name = "(3) Dynatrace Integrations"
regex_link_filter=r"/support/help/setup-and-configuration/integrations/(?!.*feed\.xml)(?!\#)"

download_all_pdf(start_html_page, root_html_page, file_name, folder_name, filter, regex_link_filter, max_depth, attribute, html_tag, config, options, current_depth, links=[], link_set=set())


####CONTINUE...###

######Everything######
folder_name = "Dynatrace Documentation"

# All Dynatrace Documentation
start_html_page = 'https://www.dynatrace.com/support/help/'
file_name = "Dynatrace Documentation Consolidated"
regex_link_filter = r"/support/help/(?!.*feed\.xml)"

download_all_pdf(start_html_page, root_html_page, file_name, folder_name, filter, regex_link_filter, 3, attribute, html_tag, config, options, current_depth)

