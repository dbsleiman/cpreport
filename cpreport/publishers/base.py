"""BasePublisher class"""

class BasePublisher(object):

    """Base Publisher defines methods for child classes"""

    def publish(self, report_string):
        """Publish the report

        Args:
            report_string: String representing all report data
        """
        raise NotImplementedError()
