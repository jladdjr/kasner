#!/usr/bin/env python

"""
Execute unit tests.
"""

import sys, os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from kasner.test.test import execute_tests
execute_tests()
