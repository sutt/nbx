import subprocess

b_IPython_loaded = False
try:
    from IPython.display import Javascript
    from IPython import display
    b_IPython_loaded = True
except:
    print('unable to import from `IPython` package')

def hello():
    print('hello world')

def was_loaded():
    return b_IPython_loaded


def demo_js():
    '''demo_js uses `display.display()` to execute a Javascript payload'''
    
    print('see devtools console for output')
    display.display(
        Javascript(data='console.log("demo_js");')
    )
    
    # try this later: using the lib argument
    # Javascript(data='console.log("mama");', lib='/static/notebook/js/main.js')
    # )

def demo_js2():
    ''' demo_js2 uses return to jupyter notebook to execute a Javascript payload
        therefore it will only work when called from jupyter.
    '''
    print('see devtools console for output')
    
    return Javascript(data='console.log("demo_js2");')

