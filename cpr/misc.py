import subprocess

try:
    from IPython.display import Javascript
    from IPython.display import display
except:
    print('unable to import from `IPython` package, this extension will not work')
    raise ImportError()

'''
TODOs

[ ] some git subprocess commands


'''

# JS Functionality ----------------------

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
         a trick to get data in js into the python kernel the notebook
         is connected to
    '''
    
    js = '''
    IPython.notebook.kernel.execute("a=1");
    IPython.notebook.kernel.execute("print(f'the value of `a` is : {a}`");
    '''

    js = '\n'.join([line.strip() for line in js.split('\n') if line.strip !=''])
    
    display(Javascript(data=js))
    