import sys

sys.path.append('../')

from nbx import gitcomm

def test_cmd_line_strip_1():
    '''
         cmd_line_strip()
    '''

    # simple
    cmd = '''
    line1
    line2
    '''

    cmd = gitcomm.cmd_line_strip(cmd)

    assert len(cmd) == 2

    # multiple blank lines
    cmd = '''

        \n
    '''

    cmd = gitcomm.cmd_line_strip(cmd)

    assert len(cmd) == 0

    # multiple blank lines
    cmd = '''

        some line
    '''

    cmd = gitcomm.cmd_line_strip(cmd)

    assert len(cmd) == 1
    assert cmd == ['some line']



