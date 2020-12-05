import re


REQUIRED_KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def validate_value(key, items):
    val = items[key]
    if key == 'byr':
        try:
            return int(val) >= 1920 and int(val) <= 2002
        except Exception:
            return False
    elif key == 'iyr':
        try:
            return int(val) >= 2010 and int(val) <= 2020
        except Exception:
            return False
    elif key == 'eyr':
        try:
            return int(val) >= 2020 and int(val) <= 2030
        except Exception:
            return False
    elif key == 'hgt':
        if 'cm' in val:
            num = val.split('cm')[0]
            try:
                return int(num) >= 150 and int(num) <= 193
            except Exception:
                return False
        elif 'in' in val:
            num = val.split('in')[0]
            try:
                return int(num) >= 59 and int(num) <= 76
            except Exception:
                return False
        else:
            return False
    elif key == 'hcl':
        if len(val) != 7:
            return False
        result = re.search("#\w{6}", val)
        if result is None:
            return False
    elif key == 'ecl':
        if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
    elif key == 'pid':
        if len(val) != 9:
            return False
        result = re.search("\d{9}", val)
        if result is None:
            return False

    return True


def is_valid_passport(passport):
    is_valid = True
    items = extract_items_from_passport(passport)
    for required_key in REQUIRED_KEYS:
        if required_key not in items.keys():
            is_valid = False
            break
        if validate_value(required_key, items) is False:
            is_valid = False
            break
    return is_valid


def extract_items_from_passport(passport):
    passport = passport.replace('\n', " ")
    elements = passport.split(' ')
    items = {}
    for elt in elements:
        parts = elt.split(':')
        if len(parts) < 2:
            continue
        items[parts[0]] = parts[1]
    return items


def solution(passports):
    valid_count = 0
    for passport in passports:
        if is_valid_passport(passport):
            valid_count += 1

    return valid_count


if __name__ == '__main__':
    with open('inputs/day4.txt', 'r') as f:
        data = f.read()
        split_data = data.split('\n\n')
        passports = [x for x in split_data if x]

    print(f"Found {solution(passports)} valid passports out of {len(passports)}")
