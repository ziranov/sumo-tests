'''
Created on Aug 12, 2010

@author: mozilla
'''

from selenium import selenium
import vars
import unittest

import search_page

class SearchDecoding(unittest.TestCase):


    def setUp(self):
        self.selenium = selenium(vars.ConnectionParameters.server, vars.ConnectionParameters.port, vars.ConnectionParameters.browser, vars.ConnectionParameters.baseurl)
        self.selenium.start()
        self.selenium.set_timeout(vars.ConnectionParameters.page_load_timeout)

    def tearDown(self):
        self.selenium.stop()

    def test_search_decoding(self):
        sel                   = self.selenium
        search_page_obj       = search_page.SearchPage(sel)
        
        search_term = "%3D"  
        search_page_obj.go_to_search_page()     
        search_page_obj.do_search_on_search_box(search_term)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter = counter + 1
            else:
                not_found = False
        self.assertNotEqual("=", sel.get_value(search_page_obj.search_box))
        self.assertEqual(search_term, sel.get_value(search_page_obj.search_box))
        
        search_term = "%25D"  
        search_page_obj.go_to_search_page()     
        search_page_obj.do_search_on_search_box(search_term)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter = counter + 1
            else:
                not_found = False
        self.assertNotEqual("=", sel.get_value(search_page_obj.search_box))
        self.assertEqual(search_term, sel.get_value(search_page_obj.search_box))
        
        search_term = "&lsquo"  
        search_page_obj.go_to_search_page()     
        search_page_obj.do_search_on_search_box(search_term)
        not_found = True
        counter = 0
        while(not_found and counter < 3):
            if(not(search_page_obj.is_search_available())):
                search_page_obj.refresh()
                counter = counter + 1
            else:
                not_found = False
        self.assertNotEqual("'", sel.get_value(search_page_obj.search_box))
        self.assertEqual(search_term, sel.get_value(search_page_obj.search_box))
 

if __name__ == "__main__":
    unittest.main()