#-------------------------------------------------------------------------------
# Name:        Registration Form
# Purpose:
#
# Author:      suresh.kumar
#
# Created:     21-07-2018
# Copyright:   (c) suresh.kumar 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import unittest
import os
import sys
import traceback
import pytest
#from flaky import flaky

dir_path = os.path.dirname(os.path.realpath(__file__))
folder_path=os.path.abspath(os.path.join(dir_path, os.pardir))

sys.path.insert(0,folder_path+"\Syslibrary")
sys.path.insert(0,folder_path+"\Library")

from datadriver import readjson
jsonread1 = readjson()

from Launchapplication import launchapplication
application = launchapplication()

tf = 'test_TestcaseNo100003'

#Test case No : 100003
#@pytest.mark.skip("no need to run now")
@pytest.mark.smoke
class TestcaseNo100003(unittest.TestCase):
    def test_TestcaseNo100003(self) :
        json_files = jsonread1.multiplejsonread()
        browser_json_files = jsonread1.multiplejsonbrowser()
        if len(json_files) == len(browser_json_files):
            i=0
            while i<len(json_files):
             try:
                env = jsonread1.jsonread(folder_path+'\Env'+'/'+ browser_json_files[i])
                registrationform_testdata = jsonread1.jsonread(folder_path+'\Data'+'/'+ json_files[i])
                browser = application.intializebrowser(env)
                application.inputurl(browser)
                self.assertEqual(browser.title,'Google')
             except Exception:
                traceback.print_exc()
                browser.save_screenshot(folder_path+'\Screenshots\Testcase-%s.png' %tf)
                self.fail("Test case No : 100002 is failed")
             finally:
                application.closebrower(browser)
                i=i+1
        else:
            print("not equal")

#if __name__ == '__main__':
    #unittest.main()

