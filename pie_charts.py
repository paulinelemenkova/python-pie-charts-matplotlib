#!/usr/bin/env python
# coding: utf-8
"""Pie Charts with Python and Matplotlib

Author:  Polina Lemenkova
ORCID:   https://orcid.org/0000-0002-5759-1089
Archive: https://doi.org/10.13140/RG.2.2.33869.69606
License: MIT

See README.md for details.
"""
import os

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

os.chdir(os.path.dirname(os.path.abspath(__file__)))
dfM = pd.read_csv("Tab-Morph.csv")

# dataset
df = pd.DataFrame({'Pacific Plate': dfM.plate_pacif,
                  'Philippine Plate': dfM.plate_phill,
                   'Mariana Plate': dfM.plate_maria,
                   'Caroline Plate': dfM.plate_carol},
                  index=dfM.profile)

# plot chart
df.plot(kind='pie', subplots=True, figsize=(10, 10),
        legend=False, table=False,
        fontsize=8, sort_columns=True,
        layout=(2, 2), colormap='tab20b',
        title='Mariana Trench: Pie charts for the \nsample points distribution by tectonic plates',
        )

# visualize and save
plt.tight_layout()
plt.savefig('plot_Pie.png', dpi=300)
plt.show()
