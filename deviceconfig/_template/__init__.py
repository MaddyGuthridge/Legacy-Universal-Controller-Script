"""device > _template > __init__.py

This script is responsible for redirecting relevant function calls in order to
allow the script to communicate with a particular type of device
"""

def initialise():
    """Loads the setup file to register the controller's commands
    """
    
    from . import autoinit

