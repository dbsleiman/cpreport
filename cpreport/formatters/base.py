"""BaseFormatter class"""


class BaseFormatter(object):

    """Defines common methods for children to implement in order to produce report in desired format"""

    @classmethod
    def get_level_heading(cls, level, text):
        """Defines how to format a heading for a specific level

        Args:
            level: Numeric value greater than 0. The smaller the value, the larger the heading
            text: The text to display in the heading
        """
        raise NotImplementedError()

    @classmethod
    def get_table(cls, headings_list, ordered_data):
        """Defines how to format a table

        Args:
            headings_list: List of strings representing table headers
            ordered_data: List of lists representing the data rows of the table. The data is printed in the order it appears in the list
        """
        raise NotImplementedError()

    @classmethod
    def get_new_line(cls):
        """Defines how to format a new line"""
        raise NotImplementedError()

    @classmethod
    def get_full_report(cls, data):
        """Defines how to structure the entire report

        Args:
            data: A dictionary reprenting the data that goes into the report with the following keys:
                root_group: string representing the name of the root group of the account
                The remaining keys below represent dictionaries for each specific table for the report. Each dictionary contains two subkeys:
                    headings: A list of strings representing the table headings
                    data: A list of lists representing the rows and each row data
                top_csp_issues: dictionary for displaying top csp issues
                top_sva_issues: dictionary for displaying top sva issues
                top_config_issues: dictionary for dispalying top config issues
                most_common_config_issues: dictionary for displaying most common config issues
                most_common_server_config_mistakes: dictionary for displaying most common server config mistakes
                most_common_cves: dictionary for displaying most common CVEs
        """

        report_string = ''
        report_string += cls.get_level_heading(1, data['root_group'])
        report_string += cls.get_new_line()

        report_string += cls.get_level_heading(2, "Vulnerabilities by CSP account")
        report_string += cls.get_new_line()

        report_string += cls.get_level_heading(3, "For CSP-level issues")
        report_string += cls.get_new_line()
        report_string += cls.get_table(data['top_csp_issues']['headings'], data['top_csp_issues']['data'])
        report_string += cls.get_new_line()

        report_string += cls.get_level_heading(3, "For SVA issues")
        report_string += cls.get_new_line()
        report_string += cls.get_table(data['top_sva_issues']['headings'], data['top_sva_issues']['data'])
        report_string += cls.get_new_line()

        report_string += cls.get_level_heading(3, "For Server Config issues")
        report_string += cls.get_new_line()
        report_string += cls.get_table(data['top_config_issues']['headings'], data['top_config_issues']['data'])
        report_string += cls.get_new_line()

        report_string += cls.get_level_heading(2, "Most common issues")
        report_string += cls.get_new_line()

        report_string += cls.get_level_heading(3, "For Configuration Issues")
        report_string += cls.get_new_line()
        report_string += cls.get_table(data['most_common_config_issues']['headings'], data['most_common_config_issues']['data'])
        report_string += cls.get_new_line()

        report_string += cls.get_level_heading(3, "For Server Configuraiton Mistakes")
        report_string += cls.get_new_line()
        report_string += cls.get_table(data['most_common_server_config_mistakes']['headings'], data['most_common_server_config_mistakes']['data'])
        report_string += cls.get_new_line()

        report_string += cls.get_level_heading(3, "For CVEs")
        report_string += cls.get_new_line()
        report_string += cls.get_table(data['most_common_cves']['headings'], data['most_common_cves']['data'])
        report_string += cls.get_new_line()

        return report_string
