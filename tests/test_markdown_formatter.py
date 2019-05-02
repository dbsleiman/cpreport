import sys
sys.path.append('./')

from cpreport.formatters.markdown import MarkdownFormatter

class MarkdownFormatterTests(object):

    def test_formatting(self):

        # test headings
        assert MarkdownFormatter.get_level_heading(1, 'test') == '# test'
        assert MarkdownFormatter.get_level_heading(2, 'test') == '## test'

        # test table
        headings = ['h1', 'h2']
        data = [['1', '2'], ['3', '4']]
        expected = '| h1 | h2 |\n|:---:|:---:|\n| 1 | 2 |\n| 3 | 4 |\n'
        assert MarkdownFormatter.get_table(headings, data) == expected

        # test new line
        assert MarkdownFormatter.get_new_line() == '  \n'

MarkdownFormatterTests().test_formatting()
