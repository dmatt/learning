from nose.tools import *
import journal

def setup():
	print("SETUP!")

def teardown():
	print('TEAR DOWN!')

def test_basic():
	print("I RAN!")

def test_truth():
	assert True

def test_math():
	assert 2 + 2 == 4
