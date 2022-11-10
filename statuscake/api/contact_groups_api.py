"""
    StatusCake API

    Copyright (c) 2022

    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or  sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.

    API Version: 1.0.1
    Contact: support@statuscake.com

    Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.
"""


import re  # noqa: F401
import sys  # noqa: F401

from statuscake.api_client import ApiClient, Endpoint as _Endpoint
from statuscake.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from statuscake.model.api_error import APIError
from statuscake.model.api_response import APIResponse
from statuscake.model.contact_group_response import ContactGroupResponse
from statuscake.model.contact_groups import ContactGroups


class ContactGroupsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_contact_group_endpoint = _Endpoint(
            settings={
                'response_type': (APIResponse,),
                'auth': [],
                'endpoint_path': '/contact-groups',
                'operation_id': 'create_contact_group',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'name',
                    'email_addresses',
                    'integrations',
                    'mobile_numbers',
                    'ping_url',
                ],
                'required': [
                    'name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'name':
                        (str,),
                    'email_addresses':
                        ([str],),
                    'integrations':
                        ([str],),
                    'mobile_numbers':
                        ([str],),
                    'ping_url':
                        (str,),
                },
                'attribute_map': {
                    'name': 'name',
                    'email_addresses': 'email_addresses',
                    'integrations': 'integrations',
                    'mobile_numbers': 'mobile_numbers',
                    'ping_url': 'ping_url',
                },
                'location_map': {
                    'name': 'form',
                    'email_addresses': 'form',
                    'integrations': 'form',
                    'mobile_numbers': 'form',
                    'ping_url': 'form',
                },
                'collection_format_map': {
                    'email_addresses': 'csv',
                    'integrations': 'csv',
                    'mobile_numbers': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )
        self.delete_contact_group_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/contact-groups/{group_id}',
                'operation_id': 'delete_contact_group',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_id',
                ],
                'required': [
                    'group_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'group_id':
                        (str,),
                },
                'attribute_map': {
                    'group_id': 'group_id',
                },
                'location_map': {
                    'group_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_contact_group_endpoint = _Endpoint(
            settings={
                'response_type': (ContactGroupResponse,),
                'auth': [],
                'endpoint_path': '/contact-groups/{group_id}',
                'operation_id': 'get_contact_group',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_id',
                ],
                'required': [
                    'group_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'group_id':
                        (str,),
                },
                'attribute_map': {
                    'group_id': 'group_id',
                },
                'location_map': {
                    'group_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_contact_groups_endpoint = _Endpoint(
            settings={
                'response_type': (ContactGroups,),
                'auth': [],
                'endpoint_path': '/contact-groups',
                'operation_id': 'list_contact_groups',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'page',
                    'limit',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'page',
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('page',): {

                        'inclusive_minimum': 1,
                    },
                    ('limit',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'page':
                        (int,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'page': 'page',
                    'limit': 'limit',
                },
                'location_map': {
                    'page': 'query',
                    'limit': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_contact_group_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [],
                'endpoint_path': '/contact-groups/{group_id}',
                'operation_id': 'update_contact_group',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'group_id',
                    'name',
                    'email_addresses',
                    'integrations',
                    'mobile_numbers',
                    'ping_url',
                ],
                'required': [
                    'group_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'group_id':
                        (str,),
                    'name':
                        (str,),
                    'email_addresses':
                        ([str],),
                    'integrations':
                        ([str],),
                    'mobile_numbers':
                        ([str],),
                    'ping_url':
                        (str,),
                },
                'attribute_map': {
                    'group_id': 'group_id',
                    'name': 'name',
                    'email_addresses': 'email_addresses',
                    'integrations': 'integrations',
                    'mobile_numbers': 'mobile_numbers',
                    'ping_url': 'ping_url',
                },
                'location_map': {
                    'group_id': 'path',
                    'name': 'form',
                    'email_addresses': 'form',
                    'integrations': 'form',
                    'mobile_numbers': 'form',
                    'ping_url': 'form',
                },
                'collection_format_map': {
                    'email_addresses': 'csv',
                    'integrations': 'csv',
                    'mobile_numbers': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )

    def create_contact_group(
        self,
        name,
        **kwargs
    ):
        """Create a contact group  # noqa: E501

        Creates a contact group with the given parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_contact_group(name, async_req=True)
        >>> result = thread.get()

        Args:
            name (str): Name of the contact group

        Keyword Args:
            email_addresses ([str]): List of email addresses. [optional]
            integrations ([str]): List of integration IDs. [optional]
            mobile_numbers ([str]): List of international format mobile phone numbers. [optional]
            ping_url (str): URL or IP address of an endpoint to push uptime events. Currently this only supports HTTP GET endpoints. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            APIResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['name'] = \
            name
        return self.create_contact_group_endpoint.call_with_http_info(**kwargs)

    def delete_contact_group(
        self,
        group_id,
        **kwargs
    ):
        """Delete a contact group  # noqa: E501

        Deletes a contact group with the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_contact_group(group_id, async_req=True)
        >>> result = thread.get()

        Args:
            group_id (str): Contact group ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['group_id'] = \
            group_id
        return self.delete_contact_group_endpoint.call_with_http_info(**kwargs)

    def get_contact_group(
        self,
        group_id,
        **kwargs
    ):
        """Retrieve a contact group  # noqa: E501

        Returns a contact group with the given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_contact_group(group_id, async_req=True)
        >>> result = thread.get()

        Args:
            group_id (str): Contact group ID

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ContactGroupResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['group_id'] = \
            group_id
        return self.get_contact_group_endpoint.call_with_http_info(**kwargs)

    def list_contact_groups(
        self,
        **kwargs
    ):
        """Get all contact groups  # noqa: E501

        Returns a list of contact groups for an account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_contact_groups(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            page (int): Page of results. [optional] if omitted the server will use the default value of 1
            limit (int): The number of contact groups to return per page. [optional] if omitted the server will use the default value of 25
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ContactGroups
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.list_contact_groups_endpoint.call_with_http_info(**kwargs)

    def update_contact_group(
        self,
        group_id,
        **kwargs
    ):
        """Update a contact group  # noqa: E501

        Updates a contact group with the given parameters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_contact_group(group_id, async_req=True)
        >>> result = thread.get()

        Args:
            group_id (str): Contact group ID

        Keyword Args:
            name (str): Name of the contact group. [optional]
            email_addresses ([str]): List of email addresses. [optional]
            integrations ([str]): List of integration IDs. [optional]
            mobile_numbers ([str]): List of international format mobile phone numbers. [optional]
            ping_url (str): URL or IP address of an endpoint to push uptime events. Currently this only supports HTTP GET endpoints. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['group_id'] = \
            group_id
        return self.update_contact_group_endpoint.call_with_http_info(**kwargs)
