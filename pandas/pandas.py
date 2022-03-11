# Task 1
import pandas as pd # import pandas
train_data = pd.read_csv('train.csv') # read the data
train_data.head() # view the data structure
hist_data = train_data[['pos', 'A', 'C', 'T', 'G']] # chose the required columns
hist_data = hist_data.fillna(0) # replace NaN with 0
hist_data.plot.bar(x = 'pos', figsize = [15, 10], stacked = True, xlabel = 'Position') # plotting

# Task 2
train_part = train_data[train_data['matches'] > train_data['matches'].mean()][['pos', 'reads_all', 'mismatches', 'deletions', 'insertions']] # chose the data
train_part.to_csv('train_part.csv') # create csv output

# Task 3
from pydataset import data 
iris_data = data('iris') # importing the dataset
iris_data.info() # view the key info about the data

iris_data.head() # view structure

iris_data.describe() # the key statistics

corr = iris_data.corr()
corr.style.background_gradient() # correlation plot

iris_data.plot.kde(figsize = [15, 10]) # look at destributions

iris_data.groupby('Species').plot(kind='kde') # destributions by species

iris_data.boxplot(figsize = [15, 10], by = 'Species')