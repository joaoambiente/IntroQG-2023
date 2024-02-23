"""Functions used in the Introduction to Quantitative Geology course"""

# Import any modules needed in your functions here
import math
import numpy as np

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

def gaussian(gauss_mean, gauss_stddev, gauss_x_array):
    """ Generates the normal distribution's probabilities of 
    "gauss_x_array" values based on the gaussian equation and 
    on the provided mean (gauss_mean) and standard deviation (gauss_stddev)
    of the values in the array """
    gauss_x_array = np.array(gauss_x_array)
    
    dividend = np.exp(-( (gauss_x_array - gauss_mean)**2 / (2 * gauss_stddev**2)))
    divisor = gauss_stddev * np.sqrt( 2 * np.pi)
    gaussian = dividend / divisor          
    return np.round(gaussian, 4)

def linregress(x, y):
    """Calculates the y-intercept "A" and slope "B" for the best-fit line to the input data (x, y)"""
    sum_x = np.sum(x)
    sum_x_squared = np.sum(np.square(x))
    sum_y = np.sum(y)
    sum_xy = np.sum(np.multiply(x, y))
    
    N = len(x)
    
    alpha = N * (sum_x_squared) - (sum_x)**2
    
    A = ((sum_x_squared * sum_y) - (sum_x * sum_xy)) / alpha
    B = ( N * sum_xy - (sum_x * sum_y)) / alpha
    
    return A, B

def pearson(x, y):
    """Returns the correlation coefficient between two variables: x and y"""
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    dividend_sum = np.sum( (x - mean_x) * (y - mean_y) )
    divisor_sum = np.sqrt( np.sum( (x - mean_x)**2 ) * np.sum( (y - mean_y)**2 ) )
    r = dividend_sum / divisor_sum
    
    return r 


def chi_squared(observations, expected_values, standard_deviation):
    """
    Reduced chi-squared equation
    Calculates how much the expected values fall within the range of observations 
    """
    variance = standard_deviation**2
    dividend = np.sum( (observations - expected_values)**2 / variance ) 
    nr_observations = len(observations)
    chi_squared = dividend / nr_observations

    return chi_squared


