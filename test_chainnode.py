# test_chainnode.py
"""
Tests for ChainNode module.
"""

import unittest
from chainnode import ChainNode

class TestChainNode(unittest.TestCase):
    """Test cases for ChainNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainNode()
        self.assertIsInstance(instance, ChainNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
