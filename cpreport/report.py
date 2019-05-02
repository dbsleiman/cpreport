"""Report class"""

from .api import API
from .formatters.markdown import MarkdownFormatter
from .publishers.file import FilePublisher

class Report(object):

    formatter = MarkdownFormatter()
    publisher = FilePublisher("output", "report.md")

    @classmethod
    def generate_report(cls):
        """Generates the report string using the specified formatter and publishes using the specified publisher"""

        # get the data from the api
        data = {
            'root_group': API.get_root_group(),
            'top_csp_issues': {
                'headings': ['Rank', 'Account', 'Num Issues'],
                'data': API.get_top_csp_issues()
            },
            'top_sva_issues': {
                'headings': ['Rank', 'Account', 'Num Issues'],
                'data': API.get_top_sva_issues(),
            },
            'top_config_issues': {
                'headings': ['Rank', 'Account', 'Num Issues'],
                'data': API.get_top_config_issues(),
            },
            'most_common_config_issues': {
                'headings': ['Description', 'Count'],
                'data': API.get_most_common_config_issues(),
            },
            'most_common_server_config_mistakes': {
                'headings': ['CIS ID', 'Description', 'Count'],
                'data': API.get_most_common_server_config_mistakes(),
            },
            'most_common_cves': {
                'headings': ['CVE ID', 'CVSS Score', 'CVE Published Date', 'Link', 'Count'],
                'data': API.get_most_common_cves(),
            },
        }

        # format and publish report
        report_string = cls.formatter.get_full_report(data)
        cls.publisher.publish(report_string)
