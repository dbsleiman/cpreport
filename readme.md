# CP Issues Report Generator

This package generates a report with common issues found by the CloudPassage HALO software suite.

**Requirements:**
Python 3.6+  
Pip3  

## How to use

Clone this repository to your local system and install the dependencies using pip: `pip install -r requirements.txt`.  Next, enter your CloudPassage Halo API Key and API Secret as environment variables or by any other method as defined by the [Halo APIKeyManager]([https://cloudpassage-halo-python-sdk.readthedocs.io/en/latest/api_key_manager.html](https://cloudpassage-halo-python-sdk.readthedocs.io/en/latest/api_key_manager.html)).

To generate the report, run `python generate_report.py` from the repository root. This create a markdown report file named `report.md` in the `output` directory of the repository. To view, copy and paste the file contents in any markdown viewer such as [StackEdit](https://stackedit.io/app#).

## Report Contents

The report contains the following information:
* Top 10 most-vulnerable CSP accounts
  * For CSP-level issues (Cloud Secure)
  * For Server SVA issues (Server Secure)
  * For Server configuration issues (Server Secure)
 * Top 10 most common issues:
     * For CSP Configuration issues
     * For Server Configuration Mistakes
     * For common CVEs across the entire account

## Extending Functionality

The format and publishing method of the report can be modified, and new formats and publishing methods can be created by inheriting from the respective base classes.

### Creating a new formatter
To create a new formatter, create a new file under `cpreport/formatters` which contains a class that inherits from BaseFormatter and implements the base functions, for example:
```
from .base import BaseFormatter

class HtmlFormatter(BaseFormatter):

   @classmethod
    def get_level_heading(cls, level, text):
        #impl here
        
    @classmethod
    def get_table(cls, headings_list, ordered_data):
        #impl here
        
    @classmethod
    def get_new_line(cls):
        #impl here
```

There are three class methods that must be implemented:

```
@classmethod
get_level_heading(cls, level, text)
```

Defines how to format a heading for a specific level. Has the following arguments:

* level: Numeric value greater than 0. The smaller the value, the larger the heading
* text: The text to display in the heading

```
@classmethod
get_table(cls, headings_list, ordered_data)
```


Defines how to format a table. Has the following arguments:
* headings_list: List of strings representing table headers
* ordered_data: List of lists representing the data rows of the table. The data is printed in the order it appears in the list

```
@classmethod
get_new_line(cls)
```


Defines how to format a new line

```
# optional override
@classmethod
get_full_report(cls, data)
```


Defines  how to structure the report. Has the following arguments:

* data: A dictionary reprenting the data that goes into the report with the following keys:
    * root_group: string representing the name of the root group of the account
    * The remaining keys below represent dictionaries for each specific table for the report. Each dictionary contains two subkeys:
        * headings: A list of strings representing the table headings
        * data: A list of lists representing the rows and each row data
    * top_csp_issues: dictionary for displaying top csp issues
    * top_sva_issues: dictionary for displaying top sva issues
    * top_config_issues: dictionary for dispalying top config issues
    * most_common_config_issues: dictionary for displaying most common config issues
    * most_common_server_config_mistakes: dictionary for displaying most common server config mistakes
    * most_common_cves: dictionary for displaying most common CVEs

### Creating a new publisher

To create a new publisher, create a new file under `cpreport/publishers` which contains a class that inherits from BasePublisher and implements the base functions, for example:

```
from .base import BasePublisher

class FTPPublisher(BasePublisher):

    def publish(self, report_string):
        # ftp impl logic here
```

There is only one method that needs to be implemented:
`publish(self, report_string)`

Publishes the report. Has the following arguments:
* report_string: String representing all report data

### Using different formatters and publishers

To use different formatters and publishers, modify the `formatter` and `publisher` class variables in the Report class found in `cpreport/report.py`.
