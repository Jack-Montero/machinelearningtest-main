# summarize the data
from pandas import read_csv 
import json

# Load dataset
url = 'C://Users/pyros/OneDrive//Documents//Coding shit//machinelearningtest-main//herostats.csv'
names = ['gold', 'performance', 'damage delt', 'damage taken', 'length']
dataset = read_csv(url, names=names)
     
# shape
print(dataset.shape)
# head
print(dataset.head(20))
# descriptions
print(dataset.describe())
# class distribution
print(dataset.groupby('length').size())
