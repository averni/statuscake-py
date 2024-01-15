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

from statuscake.models.contact_group_response import ContactGroupResponse

class TestContactGroupResponse(unittest.TestCase):
    """ContactGroupResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContactGroupResponse:
        """Test ContactGroupResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContactGroupResponse`
        """
        model = ContactGroupResponse()
        if include_optional:
            return ContactGroupResponse(
                data = statuscake.models.contact_group.ContactGroup(
                    id = '', 
                    name = '', 
                    email_addresses = [
                        ''
                        ], 
                    integrations = [
                        ''
                        ], 
                    mobile_numbers = [
                        ''
                        ], 
                    ping_url = '', )
            )
        else:
            return ContactGroupResponse(
                data = statuscake.models.contact_group.ContactGroup(
                    id = '', 
                    name = '', 
                    email_addresses = [
                        ''
                        ], 
                    integrations = [
                        ''
                        ], 
                    mobile_numbers = [
                        ''
                        ], 
                    ping_url = '', ),
        )
        """

    def testContactGroupResponse(self):
        """Test ContactGroupResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
