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
Created on Jan 1, 2016

@author: Patrik Dufresne <info@patrikdufresne.com>
"""

from __future__ import unicode_literals

import logging
from rdiffweb.test import WebCase
import unittest


class SettingsTest(WebCase):

    login = True

    reset_app = True

    reset_testcases = True

    def test_page(self):
        self.getPage("/settings/" + self.REPO)
        self.assertInBody("Character encoding")
        self.assertStatus(200)
        
    def test_as_another_user(self):
        # Create a nother user with admin right
        user_obj = self.app.userdb.add_user('anotheruser', 'password')
        user_obj.user_root = self.app.testcases
        user_obj.repos = ['testcases']
        
        self.getPage("/settings/anotheruser/testcases")
        self.assertInBody("Character encoding")
        self.assertStatus('200 OK')
        
        # Remove admin right
        admin = self.app.userdb.get_user('admin')
        admin.is_admin = 0
        
        # Browse admin's repos
        self.getPage("/settings/anotheruser/testcases")
        self.assertStatus('403 Forbidden')
        
    def test_set_maxage(self):
        self.getPage("/settings/" + self.REPO + "/", method="POST",
            body={'maxage': '4'})
        self.assertStatus(200)
        # Check database update
        repo_obj = self.app.userdb.get_user('admin').get_repo(self.REPO)
        self.assertEqual(4, repo_obj.maxage)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
