import os, sys, time

from .merge import get_answer
from .merge import give_answer

from .cpr import reload_nb

from .gitcomm import pull_answer
from .gitcomm import push_answer


def receive_answer( fn_nb, 
                    remote_name='local',
                    b_log=False, 
                    b_replace=False,
                    b_save=False
                    ):
    
    pull_answer(remote_name=remote_name, 
                b_log=b_log,
                )
    
    get_answer( fn_nb, 
                term='receive_answer',
                b_replace=b_replace,
                )
    
    reload_nb(  b_save=b_save, 
                b_scroll=True,
                b_flash=True,
                b_select=True,
                b_log=False,
                debug=False,
                )
    


def send_answer(fn_nb, 
                remote_name='local',
                b_log=False,
                ):
    
    give_answer(fn_nb, 
                term='send_answer',
                )
    
    push_answer(remote_name=remote_name, 
                b_log=b_log,
                )
    
    print('done.')