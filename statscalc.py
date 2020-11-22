# Stats Calculator by Maria Regina Sirilan
# A data set reference list generator that utilizes stats.py, which
# contains tools for statistical calculations for numerical data
# Stats homework = EZ :^)

from stats import *

if __name__ == '__main__':
    print('-'*70)
    print('DATA SET STATS CALCULATOR')
    print('-'*70)
    unsuccessful = True
    while unsuccessful:
        values = input('Enter data set values separated by a comma: ')
        try:
            data = []
            for num in values.strip().split(','):
                num = float(num)
                if num.is_integer():
                    data.append(int(num))
                else:
                    data.append(num)
            if len(data) < 2:
                print('ERROR: You must enter at least 4 values.')
            else:
                unsuccessful = False
        except ValueError:
            print('ERROR: Use numerical values only.')
    print('-' * 70)
    round_to = 4
    print('Data set:')
    print('\t ', data)
    data_set = data[:]
    data_set.sort()
    print('Sorted data set:')
    print('\t ', data_set)
    print('Population/sample size (N/n):')
    print('\t ', len(data_set))
    print('Summation:')
    print('\t ', sum(data_set))
    print('Mean:')
    print('\t ', mean(data, round_to))
    print('Median Location:')
    print('\t ', median_loc(data))
    print('Median:')
    print('\t ', median(data))
    print('Mode:')
    print('\t ', mode(data))
    print('Distance from mean:')
    print('\t ', mean_devs(data, round_to))
    print('Mean absolute deviation:')
    print('\t ', mean_abs_dev(data, round_to))
    print('Squared distance from mean:')
    print('\t ', squared_dist(data, round_to))
    print('Sample variance:')
    print('\t ', variance(data, round_to))
    print('Sample standard deviation:')
    print('\t ', stdev(data, round_to))
    print('Population variance:')
    print('\t ', pvariance(data, round_to))
    print('Population standard deviation:')
    print('\t ', pstdev(data, round_to))
    print('Range:')
    print('\t ', round(max(data) - min(data), round_to))
    print('Quartile location (index):')
    print('\t ', quartile_index(data))
    qts = quartiles(data)
    print('1st quartile (Q1):')
    print('\t ', qts[0])
    print('3rd quartile (Q3):')
    print('\t ', qts[1])
    print('Interquartile range (Q3 - Q1):')
    print('\t ', iqr(data))
    print('Lower fence:')
    print('\t ', lower_fence(data_set))
    print('Upper fence:')
    print('\t ', upper_fence(data_set))
    wks = whiskers(data_set)
    print('[Box-and-Whisker] Lower whisker extends to:')
    print('\t ', wks[0])
    print('[Box-and-Whisker] Upper whisker extends to:')
    print('\t ', wks[1])
    print('[Box-and-Whisker] Outliers:')
    outs = outliers(data_set)
    print('\t ', outs)
    print('[Box-and-Whisker] Box plot:')
    low_o = outs[0]
    upper_o = outs[1]
    inner = [num for num in data_set if num not in low_o + upper_o]
    print('\t ', str(low_o) + ' | ' + str(inner) + ' | ' + str(upper_o))
