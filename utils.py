import datetime
import re

def validDate(date):
    date_splitted = date.split('-')
    try:
        year  = int(date_splitted[0])
        month = int(date_splitted[1])
        day   = int(date_splitted[2])
    except ValueError:
        return False  # could not convert parts to integers, invalid format
    # check if year, month, and day are within valid ranges
    if year < 1 or month < 1 or month > 12 or day < 1 or day > 31:
        return False  # invalid values for year, month, or day
    # check for valid number of days for the given month and year
    if month in [4, 6, 9, 11] and day > 30:
        return False  # April, June, September, and November have 30 days
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return False  # leap year has 29 days in February
        else:
            if day > 28:
                return False  # non-leap year has 28 days in February
    return True  # valid date


def validDateTime(datetime_str):
    try:
        # split datetime string into its components
        date_str, time_str = datetime_str.split('T')
        year_str, month_str, day_str = date_str.split('-')

        offset = re.split(r'\+|-|z|Z', time_str)

        if len(offset) == 3: # checks whether or not the given datetime has both (+|-)HH::MM and z|Z offsets
            return False

        hour_str, minute_str, second_str = offset[0].split(':')
        second_parts = second_str.split('.')
        second_int = int(second_parts[0])
        microsecond_int = int(second_parts[1]) if len(second_parts) > 1 else 0

        if len(offset) == 2 and offset[1] != '':
            offset_hour, offset_min = offset[1].split(':')
            offset_hour = int(offset_hour)
            offset_min = int(offset_min)

            if offset_hour < 0 or offset_hour > 23 or offset_min < 0 or offset_min > 59:
                return False

        # parse date and time components into datetime object
        dt = datetime.datetime(
            year=int(year_str), month=int(month_str), day=int(day_str),
            hour=int(hour_str), minute=int(minute_str), second=second_int,
            microsecond=microsecond_int
        )

        return True  # valid datetime

    except (ValueError, IndexError):
        return False  # invalid datetime format

def validTime(time):
    time_splitted = re.split(r'\+|-|z|Z', time)

    if len(time_splitted) == 3:
        return False
    try:
        if len(time_splitted) == 2 and time_splitted[1] != '':
            offset_hour, offset_min = time_splitted[1].split(':')

            offset_hour = int(offset_hour)
            offset_min = int(offset_min)

            if offset_hour < 0 or offset_hour > 23 or offset_min < 0 or offset_min > 59:
                return False


        time_splitted = time_splitted[0].split('.')
        datetime.datetime.strptime(time_splitted[0], "%H:%M:%S")
    
    except (ValueError, IndexError):
        return False

    return True

def validKey(str):
    str_splitted = str.split('.')

    for split in str_splitted:
        if split[:2] == '\\\"':
            return False

    return  True

def set_up_multiline_string(str):
    lines = str.split('\n')
    if len(lines) == 1:
        return str
    else:
        backslash = False
        result = ""
        
        for line in lines:

            if backslash:
                line = line.lstrip()

            if line != '' and line[-1] == '\\':
                line = line[:-1]
                backslash = True
            else:
                if line != '':
                    line = line + '\n'
                    backslash = False

            result = result + line

        if result[-1] == '\n':
            result = result[:-1]

        return result

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            if isinstance(value, dict) and isinstance(result[key], dict):
                result[key] = merge_dicts(result[key], value)
            elif isinstance(value, set) and isinstance(result[key], set):
                result[key] |= value
            else:
                result[key] = value
        else:
            result[key] = value
    return result

def add_to_dict_chain(d, key, value):
    while list(d.values()) != [] and isinstance(list(d.values())[-1], dict):
        d = list(d.values())[-1]
    d[key] = value
