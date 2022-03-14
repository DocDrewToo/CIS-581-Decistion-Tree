import inspect

def im_here():
    current_method = inspect.stack()[0][3]
    return current_method
im_here()