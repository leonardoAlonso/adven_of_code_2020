def get_passports(_file: str) -> list:
    formated_input = []
    passports = []
    with open(_file, 'r') as reader:
        lines = reader.readlines()
        splited = []
        for line in lines:
            _line = list(line)
            if len(_line) == 1:
                passports.append(splited)
                splited = []
                continue
            splited.append(line)
    return passports

def format_passports(passports: list) -> list:
    formated_passports = []
    for passport in passports:
        passport_object = {}
        for line in passport:
            no_space = line.split(' ')
            splited = list(map(lambda l: l.split(':'), no_space))
            for element in splited:
                if '\n' in element[1]:
                    element[1] = element[1][:-2]
                passport_object.update({element[0]: element[1]})
        formated_passports.append(passport_object)
    return formated_passports

def validate_passports_part_one(passports: list) -> int:
    valid = 0
    for passport in passports:
        if len(passport) == 8 or set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']).issubset(passport.keys()):
            valid += 1
    return valid

passports = get_passports('./day_four.txt')
formated_passports = format_passports(passports)
print(validate_passports_part_one(formated_passports))