"""
    Apis

    IGT Cloud entities  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from igtcloud.client.services.entities.api_client import ApiClient, Endpoint as _Endpoint
from igtcloud.client.services.entities.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from igtcloud.client.services.entities.model.ai_suite_collection import AISuiteCollection
from igtcloud.client.services.entities.model.ai_suite_connection import AISuiteConnection
from igtcloud.client.services.entities.model.ai_suite_project import AISuiteProject
from igtcloud.client.services.entities.model.model4xx_message import Model4xxMessage


class IntegrationsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_ai_suite_collections_endpoint = _Endpoint(
            settings={
                'response_type': ([AISuiteCollection],),
                'auth': [
                    'csrf_token',
                    'jwt'
                ],
                'endpoint_path': '/integrations/aisuite/{connection_name}/projects/{aisuite_project_id}',
                'operation_id': 'get_ai_suite_collections',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'connection_name',
                    'aisuite_project_id',
                    'project_id',
                    'institute_id',
                    'x_fields',
                ],
                'required': [
                    'connection_name',
                    'aisuite_project_id',
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
                    'connection_name':
                        (str,),
                    'aisuite_project_id':
                        (str,),
                    'project_id':
                        (str,),
                    'institute_id':
                        (str,),
                    'x_fields':
                        (str,),
                },
                'attribute_map': {
                    'connection_name': 'connection_name',
                    'aisuite_project_id': 'aisuite_project_id',
                    'project_id': 'projectId',
                    'institute_id': 'instituteId',
                    'x_fields': 'X-Fields',
                },
                'location_map': {
                    'connection_name': 'path',
                    'aisuite_project_id': 'path',
                    'project_id': 'query',
                    'institute_id': 'query',
                    'x_fields': 'header',
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
        self.get_ai_suite_connections_endpoint = _Endpoint(
            settings={
                'response_type': ([AISuiteConnection],),
                'auth': [
                    'csrf_token',
                    'jwt'
                ],
                'endpoint_path': '/integrations/aisuite',
                'operation_id': 'get_ai_suite_connections',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_fields',
                ],
                'required': [],
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
                    'x_fields':
                        (str,),
                },
                'attribute_map': {
                    'x_fields': 'X-Fields',
                },
                'location_map': {
                    'x_fields': 'header',
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
        self.get_ai_suite_projects_endpoint = _Endpoint(
            settings={
                'response_type': ([AISuiteProject],),
                'auth': [
                    'csrf_token',
                    'jwt'
                ],
                'endpoint_path': '/integrations/aisuite/{connection_name}/projects',
                'operation_id': 'get_ai_suite_projects',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'connection_name',
                    'x_fields',
                ],
                'required': [
                    'connection_name',
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
                    'connection_name':
                        (str,),
                    'x_fields':
                        (str,),
                },
                'attribute_map': {
                    'connection_name': 'connection_name',
                    'x_fields': 'X-Fields',
                },
                'location_map': {
                    'connection_name': 'path',
                    'x_fields': 'header',
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
        self.post_ai_suite_collections_endpoint = _Endpoint(
            settings={
                'response_type': (AISuiteCollection,),
                'auth': [
                    'csrf_token',
                    'jwt'
                ],
                'endpoint_path': '/integrations/aisuite/{connection_name}/projects/{aisuite_project_id}',
                'operation_id': 'post_ai_suite_collections',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'connection_name',
                    'aisuite_project_id',
                    'project_id',
                    'institute_id',
                    'x_fields',
                ],
                'required': [
                    'connection_name',
                    'aisuite_project_id',
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
                    'connection_name':
                        (str,),
                    'aisuite_project_id':
                        (str,),
                    'project_id':
                        (str,),
                    'institute_id':
                        (str,),
                    'x_fields':
                        (str,),
                },
                'attribute_map': {
                    'connection_name': 'connection_name',
                    'aisuite_project_id': 'aisuite_project_id',
                    'project_id': 'projectId',
                    'institute_id': 'instituteId',
                    'x_fields': 'X-Fields',
                },
                'location_map': {
                    'connection_name': 'path',
                    'aisuite_project_id': 'path',
                    'project_id': 'query',
                    'institute_id': 'query',
                    'x_fields': 'header',
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

    def get_ai_suite_collections(
        self,
        connection_name,
        aisuite_project_id,
        **kwargs
    ):
        """get_ai_suite_collections  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_suite_collections(connection_name, aisuite_project_id, async_req=True)
        >>> result = thread.get()

        Args:
            connection_name (str): Name of AI Suite connection
            aisuite_project_id (str): AI Suite project id or reference

        Keyword Args:
            project_id (str): IGTCloud project. [optional]
            institute_id (str): IGTCloud institute. [optional]
            x_fields (str): An optional fields mask. [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [AISuiteCollection]
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['connection_name'] = \
            connection_name
        kwargs['aisuite_project_id'] = \
            aisuite_project_id
        return self.get_ai_suite_collections_endpoint.call_with_http_info(**kwargs)

    def get_ai_suite_connections(
        self,
        **kwargs
    ):
        """get_ai_suite_connections  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_suite_connections(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            x_fields (str): An optional fields mask. [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [AISuiteConnection]
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self.get_ai_suite_connections_endpoint.call_with_http_info(**kwargs)

    def get_ai_suite_projects(
        self,
        connection_name,
        **kwargs
    ):
        """get_ai_suite_projects  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_suite_projects(connection_name, async_req=True)
        >>> result = thread.get()

        Args:
            connection_name (str): Name of AI Suite connection

        Keyword Args:
            x_fields (str): An optional fields mask. [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [AISuiteProject]
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['connection_name'] = \
            connection_name
        return self.get_ai_suite_projects_endpoint.call_with_http_info(**kwargs)

    def post_ai_suite_collections(
        self,
        connection_name,
        aisuite_project_id,
        **kwargs
    ):
        """post_ai_suite_collections  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_ai_suite_collections(connection_name, aisuite_project_id, async_req=True)
        >>> result = thread.get()

        Args:
            connection_name (str): Name of AI Suite connection
            aisuite_project_id (str): AI Suite project id or reference

        Keyword Args:
            project_id (str): IGTCloud project. [optional]
            institute_id (str): IGTCloud institute. [optional]
            x_fields (str): An optional fields mask. [optional]
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
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AISuiteCollection
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
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['connection_name'] = \
            connection_name
        kwargs['aisuite_project_id'] = \
            aisuite_project_id
        return self.post_ai_suite_collections_endpoint.call_with_http_info(**kwargs)

