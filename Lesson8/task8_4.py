'''
Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
'''

import copy


class Warehouse:
    dept_list = ['склад', 'бухгалтерия', 'юристы', 'офис']

    def __init__(self):
        self._equipment_list = []

    def add_equipment(self, obj, quantity):
        for _ in range(quantity):
            obj = copy.deepcopy(obj)
            self._equipment_list.append(obj)

    def moving(self, item):
        tmp_equip_list = []
        models = []
        from_where = Warehouse.is_dept_exist('Откуда? ')
        for el in self._equipment_list:
            if type(el) == item and el.dept == from_where:
                tmp_equip_list.append(el)
                models.append(el.model)
        print(self._equipment_list[0] == tmp_equip_list[0])
        print(id(self._equipment_list[0]))
        print(id(tmp_equip_list[0]))
        models = list(set(models))
        model_name = Warehouse.is_model_exist(models, from_where)
        obj = item
        to_where = Warehouse.is_dept_exist('Куда? ')
        for el in tmp_equip_list:
            if el.model == model_name:
                obj = el
                break
        OfficeEquipment.move(obj, to_where)

    @staticmethod
    def is_dept_exist(txt):
        while True:
            print(f'Список департаментов {Warehouse.dept_list[0]}, {Warehouse.dept_list[1]}, '
                  f'{Warehouse.dept_list[2]}, {Warehouse.dept_list[3]}')
            dept_name = input(txt)
            if dept_name in Warehouse.dept_list:
                return dept_name.lower()
            else:
                print(f'{dept_name} не существует')

    @staticmethod
    def is_model_exist(models_list, dept_name):
        while True:
            print(f'В департаменте {dept_name} есть следующие модели:')
            for el in range(len(models_list)):
                print(models_list[el])
            model_name = input('Выберите модель для перемещения: ')
            if model_name in models_list:
                return model_name
            else:
                print(f'{model_name} не существует')

    def report_dept(self, option=1):
        tmp_equip_list = []
        printers = []
        scanners = []
        copiers = []
        if option == 1:
            dept_name = Warehouse.is_dept_exist('По какому департаменту нужен отчет? ')
            for el in self._equipment_list:
                if el.dept == dept_name:
                    tmp_equip_list.append(el)
        else:
            tmp_equip_list = copy.deepcopy(self._equipment_list)
        for el in tmp_equip_list:
            if type(el) == Printer:
                printers.append(el.model)
            if type(el) == Scanner:
                scanners.append(el.model)
            if type(el) == Copier:
                copiers.append(el.model)
        printers_count = len(printers)
        scanners_count = len(scanners)
        copiers_count = len(copiers)
        printers = list(set(printers))
        scanners = list(set(scanners))
        copiers = list(set(copiers))
        if option == 1:
            print(f'В департаменте "{dept_name}" находится:')
        else:
            print(f'Всего в компании находится:')
        print(f'{printers_count} принтеров моделей {", ".join(printers)}')
        print(f'{scanners_count} сканеров моделей {", ".join(scanners)}')
        print(f'{copiers_count} копировальных аппаратов моделей {", ".join(copiers)}')

    def report_status(self):
        total_working, total_nonworking = 0, 0
        for el in self._equipment_list:
            if el.working:
                total_working += 1
            else:
                total_nonworking += 1
        print(f'Всего в компании {total_working} работающей и {total_nonworking} не работающей техники')


class OfficeEquipment:
    def __init__(self, params, dept, status):
        self.date_receipt = params[1]
        self.dept = dept
        self.warranty = params[2]
        self.working = status

    def move(self, to_dept):
        self.dept = to_dept


class Printer(OfficeEquipment):
    def __init__(self, params, dept='склад', status=True):
        self.model = params[0]
        super().__init__(params, dept, status)


class Scanner(OfficeEquipment):
    def __init__(self, params, dept='склад', status=True):
        self.model = params[0]
        super().__init__(params, dept, status)


class Copier(OfficeEquipment):
    def __init__(self, params, dept='склад', status=True):
        self.model = params[0]
        super().__init__(params, dept, status)


class MyExcept(Exception):
    @classmethod
    def checking(cls, txt):
        try:
            txt = int(txt)
        except ValueError:
            print('Ввeдите число!')
            return [False, txt]
        else:
            return [True, txt]


def input_data():
    model = input('Модель: ')
    while True:
        quantity = input('Количество: ')
        if MyExcept.checking(quantity)[0]:
            quantity = (MyExcept.checking(quantity)[1])
            break
    date_receipt = input('Дата поступления: ')
    while True:
        warranty = input('Гарантия, мес: ')
        if MyExcept.checking(quantity)[0]:
            warranty = (MyExcept.checking(warranty)[1])
            break
    list_of_param = [model, quantity, date_receipt, warranty]
    return list_of_param


def menu(option, txt):
    def info():
        if option == 'main':
            print(f'{txt}. Сделайте свой выбор.')
            print('{:^25} | {:^25} | {:^25} | {:^15}'.format('\033[33m1\033[37m - Добавить на склад',
                                                             '\033[33m2\033[37m - Перемещение товара',
                                                             '\033[33m3\033[37m - Отчеты',
                                                             '\033[33m4\033[37m - Выход'))
        if option == '1' or option == '2':
            print(f'{txt}. Выберите тип товара.')
            print('{:^25} | {:^25} | {:^25} | {:^15}'.format('\033[33m1\033[37m - Принтер',
                                                             '\033[33m2\033[37m - Сканер',
                                                             '\033[33m3\033[37m - Копир',
                                                             '\033[33m4\033[37m - Главное меню'))
        if option == '3':
            print(f'{txt}. Выберите тип отчета.')
            print('{:^25} | {:^25} | {:^25} | {:^15}'.format('\033[33m1\033[37m - Кол-во обор-я в департаменте',
                                                             '\033[33m2\033[37m - Состояние техники',
                                                             '\033[33m3\033[37m - Техники всего',
                                                             '\033[33m4\033[37m - Главное меню'))

    while True:
        info()
        inp_choice = input()
        if inp_choice in ['1', '2', '3', '4']:
            return inp_choice
        else:
            print('Сделайте корректный выбор!')


print('Управление оргтехникой компании')
w = Warehouse()
p = Printer(['HP', '01.02.2019', '12'], 'офис')
w.add_equipment(p, 1)
p = Printer(['HP', '01.02.2019', '12'])
w.add_equipment(p, 3)
p = Scanner(['HP', '01.02.2019', '12'])
w.add_equipment(p, 2)
p = Printer(['Epson', '01.02.2019', '12'])
w.add_equipment(p, 4)
p = Printer(['Canon', '01.02.2019', '12'])
w.add_equipment(p, 3)
p = Copier(['Xerox', '01.02.2019', '12'])
w.add_equipment(p, 3)
p = Copier(['Canon', '01.02.2019', '12'], 'бухгалтерия')
w.add_equipment(p, 2)
p = Copier(['Brother', '01.02.2019', '12'], 'бухгалтерия', False)
w.add_equipment(p, 2)
p = Copier(['Brother', '01.02.2019', '12'])
w.add_equipment(p, 2)
p = Printer(['Brother', '01.02.2019', '12'], 'офис')
w.add_equipment(p, 2)
p = Printer(['Epson', '01.02.2019', '12'], 'офис')
w.add_equipment(p, 1)
p = Printer(['HP', '01.02.2019', '12'], 'юристы')
w.add_equipment(p, 4)
p = Scanner(['Canon', '01.02.2019', '12'])
w.add_equipment(p, 4)
flag = 'main'
choice = choice_1 = ''
while True:
    if flag == 'main':
        choice = menu(flag, 'Главное меню')
    if choice == '1':
        flag = '1'
        choice_1 = menu(flag, 'Добавление товара')
        if choice_1 == '1':
            my_list = input_data()
            num = int(my_list.pop(1))
            org = Printer(my_list)
        elif choice_1 == '2':
            my_list = input_data()
            num = int(my_list.pop(1))
            org = Scanner(my_list)
        elif choice_1 == '3':
            my_list = input_data()
            num = int(my_list.pop(1))
            org = Copier(my_list)
        elif choice_1 == '4':
            flag = 'main'
            continue
        w.add_equipment(org, num)
        continue
    if choice == '2':
        flag = '2'
        choice_1 = menu(flag, 'Перемещение товара')
        if choice_1 == '1':
            w.moving(Printer)
        elif choice_1 == '2':
            w.moving(Scanner)
        elif choice_1 == '3':
            w.moving(Copier)
        elif choice_1 == '4':
            flag = 'main'
            continue
        continue
    if choice == '3':
        flag = '3'
        choice_1 = menu(flag, 'Отчет')
        if choice_1 == '1':
            w.report_dept()
        elif choice_1 == '2':
            w.report_status()
        elif choice_1 == '3':
            w.report_dept(3)
        elif choice_1 == '4':
            flag = 'main'
    if choice == '4':
        break
