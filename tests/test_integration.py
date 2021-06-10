import os, sys, json, time, copy
import subprocess
import argparse
# import signal
# import shutil

'''
    run tests from tests dir:
    nbx/tests>pytest -vv [filename]

    or run:
    (venvtest1) nbx/tests/> python test_integration.py [--no-tear-down]

        --no-tear-down  :   leave directory and notebooks + servers running

'''

from modules.basic import basic_1

# Don't start these with a forward slash
TEMPLATE_DIR   = 'test_templates'
TEST_STAGE_DIR = 'test_stages'



def test_basic_1(b_no_tear_down=False):
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
            - able to send/receive without existing .nbx directory
            - the newly run answer cell is sent to student modified 

        caveats / does not test:
            - doesn't verify student with pull.rebase=true is able to receive answers;
              need to save notebook to trigger thus bug

        notes:
            - get_cell_output uses a different numbering
            - need to add double backslash ("\\") to the contents 
              of a json when inputting a literal TEST_DATA
            - if this notebook is re-opened by jupyter in templates, 
              the "id" value will change to another guid

    '''
    ERR_MSGS    = []
    TEST_FAILS  = False

    THIS_TEMPLATE_NAME   = 'init.clone.1'
    THIS_STAGE_NAME      = 'basic_1'

    if b_no_tear_down:
        print('--------------running with NO TEARDOWN ----------------')
    
    starting_cwd = os.getcwd()

    # Setup Stage Dir
    src = os.path.join(TEMPLATE_DIR,   THIS_TEMPLATE_NAME)
    dst = os.path.join(TEST_STAGE_DIR, THIS_STAGE_NAME)
    ret = subprocess.check_output(['cp', '-r', str(src), str(dst)])

    # Make Stage - git commands
    os.chdir(dst)
    ret = subprocess.check_output(["mkstage.bat"])

    # Run Separate NB Servers
    
    os.chdir("teacher")
    proc_teacher_server = subprocess.Popen([
        'jupyter',
        'notebook',
        '--port=9200', 
        '--no-browser',
        "--NotebookApp.token=''",
        "--NotebookApp.password=''"
        ],shell=True,)

    os.chdir("../student")
    proc_student_server = subprocess.Popen([
        'jupyter',
        'notebook',
        '--port=9201', 
        '--no-browser',
        "--NotebookApp.token=''",
        "--NotebookApp.password=''"
    ],shell=True,)
    
    time.sleep(10)
    print("done launching servers")

    
    # Perform Actions + In-Notebook Test Conditions
    ERR_MSGS, TEST_FAILS, d_outputs = basic_1(
        copy.copy(ERR_MSGS), 
        TEST_FAILS, 
        b_no_tear_down=b_no_tear_down,
        )

    # Test Conditions - File System / Contents 
    
    print(os.getcwd())
    
    if '.nbx' not in os.listdir('.'):
        ERR_MSGS.append("no .nbx dir created on student side")
        TEST_FAILS = True
    
    try:
        with open('.nbx/master.json', 'r') as f:
            lines = f.readlines()
    except:
        ERR_MSGS.append("not able to read from student master.json file") 
        TEST_FAILS = True
    
    if len(lines) != 1:
         ERR_MSGS.append("master.json contents has length different from 1")

    try:
        d_master = json.loads(lines[0])
        if len(d_master['cells']) != 1:
            pass
    except:
        ERR_MSGS.append("not able to transform .nbx/master.json into JSON\n{lines}")
    

    ## Tear Down
    if not(b_no_tear_down):

        print("................killing nb servers...................")
        subprocess.call(['taskkill', '/F', '/T', '/PID', str(proc_teacher_server.pid)])
        subprocess.call(['taskkill', '/F', '/T', '/PID', str(proc_student_server.pid)])
    
        time.sleep(8)
    

    ## Signal Test-Runner if this test passes
    if TEST_FAILS: 
        print("TEST_FAILS=True")
        print('\n'.join([str(e) for e in ERR_MSGS]))
    else:
        print("Tests Pass!")
    

    if not(TEST_FAILS) and not(b_no_tear_down):
    
        os.chdir(starting_cwd)
        print("................deleting test stage...........")
        subprocess.call(['rm', '-rf', str(dst)])
        print(".................done test: basic_1 ..........")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--no-tear-down',default=False, action='store_true' )
    args = parser.parse_args()
    
    test_basic_1(b_no_tear_down=args.no_tear_down)