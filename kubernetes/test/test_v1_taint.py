# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.6.7
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1_taint import V1Taint


class TestV1Taint(unittest.TestCase):
    """ V1Taint unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1Taint(self):
        """
        Test V1Taint
        """
        model = kubernetes.client.models.v1_taint.V1Taint()


if __name__ == '__main__':
    unittest.main()
