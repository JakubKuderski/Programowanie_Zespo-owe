# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.social import Social  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSocialController(BaseTestCase):
    """SocialController integration test stubs"""

    def test_create_connection(self):
        """Test case for create_connection

        creates a new social media connection
        """
        query_string = [('alias', 'alias_example')]
        headers = [('value', None)]
        response = self.client.open(
            '/MATEUSZTEPLICKI/foto_portfolio_project/1.1.0/social',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_social_by_id(self):
        """Test case for delete_social_by_id

        deletes a social by ID
        """
        response = self.client.open(
            '/MATEUSZTEPLICKI/foto_portfolio_project/1.1.0/social/{id}'.format(id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_social_by_id(self):
        """Test case for get_social_by_id

        finds a social by ID
        """
        response = self.client.open(
            '/MATEUSZTEPLICKI/foto_portfolio_project/1.1.0/social/{id}'.format(id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_socials(self):
        """Test case for get_socials

        returns a array of social bindings
        """
        response = self.client.open(
            '/MATEUSZTEPLICKI/foto_portfolio_project/1.1.0/social',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
