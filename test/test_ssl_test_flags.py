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

from statuscake.models.ssl_test_flags import SSLTestFlags

class TestSSLTestFlags(unittest.TestCase):
    """SSLTestFlags unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SSLTestFlags:
        """Test SSLTestFlags
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SSLTestFlags`
        """
        model = SSLTestFlags()
        if include_optional:
            return SSLTestFlags(
                follow_redirects = True,
                has_mixed = True,
                has_pfs = True,
                is_broken = True,
                is_expired = True,
                is_extended = True,
                is_missing = True,
                is_revoked = True
            )
        else:
            return SSLTestFlags(
                follow_redirects = True,
                has_mixed = True,
                has_pfs = True,
                is_broken = True,
                is_expired = True,
                is_extended = True,
                is_missing = True,
                is_revoked = True,
        )
        """

    def testSSLTestFlags(self):
        """Test SSLTestFlags"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
