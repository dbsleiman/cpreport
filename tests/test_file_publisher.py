import sys
sys.path.append('./')

from cpreport.publishers.file import FilePublisher
import os

class FilePublisherTests(object):

    def test_publish(self):

        directory = 'temp_test_dir'
        file_name = 'test_file_name'
        report_string = 'test_report_data'

        # remove files and directory from any old runs
        try:
            os.remove('{}/{}'.format(directory, file_name))
            os.rmdir(directory)
        except:
            pass

        # make sure they are deleted
        assert not os.path.exists(directory)

        publisher = FilePublisher(directory, file_name)
        publisher.publish(report_string)

        f = open('{}/{}'.format(directory, file_name), 'r')
        file_contents = f.read()

        assert report_string == file_contents

FilePublisherTests().test_publish()
