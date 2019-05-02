"""API class"""

import cloudpassage


class API(object):

    api_key = '0039d8c0'
    api_secret = '89b242b61b7f285cfc860a7e8ab13601'
    session = cloudpassage.HaloSession(api_key, api_secret)
    issue = cloudpassage.Issue(session)

    def __init__(self):
        list_of_servers = self.issue.list_all()
        for s in list_of_servers:
            print(s)

    @classmethod
    def get_root_group(cls, limit=10):
        """Return root group name via HALO API."""
        return 'TEST'

    @classmethod
    def get_top_csp_issues(cls, limit=10):
        """Return top CSP issues via HALO API.

        Args:
            limit: The number of issues to return

        Returns list of lists representing data for Rank, Account Name, and Count

        """
        return [
            [i, 'CSP Account {}'.format(i), i*3] for i in range(1, limit+1)
        ]

    @classmethod
    def get_top_sva_issues(cls, limit=10):
        """Return top SVA issues via HALO API.

        Args:
            limit: The number of issues to return

        Returns list of lists representing data for Rank, Account Name, and Count

        """
        return [
            [i, 'CSP (SVA) Account {}'.format(i), i*3] for i in range(1, limit+1)
        ]

    @classmethod
    def get_top_config_issues(cls, limit=10):
        """Return top configuration issues via HALO API.

        Args:
            limit: The number of issues to return

        Returns list of lists representing data for Rank, Account Name, and Count

        """
        return [
            [i, 'CSP (Config) Account {}'.format(i), i*3] for i in range(1, limit+1)
        ]

    @classmethod
    def get_most_common_config_issues(cls, limit=10):
        """Return most common config issues via HALO API.

        Args:
            limit: The number of issues to return

        Returns list of lists representing data for Description and Counts

        """
        return [
            ['Description {}'.format(i), i*2] for i in range(1, limit+1)
        ]

    @classmethod
    def get_most_common_server_config_mistakes(cls, limit=10):
        """Return most common server configuration mistakes via HALO API.

        Args:
            limit: The number of mistakes to return

        Returns list of lists representing data for CIS ID, Description, and Counts

        """
        return [
            ['CIS ID {}'.format(i), 'CSP (Config) Account {}'.format(i), i*4] for i in range(1, limit+1)
        ]

    @classmethod
    def get_most_common_cves(cls, limit=10):
        """Return most common CVEs via HALO API.

        Args:
            limit: The number of CVEs to return

        Returns list of lists representing data for CVE ID, CVSS score, Publish Date, link to NIST page, and Counts

        """
        return [
            ['CVE ID {}'.format(i), 'CVSS Score {}'.format(i), '2018-01-02', 'http://google.com', i*5] for i in range(1, limit+1)
        ]


