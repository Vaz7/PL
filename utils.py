import datetime
import re
import json


def validate_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            json.load(file)
        print("The JSON file is valid.")
    except (ValueError, FileNotFoundError) as e:
        print("The JSON file is not valid:", str(e))

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
    for key, value in dict2.items():
        if key in dict1:
            if isinstance(value, dict) and isinstance(dict1[key], dict):
                dict1[key] = merge_dicts(dict1[key], value)
            elif isinstance(value, set) and isinstance(dict1[key], set):
                dict1[key] |= value
            else:
                dict1[key] = value
        else:
            dict1[key] = value
    return dict1

def is_array_table(value):
    for elem in value:
        if isinstance(elem, dict):
            return True
            
    return False

def merge_elems(dict1, dict2):
    #print(dict1)
    #print(dict2)
    #print('*'*50)
    for key, value in dict2.items():
        if key in dict1:
            #check both types
            if isinstance(value, list) and is_array_table(value) and isinstance(dict1[key], list) and is_array_table(dict1[key]):
                dict1 = join_toml_array_tables(dict1, {key : value})
            elif isinstance(value, dict) and isinstance(dict1[key], list) and is_array_table(dict1[key]):
                print("aqui")
                print(dict1[key])
                print(value)
                print('-'*40)
                dict1[key][-1] = join_toml_array_tables(dict1[key][-1], value)
                print(dict1[key])
            elif isinstance(value, dict) and isinstance(dict1[key], dict):
                dict1[key] = merge_dicts(dict1[key], value)
                pass
            elif isinstance(value, set) and isinstance(dict1[key], set):
                dict1[key] |= value
            else:
                dict1[key] = value
        else:
            dict1[key] = value

    return dict1

def build_dict(keys, value):
    temp = keys.split('.')
    result = dict()

    for elem in temp:
        if elem != temp[-1]:
            add_to_dict_chain(result, elem, {})
        else:
            add_to_dict_chain(result, elem, value)

    return result

def add_to_dict_chain(d, key, value):
    while list(d.values()) != [] and isinstance(list(d.values())[-1], dict):
        d = list(d.values())[-1]
    d[key] = value

def add_to_array_chain(d, key, value):
    while list(d.values()) != [] and isinstance(list(d.values())[-1][-1], dict):
        d = list(d.values())[-1][-1]
    d[key] = value

def get_key_index(key, d):
    index = 0;
    
    for elem in d:
        if key in elem.keys():
            return index

        index += 1
    
    return -1

def join_array_tables(dict1, dict2):
    
    for key in dict2.keys():
        if isinstance(dict1, dict) and key in dict1.keys():
            if len(dict2[key]) == 1 and dict2[key][0] != {} and isinstance(list(dict2[key][0].values())[-1], list):
                dict1[key] = join_array_tables(dict1[key], dict2[key][0])
            else:
                dict1[key] = dict1[key] + dict2[key] # TODO: Rever esta parte e olhar para o último exemplo do parser file (ver documentação do toml agane)
        elif isinstance(dict1, dict):
            dict1[key] = dict2[key]
        else:
            index = get_key_index(key, dict1)
            if index < 0:
                if isinstance(dict2[key], list):
                    dict1[-1][key] = dict2[key]
                else:
                    dict1.append(dict2) 
            else:
                if isinstance(dict2[key], list):
                    dict1[index][key] = join_array_tables(dict1[index][key], dict2[key][0])
                else:
                    dict1.append(dict2)

    return dict1

# TODO: Rever esta função para o exemplo da wakanda
def join_toml_array_tables(dict1, dict2):
    for key in dict2.keys():
        if key in dict1.keys():
            if len(dict2[key]) == 1 and isinstance(dict2[key], list) and dict2[key][0] != {} and isinstance(list(dict2[key][0].values())[-1], list):
                if isinstance(dict1[key], list):
                    dict1[key][-1] = join_toml_array_tables(dict1[key][-1], dict2[key][0])
                else:
                    dict1[key] = join_toml_array_tables(dict1[key], dict2[key][0])
            else:
                if isinstance(dict2[key], list):
                    dict1[key].append(dict2[key][0])
                elif isinstance(dict1[key], list):
                    dict1[key][-1].update(dict2[key])
                else:
                    dict1[key].update(dict2[key])
        else:
            dict1[key] = dict2[key]

    return dict1