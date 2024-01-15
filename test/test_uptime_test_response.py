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

from statuscake.models.uptime_test_response import UptimeTestResponse

class TestUptimeTestResponse(unittest.TestCase):
    """UptimeTestResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UptimeTestResponse:
        """Test UptimeTestResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UptimeTestResponse`
        """
        model = UptimeTestResponse()
        if include_optional:
            return UptimeTestResponse(
                data = statuscake.models.uptime_test.UptimeTest(
                    id = '', 
                    name = '', 
                    test_type = 'DNS', 
                    website_url = '', 
                    check_rate = 0, 
                    confirmation = 0, 
                    contact_groups = [
                        ''
                        ], 
                    custom_header = '', 
                    dns_ips = [
                        ''
                        ], 
                    dns_server = '', 
                    do_not_find = True, 
                    enable_ssl_alert = True, 
                    final_endpoint = '', 
                    find_string = '', 
                    follow_redirects = True, 
                    include_header = True, 
                    host = '', 
                    last_tested_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    next_location = '', 
                    paused = True, 
                    port = 0, 
                    post_body = '', 
                    post_raw = '', 
                    processing = True, 
                    processing_on = '', 
                    processing_state = 'complete', 
                    servers = [
                        statuscake.models.monitoring_location.MonitoringLocation(
                            description = '', 
                            ipv4 = '', 
                            ipv6 = '', 
                            region = '', 
                            region_code = '', 
                            status = 'down', )
                        ], 
                    status = 'down', 
                    status_codes = [
                        ''
                        ], 
                    tags = [
                        ''
                        ], 
                    timeout = 5, 
                    trigger_rate = 0, 
                    uptime = 0, 
                    use_jar = True, 
                    user_agent = '', )
            )
        else:
            return UptimeTestResponse(
                data = statuscake.models.uptime_test.UptimeTest(
                    id = '', 
                    name = '', 
                    test_type = 'DNS', 
                    website_url = '', 
                    check_rate = 0, 
                    confirmation = 0, 
                    contact_groups = [
                        ''
                        ], 
                    custom_header = '', 
                    dns_ips = [
                        ''
                        ], 
                    dns_server = '', 
                    do_not_find = True, 
                    enable_ssl_alert = True, 
                    final_endpoint = '', 
                    find_string = '', 
                    follow_redirects = True, 
                    include_header = True, 
                    host = '', 
                    last_tested_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    next_location = '', 
                    paused = True, 
                    port = 0, 
                    post_body = '', 
                    post_raw = '', 
                    processing = True, 
                    processing_on = '', 
                    processing_state = 'complete', 
                    servers = [
                        statuscake.models.monitoring_location.MonitoringLocation(
                            description = '', 
                            ipv4 = '', 
                            ipv6 = '', 
                            region = '', 
                            region_code = '', 
                            status = 'down', )
                        ], 
                    status = 'down', 
                    status_codes = [
                        ''
                        ], 
                    tags = [
                        ''
                        ], 
                    timeout = 5, 
                    trigger_rate = 0, 
                    uptime = 0, 
                    use_jar = True, 
                    user_agent = '', ),
        )
        """

    def testUptimeTestResponse(self):
        """Test UptimeTestResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
