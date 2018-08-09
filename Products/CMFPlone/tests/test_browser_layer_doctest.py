# -*- coding: utf-8 -*-
from .test_browser_layer import PLONETHEME_FUNCTIONAL_TESTING
from plone.testing import layered

import doctest
import unittest


def test_suite():
    return unittest.TestSuite(
        [
            layered(
                doctest.DocFileSuite(
                    'test_browserlayer.rst',
                    package='Products.CMFPlone.tests',
                    optionflags=(
                        doctest.ELLIPSIS | doctest.REPORT_ONLY_FIRST_FAILURE
                    ),
                ),
                layer=PLONETHEME_FUNCTIONAL_TESTING
            ),
        ]
    )
