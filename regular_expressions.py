import re

# Регулярные выражения для почтовых индексов
postcode_regex = r'^\w{1,} .{1,}$'
ru_postcode_regex = r'^ru \d{6}$'
usa_postcode_regex = r'^usa \d{5}$'
uk_postcode_regex = r'^uk [A-Z]{1,2}\d[A-Z\d]? \d[A-Z]{2}$'
french_postcode_regex = r'^french \d{5}$'

# Функция получения региона 
def get_region(postcode):
    res = ''
    i = 0
    while i < len(postcode) and postcode[i] != ' ':
        res += postcode[i]
        i += 1
    return res

# Основная функция
def is_valid_postcode(postcode):
    # Сначала проверяем, что строка не пустая
    if len(postcode) == 0:
        return False
    
    region = get_region(postcode)

    # Проверяем соответствие общему шаблону
    if re.match(postcode_regex, postcode) is None:
        return False

    # Проверяем регулярное выражение в зависимости от региона
    if region == 'ru':
        return re.match(ru_postcode_regex, postcode) is not None
    elif region == 'usa':
        return re.match(usa_postcode_regex, postcode) is not None
    elif region == 'uk':
        return re.match(uk_postcode_regex, postcode) is not None
    elif region == 'french':
        return re.match(french_postcode_regex, postcode) is not None
    else:
        return False