#!/usr/bin/env python3
"""Test module for utils"""
import unittest
from unittest.mock import patch
import utils
from parameterized import parameterized
from requests.exceptions import Timeout


class TestAccessNestedMap(unittest.TestCase):
    """Test for utils.access_nested_maps"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, output):
        """Tests utils.access_nested_map with parameterized data"""
        self.assertEqual(utils.access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Tests KeyError exception raise on wrong input"""
        with self.assertRaises(KeyError) as exc:
            utils.access_nested_map(nested_map, path)
            self.assertEqual(exc.exception.arg, ('KeyError',))


class TestGetJson(unittest.TestCase):
    """Test for utils.get_json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests')
    def test_get_json(self, test_url, test_payload, mock_request):
        """Tests utils get json witb parameterized inputs"""
        mock_request.get.side_effect = Timeout
        mock_request.json.return_value = test_payload

        with self.assertRaises(Timeout):
            payload = utils.get_json(test_url)
            mock_request.get.assert_called_once()
            mock_request.get.assertEqual(payload, test_payload)
            mock_request.get.assert_called_with(test_url)
