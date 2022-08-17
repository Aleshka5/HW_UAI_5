import functional
import sys
import os
def test_os_info():
    assert functional.os_info() == sys.platform

def test_pr_creator():
    assert functional.programm_creator() == 'Aleshka5'

def test_listdir():
    assert functional.view_in_folder() == os.listdir()
