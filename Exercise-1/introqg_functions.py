"""Functions used in the Introduction to Quantitative Geology course"""

# Import any modules needed in your functions here
import math

# Define your new functions below

def mean(sample_list):
    """
    Calculates the sample mean of sample results contained on a given "sample_list".
    "sample_result" is each value to be included in the mean calculation
    "total_nr_samples" is the total number of values to average
    """
    sample_sum = 0
    total_nr_samples = len(sample_list)
    for sample_result in sample_list:
        sample_sum += sample_result
    sample_mean = sample_sum / total_nr_samples
    
    return sample_mean 


def stddev(sample_list):
    """
    Calculates the standard deviation of sample results contained on a given "sample_list".
    "sample_result" is each value to be included in the standard_dev calculation
    "total_nr_samples" is the total number of values to average
    "squared_sample_dif_sum" is the squared difference of each sample relative to the mean
    """
    sample_sum = 0
    total_nr_samples = len(sample_list)
    sample_mean = mean(sample_list)
    squared_sample_dif_sum = 0
    
    for sample_result in sample_list:
        squared_sample_dif_sum += (sample_result - sample_mean)**2
        
    standard_dev = math.sqrt(squared_sample_dif_sum / total_nr_samples)
        
    return standard_dev

def stderr(sample_list):
    """
    Calculates the standard error of sample results contained on a given "sample_list".
    "total_nr_samples" is the total number of values to average
    "standard_deviation" is standard deviation for all the values in the sample list
    """
    total_nr_samples = len(sample_list)
    standard_deviation = stddev(sample_list)
    
    standard_error = standard_deviation / math.sqrt(total_nr_samples)
    
    return standard_error