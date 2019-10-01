#!/usr/bin/env python
# coding: utf-8

# # Importing Modules
# 
# This lesson covers:
# 
# * Module import

# ## Problem: Importing Modules
# 
# Python is a general-purpose programming language and is not specialized for
# numerical or statistical computation. The core modules that enable Python to store
# and access data efficiently and that provide statistical algorithms are
# located in modules.  The most important are:
# 
# * NumPy (`numpy`) - provide the basic array block used throughout numerical
#   Python
# * pandas (`pandas`) - provides DataFrames which are used to store 
#   data in an easy-to-use format
# * SciPy (`scipy`) - Basic statistics and random number generators. The most
#   important submodule is `scipy.stats`
# * matplotlib (`matplotlib`) - graphics. The most important submodule is
#   `matplotlib.pyplot`.
# * statsmodels (`statsmodels`) - statistical models such as OLS. The most
#   important submodules are `statsmodels.api` and `statsmodels.tsa.api`.
# 
# Begin by importing the important modules.




# ## Problem: Canonical Names
# 
# Use the `as` keyword to import the modules using their canonical names:
# 
# | Module              | Canonical Name |
# | :------------------ | :------------- |
# | numpy               | np             |
# | pandas              | pd             |
# | scipy               | sp             |
# | scipy.stats         | stats          |
# | matplotlib.pyplot   | plt            |
# | statsmodels.api     | sm             |
# | statsmodels.tsa.api | tsa            |
# 
# Import the core modules using `import` _module_ `as` _canonical_.




# ## Problem: Importing individual functions
# 
# 1. Import `array`, `sqrt`, `log` and `exp` from NumPy.
# 2. Import `OLS` from `statsmodels.regression.linear_model`
# 3. Import the `stats` module from `scipy`



