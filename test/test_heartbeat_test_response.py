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

from statuscake.models.heartbeat_test_response import HeartbeatTestResponse

class TestHeartbeatTestResponse(unittest.TestCase):
    """HeartbeatTestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HeartbeatTestResponse:
        """Test HeartbeatTestResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HeartbeatTestResponse`
        """
        model = HeartbeatTestResponse()
        if include_optional:
            return HeartbeatTestResponse(
                data = statuscake.models.heartbeat_test.HeartbeatTest(
                    id = '', 
                    name = '', 
                    url = '', 
                    period = 3E+1, 
                    contact_groups = [
                        ''
                        ], 
                    host = '', 
                    last_tested_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    paused = True, 
                    status = 'down', 
                    tags = [
                        ''
                        ], 
                    uptime = 0, )
            )
        else:
            return HeartbeatTestResponse(
                data = statuscake.models.heartbeat_test.HeartbeatTest(
                    id = '', 
                    name = '', 
                    url = '', 
                    period = 3E+1, 
                    contact_groups = [
                        ''
                        ], 
                    host = '', 
                    last_tested_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    paused = True, 
                    status = 'down', 
                    tags = [
                        ''
                        ], 
                    uptime = 0, ),
        )
        """

    def testHeartbeatTestResponse(self):
        """Test HeartbeatTestResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
