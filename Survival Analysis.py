# Importing the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.datasets import load_rossi

# Loading the Rossi dataset from lifelines
data = load_rossi()

# Creating a Kaplan-Meier estimator and fitting the data
kmf = KaplanMeierFitter()
kmf.fit(data['week'], event_observed=data['arrest'])

# Plotting the Kaplan-Meier curve
kmf.plot_survival_function()
plt.xlabel('Weeks')
plt.ylabel('Survival Probability')
plt.title('Kaplan-Meier Survival Curve')

# Displaying the plot
plt.show()
