#!/usr/bin/env python3
"""Test module for utils"""
import unittest
import utils
from parameterized import parameterized


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
