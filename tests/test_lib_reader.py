# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Development Team: Stanislav WEB
"""

import unittest2 as unittest
from src.lib.reader import Reader, ReaderError


class TestReader(unittest.TestCase):
    """TestReader class"""

    def setUp(self):
        self.reader = Reader(browser_config={})

    def test_total_lines(self):
        """ Reader.total_lines test """

        self.assertIs(type(self.reader.total_lines), int)

    def test_get_user_agents_empty(self):
        """ Reader.get_user_agents() empty test """

        self.assertIs(type(self.reader.get_user_agents()), list)

    def test_get_ignored_list_empty(self):
        """ Reader.get_ignored_list() empty test """

        self.assertIs(type(self.reader.get_ignored_list()), list)

    def test_get_proxies_empty(self):
        """ Reader.get_proxies() empty test """

        self.assertIs(type(self.reader.get_user_agents()), list)

if __name__ == "__main__":
    unittest.main()