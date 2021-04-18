import os, sys, json, shutil
import subprocess

sys.path.append('../')

from nbx import merge

'''
    run tests from tests dir:
    nbx/tests>pytest -vv [filename]
'''
TEMPLATE_DIR   = 'test_templates'
TEST_STAGE_DIR = 'test_stages'

def test_merge_1():
    '''
        test merge.give_answer() functionality

        setup: using only a single simple pre-setup notebook

        verify:
            - does an .nbx/ dir get created (in it's abscence)?
            - does a  .nbx/master.json get created (in it's absence)?
            - does the appropriate content get written into a cell?
            - can we load master.json with json module?
            - does the dict loaded from json have the right keys/values?
            - tests simple multiline inputs + outputs

        caveats / does not test:
            - if .nbx / .nbx/master.json already exists
            - `term` argument looks for "send_answer"

        notes:
            - need to add double backslash ("\\") to the contents 
              of a json when inputting a literal TEST_DATA
            - if this notebook is re-opened by jupyter in templates, 
              the "id" value will change to another guid

    '''
    THIS_TEMPLATE_DIR = 'merge.test_merge_1'
    
    # Setup
    src = os.path.join(TEMPLATE_DIR, THIS_TEMPLATE_DIR)
    dst = os.path.join(TEST_STAGE_DIR, THIS_TEMPLATE_DIR)
    ret = subprocess.check_output(['cp', '-r', str(src), str(dst)])
    starting_cwd = os.getcwd()

    # Execute Action
    os.chdir(dst)
    merge.give_answer('test_book_1.ipynb', term="send_answer")

    # Test Conditions
    list_files = os.listdir('.')
    assert '.nbx' in list_files, "no .nbx dir created"
    
    try:
        with open('.nbx/master.json', 'r') as f:
            lines = f.readlines()
    except:
        raise 
    
    assert len(lines) == 1, "master.json contents has length different from 1"

    TEST_DATA = '''{"cells": [{"cell_type": "code", "execution_count": 10, "id": "3778060b", "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["merge.test_merge_1\\n", "multiline\\n"]}], "source": ["print(\\"merge.test_merge_1\\")\\n", "\\n", "print(\\"multiline\\")"]}]}'''
    assert lines[0] == TEST_DATA, f"""contents loaded from master.json does not match expected\n\nexpected:\n{TEST_DATA}\n\nactual:\n{lines[0]}"""

    # Tear Down
    os.chdir(starting_cwd)
    shutil.rmtree(dst)
