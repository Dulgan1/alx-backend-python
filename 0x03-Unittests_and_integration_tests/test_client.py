#!/usr/bin/env python3
"""Test module for client"""
import unittest
import client


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        """Tests client.GithubOrgCloent.org """
        endpoint = "https://api.github.com/orgs/{}".format(org)
        client = client.GithubOrgClient(org)
        client.org()
        mock_get_json.assert_called_once_with(endpoint)
