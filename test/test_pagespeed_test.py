# coding: utf-8

"""
    StatusCake API

    StatusCake API endpoints to manage monitoring resources.  # Authentication  Documentation on API authentication can be found [here](https://developers.statuscake.com/guides/api/authentication).  # Ratelimiting  Documentation on API ratelimiting can be found [here](https://developers.statuscake.com/guides/api/ratelimiting).  # Errors  Documentation on error handling can be found [here](https://developers.statuscake.com/guides/api/errors).  # Handling Input Parameters  Documentation on input parameters, including how to pass arrays to API endpoints can be found [here](https://developers.statuscake.com/guides/api/parameters). 

    The version of the OpenAPI document: 1.2.0
    Contact: support@statuscake.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from statuscake.models.pagespeed_test import PagespeedTest

class TestPagespeedTest(unittest.TestCase):
    """PagespeedTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PagespeedTest:
        """Test PagespeedTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PagespeedTest`
        """
        model = PagespeedTest()
        if include_optional:
            return PagespeedTest(
                id = '',
                name = '',
                website_url = '',
                check_rate = 60,
                alert_bigger = 0,
                alert_slower = 0,
                alert_smaller = 0,
                contact_groups = [
                    ''
                    ],
                latest_stats = statuscake.models.pagespeed_test_stats.PagespeedTestStats(
                    filesize = 0, 
                    has_issue = True, 
                    loadtime = 0, 
                    requests = 0, 
                    latest_issue = '', ),
                location = '',
                paused = True
            )
        else:
            return PagespeedTest(
                id = '',
                name = '',
                website_url = '',
                check_rate = 60,
                alert_bigger = 0,
                alert_slower = 0,
                alert_smaller = 0,
                contact_groups = [
                    ''
                    ],
                location = '',
                paused = True,
        )
        """

    def testPagespeedTest(self):
        """Test PagespeedTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
