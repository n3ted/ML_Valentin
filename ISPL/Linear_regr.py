import numpy as np
import pandas as pd
from matplotlib.pyplot import subplots 
import statsmodels.api as sm
from statsmodels.stats.outliers_influence \
    import variance_inflation_factor as  vif
from statsmodels.stats.anova import anova_lm
from ISLP import load_data
from ISLP.models import (ModelSpec as ms, 
                         summarize, poly)
# Inspecting objects and Namespace
dir()



