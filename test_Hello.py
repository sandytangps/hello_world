from hello import *

def test_Hello():
    assert hello() == "Hello World !"

def test_HelloUser():
    assert hello('User') == "Hello World User!"