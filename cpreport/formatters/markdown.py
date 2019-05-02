"""MarkdownFormatter class"""

from .base import BaseFormatter

class MarkdownFormatter(BaseFormatter):

    """Implementation of BaseFormatter for Markdown"""

    @classmethod
    def get_level_heading(cls, level, text):
        leading_pound_signs = ''.join(['#' for i in range(0, level)])
        return '{} {}'.format(leading_pound_signs, text)

    @classmethod
    def get_table(cls, headings_list, ordered_data):
        table = '|'

        # headings
        table += ''.join([' {} |'.format(heading) for heading in headings_list])
        table += '\n'

        # col definitions
        table += '|'
        table += ''.join([':---:|' for i in range(0, len(headings_list))])
        table += '\n'

        #data
        for data_list in ordered_data:
            table += '|'
            table += ''.join([' {} |'.format(data) for data in data_list])
            table += '\n'

        return table

    @classmethod
    def get_new_line(cls):
        return "  \n"
