# test_swarmlink.py
"""
Tests for SwarmLink module.
"""

import unittest
from swarmlink import SwarmLink

class TestSwarmLink(unittest.TestCase):
    """Test cases for SwarmLink class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SwarmLink()
        self.assertIsInstance(instance, SwarmLink)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SwarmLink()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
