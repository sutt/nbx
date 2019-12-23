import subprocess

try:
    from IPython.display import Javascript
    from IPython.display import display
except:
    print('unable to import from `IPython` package, this extension will note work')
    raise ImportError()

# Documentation + Tips ---------------
'''
# getting notebooks in <root>/misc/book to import <root>/cpr
import sys
sys.path.append('../../')
from IPython import display
from IPython.display import Javascript
%reload_ext autoreload
%autoreload 2
import cpr.cpr as cpr

'''
# Demo Functions ----------------------

def demo_js():
    ''' 
         demo_js uses `display.display()` to execute a Javascript payload
    '''
    
    print('see devtools console for output')
    display(
        Javascript(data='console.log("demo_js");')
    )
    
def demo_js_to_python():
    ''' 
         demo_js uses a trick to get data in js into the python kernel
    '''
    
    js = '''
    Ipython.notebook.kernel.execute("a=1");
    Ipython.notebook.kernel.execute("print(f'the value of `a` is : {a}`");
    '''

    js = '\n'.join([line.strip() for line in js.split('\n') if line.strip !=''])
    
    display(Javascript(data=js))
    

# Basic Functionality ------------------

def reload_nb(b_save=False):
    '''
         realod the noetbook thru javascript
         b_save: if True, saves notebook before reload

         note: we'll probably want to save in a separate function, 
               before the git add/commit/pull.
    '''
        
    if b_save:
        print('b_save NotImplemented')

    # js = '''
    # var nb_path = IPython.notebook.notebook_path;
    # var mycell = IPython.notebook.get_selected_cell();
    # var mycellelement = $(mycell.element);
    # IPython.notebook.load_notebook(nb_path);
    # mycellelement[0].scrollIntoViewIfNeeded({inline:'center'});
    # '''

    js = '''
    var nb_path = IPython.notebook.notebook_path;
    var mycell_index = IPython.notebook.get_selected_index();
    IPython.notebook.load_notebook(nb_path);
    console.log('after load')
    setTimeout(basicFunc, 500);
    function basicFunc() {
        console.log('in basicFunc');   
        var orig_cell = IPython.notebook.get_cell(mycell_index);
        $(orig_cell.element)[0].scrollIntoViewIfNeeded({inline:'center'});
        console.log('final line.')
    }
    console.log('done')
    '''
    
    # js = '''
    # console.log('begin')
    # function basicFunc() {
    #     console.log('in basicFunc');
    # }
    # setTimeout(basicFunc, 3000);
    # console.log('done')
    # '''
    
    js = '\n'.join([line.strip() for line in js.split('\n') if line.strip !=''])

    display.display(Javascript(js))
    