'''
# We can directly import needed functions from cla

try:
    from cla.metrics import grid_search_svm_hyperparams, plot_svm_boundary, \
        plot_lr_boundary
except Exception as e:
    print(e)
    print('Please try: pip install cla==1.0.2 or above')

'''

import cla
assert( '__version__' in cla.__dict__ and cla.__version__ >= '1.1.7')