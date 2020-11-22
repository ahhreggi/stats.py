# Stats Module by Maria Regina Sirilan
# Contains tools for statistical calculations for numerical data
# A supplement to the built-in statistics library


class StatsEmptyError(Exception):
    """An exception to be raised when data is empty."""


class StatsDataError(Exception):
    """An exception to be raised when a data value is invalid."""


def mode(data):
    """(list) -> list
    Return a list of items with the highest number of occurrences in data.
    Raises an error if data is empty.
    """
    try:
        temp = set(data)
        freq = {}
        for num in temp:
            freq[num] = data.count(num)
        mode_freq = max(freq.values())
        return [num for num in temp if data.count(num) == mode_freq]
    except (ZeroDivisionError, ValueError):
        raise StatsEmptyError('mode requires at least one item')


def multimodal(data):
    """(list of ints or floats) -> list of ints or floats
    Return True if the data contains more than 1 mode.
    Raises an error if data is empty.
    """
    try:
        return len(mode(data)) > 1
    except (ZeroDivisionError, ValueError, StatsEmptyError):
        raise StatsEmptyError('multimodal requires at least one item')


def mean(data, round_to=4):
    """(list of ints or floats[, int]) -> float
    Return the sample arithmetic mean of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        return round(sum(data) / len(data), round_to)
    except ZeroDivisionError:
        raise StatsEmptyError('mean requires at least one data point')
    except TypeError:
        raise StatsDataError('mean expects numerical values')


def mean_devs(data, round_to=4):
    """(list of ints or floats[, int]) -> list of floats
    Return a list of the mean deviations of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        dev = []
        avg = mean(data)
        for num in data:
            dev.append(round(abs(avg - num), round_to))
        return dev
    except (ZeroDivisionError, StatsEmptyError):
        raise StatsEmptyError('mean_devs requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('mean_devs expects numerical values')


def mean_abs_dev(data, round_to=4):
    """(list of ints or floats[, int]) -> float
    Return the mean absolute deviation of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        return round(sum(mean_devs(data)) / len(data), round_to)
    except (ZeroDivisionError, StatsEmptyError):
        raise StatsEmptyError(
            'mean_abs_devs requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('mean_abs_devs expects numerical values')


def squared_dist(data, round_to=4):
    """(list of ints or floats[, int]) -> float
    Return a list of squared distances from the mean of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        var_sq = []
        avg = mean(data)
        for num in data:
            var_sq.append(round((num - avg) ** 2, round_to))
        return var_sq
    except (ZeroDivisionError, StatsEmptyError):
        raise StatsEmptyError('squared_dist requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('squared_dist expects numerical values')


def variance(data, round_to=4):
    """(list of ints or floats[, int]) -> float
    Return the sample variance of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        return round(sum(squared_dist(data)) / (len(data) - 1), round_to)
    except (ZeroDivisionError, StatsEmptyError):
        raise StatsEmptyError('variance requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('variance expects numerical values')


def stdev(data, round_to=4):
    """(list of ints or floats[, int]) -> float
    Return the sample standard deviation of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        return round(variance(data) ** 0.5, round_to)
    except (ZeroDivisionError, StatsEmptyError):
        raise StatsEmptyError('stdev requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('stdev expects numerical values')


def pvariance(data, round_to=4):
    """(list of ints or floats[, int]) -> float
    Return the population variance of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        return round(sum(squared_dist(data)) / len(data), round_to)
    except (ZeroDivisionError, StatsEmptyError):
        raise StatsEmptyError('pvariance requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('pvariance expects numerical values')


def pstdev(data, round_to=4):
    """(list of ints or floats[, int]) -> float
    Return the population standard deviation of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        return round(pvariance(data) ** 0.5, round_to)
    except (ZeroDivisionError, StatsEmptyError):
        raise StatsEmptyError('pstdev requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('pstdev expects numerical values')


def median_loc(data):
    """(list of ints or floats) -> float
    Return the float location of the median of data.
    Note: This location is applicable to data when sorted in ascending order.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        length = len(data)
        if length < 1:
            raise IndexError
        return float(length) / 2 - 0.5
    except (ZeroDivisionError, IndexError):
        raise StatsEmptyError('median_loc requires at least one data point')
    except TypeError:
        raise StatsDataError('median_loc expects numerical values')


def median(data):
    """(list of ints or floats) -> int or float
    Return the median of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        data_copy = data[:]
        data_copy.sort()
        index = median_loc(data_copy)
        if len(data_copy) % 2 == 1:
            med = data_copy[int(index)]
        else:
            med = (data_copy[int(index) - 1] + data_copy[int(index) - 2]) / 2
        return med
    except (ZeroDivisionError, IndexError, StatsEmptyError):
        raise StatsEmptyError('median requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('median expects numerical values')


def quartile_index(data):
    """(list of ints or floats) -> float
    Return the float quartile location of data.
    Note: This location is applicable to data when sorted in ascending order.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        return (median_loc(data) + 1.5) / 2
    except (ZeroDivisionError, IndexError, StatsEmptyError):
        raise StatsEmptyError(
            'quartile_index requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('quartile_index expects numerical values')


def quartiles(data):
    """(list of ints or floats) -> tuple of floats
    Return a tuple containing the 1st and 3rd quartiles.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        data_copy = data[:]
        data_copy.sort()
        loc = quartile_index(data_copy)
        if (loc % 2 == 1) or (loc % 2 == 0):
            loc = int(loc)
            q1 = data_copy[loc - 1]
            q3 = data_copy[0 - loc]
        else:
            q_floor = round(loc - 0.4999999999) - 1
            q_ceil = round(loc + 0.4999999999) - 1
            q1 = (data_copy[q_floor] + data_copy[q_ceil]) / 2
            q_floor2 = 0 - q_floor - 1
            q_ceil2 = 0 - q_ceil - 1
            q3 = (data_copy[q_floor2] + data_copy[q_ceil2]) / 2
        return q1, q3
    except (ZeroDivisionError, IndexError, StatsEmptyError):
        raise StatsEmptyError('quartiles requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('quartiles expects numerical values')


def iqr(data):
    """(list of ints or floats) -> float
    Return the interquartile range of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        q = quartiles(data)
        return q[1] - q[0]
    except (ZeroDivisionError, IndexError, StatsEmptyError):
        raise StatsEmptyError('iqr requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('iqr expects numerical values')


def lower_fence(data):
    """(list of ints or floats) -> float
    Return the lower fence of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        return quartiles(data)[0] - (1.5 * iqr(data))
    except (ZeroDivisionError, IndexError, StatsEmptyError):
        raise StatsEmptyError('lower_fence requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('lower_fence expects numerical values')


def upper_fence(data):
    """(list of ints or floats) -> float
    Return the upper fence of data.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        return quartiles(data)[1] + (1.5 * iqr(data))
    except (ZeroDivisionError, IndexError, StatsEmptyError):
        raise StatsEmptyError('upper_fence requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('upper_fence expects numerical values')


def outliers(data):
    """(list of ints or floats) -> [list of ints or floats]
    Return a nested list containing the lower and upper outliers.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        lower = lower_fence(data)
        upper = upper_fence(data)
        lower_o, upper_o = [], []
        if lower != upper:
            lower_o = [num for num in data if num <= lower]
            upper_o = [num for num in data if num >= upper]
        return [lower_o, upper_o]
    except (ZeroDivisionError, IndexError, StatsEmptyError):
        raise StatsEmptyError('outliers requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('outliers expects numerical values')


def whiskers(data):
    """(list of ints or floats) -> float
    Return a list containing the lower and upper whiskers of a box
    and whiskers box plot.
    Raises an error if data is empty or contains non-numerical values.
    """
    try:
        lower = lower_fence(data)
        upper = upper_fence(data)
        result = data[:]
        outliers = []
        wsk = []
        for num in result:
            if num >= upper or num <= lower:
                result.remove(num)
                outliers.append(num)
        if result:
            wsk = min(result), max(result)
        return wsk
    except (ZeroDivisionError, IndexError, StatsEmptyError):
        raise StatsEmptyError('whiskers requires at least one data point')
    except (TypeError, StatsDataError):
        raise StatsDataError('whiskers expects numerical values')
