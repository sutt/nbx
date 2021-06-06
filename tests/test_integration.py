import os, sys, json, shutil, time
import subprocess
import signal

'''
    run tests from tests dir:
    nbx/tests>pytest -vv [filename]
'''

from modules.basic import basic_1


TEMPLATE_DIR   = 'test_templates'
TEST_STAGE_DIR = 'test_stages'



def test_basic_1():
    '''
        test:
             teacher::send_answer()
             student::receive_answer()

        stage: init.clone
            - no existing .nbx/master.json
            -  

        base notebook: 
            - same for student and teacher; blank besides relative import

        verify:
            -

        caveats / does not test:
            -

        notes:
            - need to add double backslash ("\\") to the contents 
              of a json when inputting a literal TEST_DATA
            - if this notebook is re-opened by jupyter in templates, 
              the "id" value will change to another guid

    '''
    THIS_TEMPLATE_NAME   = 'init.clone.1'
    THIS_STAGE_NAME      = 'basic_1'
    
    starting_cwd = os.getcwd()

    # Setup Stage Dir
    src = os.path.join(TEMPLATE_DIR,   THIS_TEMPLATE_NAME)
    dst = os.path.join(TEST_STAGE_DIR, THIS_STAGE_NAME)
    ret = subprocess.check_output(['cp', '-r', str(src), str(dst)])

    # Make Stage - git commands
    os.chdir(dst)
    ret = subprocess.check_output(["mkstage.bat"])

    # Run Separate NB Servers
    # must be Popen so this doenst block the rest of the execution
    # ret = subprocess.Popen('test-setup.bat')
    
    os.chdir("teacher")
    proc_teacher_server = subprocess.Popen([
        'jupyter',
        'notebook',
        '--port=9200', 
        '--no-browser',
        "--NotebookApp.token=''",
        "--NotebookApp.password=''"
        ],shell=True,
        
        )

    os.chdir("../student")
    proc_student_server = subprocess.Popen([
        'jupyter',
        'notebook',
        '--port=9200', 
        '--no-browser',
        "--NotebookApp.token=''",
        "--NotebookApp.password=''"
    ],shell=True,)
    
    time.sleep(5)
    print("done launching servers")

    
    # Perform Actions
    basic_1()

    # Test Conditions
    # list_files = os.listdir('.')
    # assert '.nbx' in list_files, "no .nbx dir created"
    
    # try:
    #     with open('.nbx/master.json', 'r') as f:
    #         lines = f.readlines()
    # except:
    #     raise 
    
    # assert len(lines) == 1, "master.json contents has length different from 1"

    # TEST_DATA = '''{"cells": [{"cell_type": "code", "execution_count": 10, "id": "3778060b", "metadata": {}, "outputs": [{"name": "stdout", "output_type": "stream", "text": ["merge.test_merge_1\\n", "multiline\\n"]}], "source": ["print(\\"merge.test_merge_1\\")\\n", "\\n", "print(\\"multiline\\")"]}]}'''
    # assert lines[0] == TEST_DATA, f"""contents loaded from master.json does not match expected\n\nexpected:\n{TEST_DATA}\n\nactual:\n{lines[0]}"""

    # # Tear Down
    os.kill(proc_teacher_server.pid, signal.CTRL_C_EVENT)
    # proc_teacher_server.terminate()
    time.sleep(5)
    os.kill(proc_student_server.pid, signal.CTRL_C_EVENT)
    # proc_student_server.terminate()
    time.sleep(5)

    os.chdir(starting_cwd)
    print("................deleting test stage...........")
    shutil.rmtree(dst)

if __name__ == "__main__":
    test_basic_1()