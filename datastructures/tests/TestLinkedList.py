from linkedLIst import *
import pytest

class TestLinkedList:
    def setup_method(self):
        self.prepare_ll = SlinkedLIst()
        self.prepare_ll.insertNode(5)
        self.prepare_ll.insertNode(2)
        self.prepare_ll.insertNode(9)
        
        assert list(self.prepare_ll) == [5,2,9]
        
def test_insertNode():
    ll = SlinkedLIst()
    ll.insertNode(10)
    assert list(ll) == [10]