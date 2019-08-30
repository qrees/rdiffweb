#!/usr/bin/python
# -*- coding: utf-8 -*-
# rdiffweb, A web interface to rdiff-backup repositories
# Copyright (C) 2019 rdiffweb contributors
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Created on Aug 30, 2019

@author: Patrik Dufresne <info@patrikdufresne.com>
"""

from __future__ import unicode_literals

import logging
from rdiffweb.test import WebCase
import unittest


class StatusTest(WebCase):

    login = True

    reset_app = True

    reset_testcases = True

    def _status(self, failures=False, date=None):
        url = "/status/"
        if date:
            url += '?date=' + str(date)
        if failures:
            url += '?failures=T'
        self.getPage(url)

    def test_page(self):
        self._status()
        self.assertStatus(200)
        self.assertInBody('There are no recent backups to display.')
        self.assertInBody('Show all')
        self.assertInBody('Show errors only')
        
    def test_page_failures(self):
        self._status(failures=True)
        self.assertStatus(200)
        self.assertInBody('There are no recent backups with errors.')
        
    def test_page_date(self):
        self._status(date=1454448640)
        self.assertStatus(200)
        self.assertInBody('Successful')


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
