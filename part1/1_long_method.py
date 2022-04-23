# В задании представлена одна большая функция...
# Делает она:
# - читает из строки (файла)         `_read`
# - сортирует прочитанные значения   `_sort`
# - фильтрует итоговый результат     `_filter`
# мы бы советовали разнести функционал
# по более узким функциям и написать их с нуля

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list():
    data = _read(csv)
    print("Чтение данных: ", data)
    data = _sort(data)
    print("Сортировка данных: ", data)
    return _filter(data)


# Чтение данных из строки
def _read(csv):
    # [x.split(';') for x in csv.split('\n')]
    data = []
    for line in csv.split('\n'):
        name, age = line.split(';')
        data.append({'name': name, 'age': int(age)})
    return data


# Сортировка по возрасту по возрастанию
def _sort(data):
    numbers_list = []
    new_data = []
    for item in data:
        numbers_list.append(int(item['age']))
    numbers_list.sort()
    for age in numbers_list:
        for item in data:
            if age == item['age']:
                new_data.append(item)
    return new_data  # sorted(data, key=lambda x: int(x[1]))


# Фильтрация
def _filter(data):
    # [x for x in data if int(x[1]) > 10]
    result_data = []
    for person in data:
        if person['age'] < 10:
            continue
        else:
            result_data.append(person)
    return result_data


if __name__ == "__main__":
    print("Фильтрация старше 10 лет: ", get_users_list())
