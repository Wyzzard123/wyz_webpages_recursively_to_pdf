"""
Example if, in the previous example, the following code failed:

    # DYNATRACE INTEGRATIONS - DYNATRACE MODULES AND THIRD PARTY INTEGRATIONS
    start_html_page = 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/'
    file_name = "(3) Dynatrace Integrations"
    regex_link_filter=r"/support/help/setup-and-configuration/integrations/(?!.*feed\.xml)"

    download_all_pdf(start_html_page, root_html_page, file_name, folder_name, filter, regex_link_filter, max_depth, attribute, html_tag, config, options, current_depth, links=[], link_set=set())

We will copy paste the list straight from the relevant LINK_.txt and use download_as_pdf
"""
from linkpdfs import *

example_integrations_links = ['https://www.dynatrace.com/support/help/setup-and-configuration/integrations/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/dynatrace-modules/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/dynatrace-modules/appmon/link-purepaths-between-dynatrace-appmon/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/dynatrace-modules/appmon/incorporate-appmon-data-into-dynatrace/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/dynatrace-modules/nam/integrate-num-and-network-monitoring/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/email-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/webhook-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/servicenow-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/jira-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/opsgenie-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/pagerduty-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/victorops-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/microsoft-teams-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/slack-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/problem-notification-systems/xmatters-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/test-automation-frameworks/dynatrace-and-load-testing-tools-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/test-automation-frameworks/dynatrace-and-loadrunner-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/test-automation-frameworks/dynatrace-and-jmeter-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/test-automation-frameworks/neotys-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/third-party-integrations/deployment-automation-frameworks/dynatrace-and-ansible-tower-integration/', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/dynatrace-modules/appmon/incorporate-appmon-data-into-dynatrace/#anchor_xproddt-integration-config', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/dynatrace-modules/appmon/incorporate-appmon-data-into-dynatrace/#anchor_xproddt-integration-metrics', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/dynatrace-modules/appmon/incorporate-appmon-data-into-dynatrace/#anchor_xproddt-integration-dialog', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/dynatrace-modules/appmon/incorporate-appmon-data-into-dynatrace/#anchor_xproddt-integration-measurepicker', 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/dynatrace-modules/appmon/incorporate-appmon-data-into-dynatrace/#anchor_xproddt-integration-measureconfig']

root_html_page = "https://www.dynatrace.com"
max_depth = 1000
filter = "suffix"
attribute='href'
html_tag='a'

config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
options={'javascript-delay': 500} # We can increase the delay to allow the pages to load a while longer
current_depth = 0


folder_name = "(1) WORKAROUND Setup and Configuration"

# DYNATRACE INTEGRATIONS - DYNATRACE MODULES AND THIRD PARTY INTEGRATIONS
start_html_page = 'https://www.dynatrace.com/support/help/setup-and-configuration/integrations/'
file_name = "(3) WORKAROUND Dynatrace Integrations"
regex_link_filter=r"/support/help/setup-and-configuration/integrations/(?!.*feed\.xml)"

# Use download_as_pdf instead
download_as_pdf(example_integrations_links, file_name, folder_name, config, options)