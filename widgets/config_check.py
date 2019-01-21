'''The script checks existence and versions of required modules.''' 

import warnings
import sys

msg_old = 'Your current version of %s (%s) is older then the one used in tests (%s). It is recommended to uprgade it.'
msg_no = 'No %s module is found.'

python_version = '3.6.4'
if sys.version.split('.') < python_version.split('.'):
    warnings.warn(str(msg_old % ('python', sys.version, python_version)), stacklevel=100)

def check_version(module_name, module_version):    
    try:
        exec('import ' + module_name)
        current_version = eval(module_name + '.__version__')
        if current_version.split('.') < module_version.split('.'):
            warnings.warn(str(msg_old % (module_name, current_version, module_version)), stacklevel=100)
    except:
        warnings.warn(str(msg_no % module_name), stacklevel=100)
        
def check_existence(module_name):    
    try:
        exec('import ' + module_name)
    except:
        warnings.warn(str(msg_no % module_name), stacklevel=100)

modules_vers = {'numpy' : '1.14.0', 
                'scipy' : '1.0.0', 
                'matplotlib' : '2.1.2', 
                'pystan' : '2.17.1.0', 
                'ipywidgets' : '7.2.1',
                'bqplot' : '0.11',
                'IPython' : '6.3.1',
                'torch' : '0.4.1'}
modules_exist = ['jupyter_cms']

for key, value in modules_vers.items():
    check_version(key, value)

for module in modules_exist:
    check_existence(module)