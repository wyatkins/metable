marka = input('Введите марку: ')
print(marka)
print(marka.upper())
print(list(marka))

# Проверка на углерод
if marka[0] == '1':
    marka_uglerod = 1 / 10
    print('Содержание С', marka_uglerod, end='%\n')
elif marka[0] == '2':
    marka_uglerod = 2 / 10
    print('Содержание С', marka_uglerod, end='%\n')
elif marka[0] == '3':
    marka_uglerod = 3 / 10
    print('Содержание С', marka_uglerod, end='%\n')
elif marka[0] == '4':
    marka_uglerod = 4 / 10
    print('Содержание С', marka_uglerod, end='%\n')
elif marka[0] == '5':
    marka_uglerod = 5 / 10
    print('Содержание С', marka_uglerod, end='%\n')
elif marka[0] == '6':
    marka_uglerod = 6 / 10
    print('Содержание С', marka_uglerod, end='%\n')
elif marka[0] == '7':
    marka_uglerod = 7 / 10
    print('Содержание С', marka_uglerod, end='%\n')
elif marka[0] == '8':
    marka_uglerod = 8 / 10
    print('Содержание С', marka_uglerod, end='%\n')
elif marka[0] == '9':
    marka_uglerod = 9 / 10
    print('Содержание С', marka_uglerod, end='%\n')
else:
    marka_uglerod = 1.0
    print('Количество углерода в пределах 1%')

# Классификация стали
print('Классификация стали', marka.upper())

print('по химическому составу:')

# Углеродистость
if marka_uglerod == 0.1:
    print('Низкоуглеродистая')
elif marka_uglerod == 0.2 or marka_uglerod == 0.3 or marka_uglerod == 0.4:
    print('Среднеуглеродистая')
else:
    print('Высокоуглеродистая')

# Легирование
if 'х' in marka or 'с' in marka or 'т' in marka or 'д' in marka or 'в' in marka or 'г' in marka \
        or 'ф' in marka or 'р' in marka or 'а' in marka or 'н' in marka or 'к' in marka and not \
        marka[-1] == 'к' or 'м' in marka or 'б' in marka or 'е' in marka or 'ц' in marka or 'ю' in marka:
    print('легированная')

# Качество
print('по качеству:')
if marka[-1] == 'а':
    print('Высококачественная (содержание серы и фосфора не более 0,025%)')
elif marka[-1] == 'ш':
    print('Сталь электрошлакового переплава (особовысококачественная сталь)')
elif marka[-1] == 'д' and marka[-2] == 'в':
    print('Сталь вакуумно-дугового переплава (особовысококачественная сталь)')
else:
    print('Обыкновенного качества')

# Назначение
print('по назначению:')
if marka[-1] == 'т':
    print('Термоупрочненная')
elif marka[-1] == 'к':
    print('С повышенной коррозионной стойкостью')
elif marka[0] == 'с':
    print('Строительная')
elif marka[0] == 'р':
    print('Быстрорежущая, инструментальная')
elif marka[0] == 'у':
    print('Инструментальная')
elif marka[0] == 'ш':
    print('Подшипниковая')
else:
    print('Конструкционная')

# Хром
if 'х' in marka or marka[0] == 'р':
    print('Хром есть')
if 'х' in marka and 'х2' not in marka and 'х3' not in marka and 'х4' not in marka and 'х5' not in marka and 'х6' \
        not in marka and 'х7' not in marka and 'х8' not in marka and 'х9' not \
        in marka and 'х10' not in marka and 'х11' not in marka and 'х12' not in marka and 'х13' \
        not in marka and 'х14' not in marka and 'х15' not in marka and 'х16' not in marka and 'х17' not \
        in marka and 'х18' not in marka and 'х19' not in marka:
    print('1%')
elif 'х2' in marka:
    print('2%')
elif 'х3' in marka:
    print('3%')
elif 'х4' in marka:
    print('4%')
elif marka[0] == 'р':
    print('4%*')
elif 'х5' in marka:
    print('5%')
elif 'х6' in marka:
    print('6%')
elif 'х7' in marka:
    print('7%')
elif 'х8' in marka:
    print('8%')
elif 'х9' in marka:
    print('9%')
elif 'х10' in marka:
    print('10%')
elif 'х11' in marka:
    print('11%')
elif 'х12' in marka:
    print('12%')
elif 'х13' in marka:
    print('13%')
elif 'х14' in marka:
    print('14%')
elif 'х15' in marka:
    print('15%')
elif 'х16' in marka:
    print('16%')
elif 'х17' in marka:
    print('17%')
elif 'х18' in marka:
    print('18%')
elif 'х19' in marka:
    print('19%')
else:
    print('Хрома нет')

# Кремний
if 'с' in marka:
    print('Кремний есть')
if 'с' in marka and 'с2' not in marka and 'с3' not in marka and 'с4' not in marka and 'с5' not in marka and 'с6' \
        not in marka and 'с7' not in marka and 'с8' not in marka and 'с9' not in marka and 'с10' not in marka and \
        'с11' not in marka and 'с12' not in marka and 'с13' not in marka and 'с14' not in marka and 'с15' \
        not in marka and 'с16' not in marka and 'с17' not in marka and 'с18' not in marka and 'с19' not in marka:
    print('1%')
elif 'с2' in marka:
    print('2%')
elif 'с2' in marka:
    print('3%')
elif 'с4' in marka:
    print('4%')
elif 'с5' in marka:
    print('5%')
elif 'с6' in marka:
    print('6%')
elif 'с7' in marka:
    print('7%')
elif 'с8' in marka:
    print('8%')
elif 'с9' in marka:
    print('9%')
elif 'с10' in marka:
    print('10%')
elif 'с11' in marka:
    print('11%')
elif 'с12' in marka:
    print('12%')
elif 'с13' in marka:
    print('13%')
elif 'с14' in marka:
    print('14%')
elif 'с15' in marka:
    print('15%')
elif 'с16' in marka:
    print('16%')
elif 'с17' in marka:
    print('17%')
elif 'с18' in marka:
    print('18%')
elif 'с19' in marka:
    print('19%')
else:
    print('Кремния нет')

# Титан
if 'т' in marka:
    print('Титан есть')
if 'т' in marka and 'т2' not in marka and 'т3' not in marka and 'т4' not in marka and 'т5' not in marka and \
    'т6' not in marka and 'т7' not in marka and 'т8' not in marka and 'т9' not in marka and 'т10' not in marka \
        and 'т11' not in marka and 'т12' not in marka and 'т13' not in marka and 'т14' not in marka and 'т15' \
            not in marka and 'т16' not in marka and 'т17' not in marka and 'т18' not in marka and 'т19' not in marka:
    print('1%')
elif 'т2' in marka:
    print('2%')
elif 'т3' in marka:
    print('3%')
elif 'т4' in marka:
    print('4%')
elif 'т5' in marka:
    print('5%')
elif 'т6' in marka:
    print('6%')
elif 'т7' in marka:
    print('7%')
elif 'т8' in marka:
    print('8%')
elif 'т9' in marka:
    print('9%')
elif 'т10' in marka:
    print('10%')
elif 'т11' in marka:
    print('11%')
elif 'т12' in marka:
    print('12%')
elif 'т13' in marka:
    print('13%')
elif 'т14' in marka:
    print('14%')
elif 'т15' in marka:
    print('15%')
elif 'т16' in marka:
    print('16%')
elif 'т17' in marka:
    print('17%')
elif 'т18' in marka:
    print('18%')
elif 'т19' in marka:
    print('19%')
else:
    print('Титана нет')

# Медь
if 'д' in marka:
    print('Медь есть')
if 'д' in marka and 'д2' not in marka and 'д3' not in marka and 'д4' not in marka and 'д5' not in marka \
        and 'д6' not in marka and 'д7' not in marka and 'д8' not in marka and 'д9' not in marka and 'д10' \
        not in marka and 'д11' not in marka and 'д12' not in marka and 'д13' not in marka and 'д14' \
        not in marka and 'д15' not in marka and 'д16' not in marka and 'д17' not in marka and 'д18' \
        not in marka and 'д19' not in marka:
    print('1%')
elif 'д2' in marka:
    print('2%')
elif 'д3' in marka:
    print('3%')
elif 'д4' in marka:
    print('4%')
elif 'д5' in marka:
    print('5%')
elif 'д6' in marka:
    print('6%')
elif 'д7' in marka:
    print('7%')
elif 'д8' in marka:
    print('8%')
elif 'д9' in marka:
    print('9%')
elif 'д10' in marka:
    print('10%')
elif 'д11' in marka:
    print('11%')
elif 'д12' in marka:
    print('12%')
elif 'д13' in marka:
    print('13%')
elif 'д14' in marka:
    print('14%')
elif 'д15' in marka:
    print('15%')
elif 'д16' in marka:
    print('16%')
elif 'д17' in marka:
    print('17%')
elif 'д18' in marka:
    print('18%')
elif 'д19' in marka:
    print('19%')
else:
    print('Меди нет')

# Вольфрам
if 'в' in marka or marka[0] == 'р':
    print('Вольфрам есть')
if 'в' in marka and 'в2' not in marka and 'в3' not in marka and 'в4' not in marka and 'в5' not in marka \
        and 'в6' not in marka and 'в7' not in marka and 'в8' not in marka and 'в9' not in marka and 'в10' \
            not in marka and 'в11' not in marka and 'в12' not in marka and 'в13' not in marka and 'в14' \
        not in marka and 'в15' not in marka and 'в16' not in marka and 'в17' not in marka and 'в18' \
        not in marka and 'в19' not in marka:
    print('1%')
elif 'в2' in marka or 'р2' in marka and marka[0] == 'р':
    print('2%')
elif 'в3' in marka or 'р3' in marka and marka[0] == 'р':
    print('3%')
elif 'в4' in marka or 'р4' in marka and marka[0] == 'р':
    print('4%')
elif 'в5' in marka or 'р5' in marka and marka[0] == 'р':
    print('5%')
elif 'в6' in marka or 'р6' in marka and marka[0] == 'р':
    print('6%')
elif 'в7' in marka or 'р7' in marka and marka[0] == 'р':
    print('7%')
elif 'в8' in marka or 'р8' in marka and marka[0] == 'р':
    print('8%')
elif 'в9' in marka or 'р9' in marka and marka[0] == 'р':
    print('9%')
elif 'в10' in marka or 'р10' in marka and marka[0] == 'р':
    print('10%')
elif 'в11' in marka or 'р11' in marka and marka[0] == 'р':
    print('11%')
elif 'в12' in marka or 'р12' in marka and marka[0] == 'р':
    print('12%')
elif 'в13' in marka or 'р13' in marka and marka[0] == 'р':
    print('13%')
elif 'в14' in marka or 'р14' in marka and marka[0] == 'р':
    print('14%')
elif 'в15' in marka or 'р15' in marka and marka[0] == 'р':
    print('15%')
elif 'в16' in marka or 'р16' in marka and marka[0] == 'р':
    print('16%')
elif 'в17' in marka or 'р17' in marka and marka[0] == 'р':
    print('17%')
elif 'в18' in marka or 'р18' in marka and marka[0] == 'р':
    print('18%')
elif 'в19' in marka or 'р19' in marka and marka[0] == 'р':
    print('19%')
else:
    print('Вольфрама нет')

# Марганец
if "г" in marka:
    print('Марганец есть')
if "г" in marka and "г2" not in marka and "г3" not in marka and "г4" not in marka and "г5" not in marka \
        and "г6" not in marka and "г7" not in marka and "г8" not in marka and "г9" not in marka and "г10" \
            not in marka and "г11" not in marka and "г12" not in marka and "г13" not in marka and "г14" \
        not in marka and "г15" not in marka and "г16" not in marka and "г17" not in marka and "г18" \
        not in marka and "г19" not in marka:
    print('1%')
elif "г2" in marka:
    print('2%')
elif "г3" in marka:
    print('3%')
elif "г4" in marka:
    print('4%')
elif "г5" in marka:
    print('5%')
elif "г6" in marka:
    print('6%')
elif "г7" in marka:
    print('7%')
elif "г8" in marka:
    print('8%')
elif "г9" in marka:
    print('9%')
elif "г10" in marka:
    print('10%')
elif "г11" in marka:
    print('11%')
elif "г12" in marka:
    print('12%')
elif "г13" in marka:
    print('13%')
elif "г14" in marka:
    print('14%')
elif "г15" in marka:
    print('15%')
elif "г16" in marka:
    print('16%')
elif "г17" in marka:
    print('17%')
elif "г18" in marka:
    print('18%')
elif "г19" in marka:
    print('19%')
else:
    print('Марганца нет')

# Ванадий
if "ф" in marka:
    print('Ванадий есть')
if "ф" in marka and "ф2" not in marka and "ф3" not in marka and "ф4" not in marka and "ф5" not in marka \
        and "ф6" not in marka and "ф7" not in marka and "ф8" not in marka and "ф9" not in marka and "ф10" \
            not in marka and "ф11" not in marka and "ф12" not in marka and "ф13" not in marka and "ф14" \
        not in marka and "ф15" not in marka and "ф16" not in marka and "ф17" not in marka and "ф18" \
        not in marka and "ф19" not in marka:
    print('1%')
elif "ф2" in marka:
    print('2%')
elif "ф3" in marka:
    print('3%')
elif "ф4" in marka:
    print('4%')
elif "ф5" in marka:
    print('5%')
elif "ф6" in marka:
    print('6%')
elif "ф7" in marka:
    print('7%')
elif "ф8" in marka:
    print('8%')
elif "ф9" in marka:
    print('9%')
elif "ф10" in marka:
    print('10%')
elif "ф11" in marka:
    print('11%')
elif "ф12" in marka:
    print('12%')
elif "ф13" in marka:
    print('13%')
elif "ф14" in marka:
    print('14%')
elif "ф15" in marka:
    print('15%')
elif "ф16" in marka:
    print('16%')
elif "ф17" in marka:
    print('17%')
elif "ф18" in marka:
    print('18%')
elif "ф19" in marka:
    print('19%')
else:
    print('Ванадия нет')

# Бор
if "р" in marka and not marka[0] == "р":
    print('Бор есть')
if "р" in marka and not marka[0] == "р" and "р2" not in marka and "р3" not in marka and "р4" not in marka \
        and "р5" not in marka and "р6" not in marka and "р7" not in marka and "р8" not in marka and "р9" \
        not in marka and "р10" not in marka and "р11" not in marka and "р12" not in marka and "р13" \
        not in marka and "р14" not in marka and "р15" not in marka and "р16" not in marka and "р17" \
        not in marka and "р18" not in marka and "р19" not in marka:
    print('1%')
elif "р2" in marka and not marka[0] == "р":
    print('2%')
elif "р3" in marka and not marka[0] == "р":
    print('3%')
elif "р4" in marka and not marka[0] == "р":
    print('4%')
elif "р5" in marka and not marka[0] == "р":
    print('5%')
elif "р6" in marka and not marka[0] == "р":
    print('6%')
elif "р7" in marka and not marka[0] == "р":
    print('7%')
elif "р8" in marka and not marka[0] == "р":
    print('8%')
elif "р9" in marka and not marka[0] == "р":
    print('9%')
elif "р10" in marka and not marka[0] == "р":
    print('10%')
elif "р11" in marka and not marka[0] == "р":
    print('11%')
elif "р12" in marka and not marka[0] == "р":
    print('12%')
elif "р13" in marka and not marka[0] == "р":
    print('13%')
elif "р14" in marka and not marka[0] == "р":
    print('14%')
elif "р15" in marka and not marka[0] == "р":
    print('15%')
elif "р16" in marka and not marka[0] == "р":
    print('16%')
elif "р17" in marka and not marka[0] == "р":
    print('17%')
elif "р18" in marka and not marka[0] == "р":
    print('18%')
elif "р19" in marka and not marka[0] == "р":
    print('19%')
else:
    print('Бора нет')

# Азот
if "а" in marka and not marka[-1] == "а":
    print('Азот есть')
if "а" in marka and not marka[-1] == "а" and "а2" not in marka and "а3" not in marka and "а4" \
        not in marka and "а5" not in marka and "а6" not in marka and "а7" not in marka and "а8" \
    not in marka and "а9" not in marka and "а10" not in marka and "а11" not in marka and "а12" \
        not in marka and "а13" not in marka and "а14" not in marka and "а15" not in marka and "а16" \
        not in marka and "а17" not in marka and "а18" not in marka and "а19" not in marka:
    print('1%')
elif "а2" in marka and not marka[-1] == "а":
    print('2%')
elif "а3" in marka and not marka[-1] == "а":
    print('3%')
elif "а4" in marka and not marka[-1] == "а":
    print('4%')
elif "а5" in marka and not marka[-1] == "а":
    print('5%')
elif "а6" in marka and not marka[-1] == "а":
    print('6%')
elif "а7" in marka and not marka[-1] == "а":
    print('7%')
elif "а8" in marka and not marka[-1] == "а":
    print('8%')
elif "а9" in marka and not marka[-1] == "а":
    print('9%')
elif "а10" in marka and not marka[-1] == "а":
    print('10%')
elif "а11" in marka and not marka[-1] == "а":
    print('11%')
elif "а12" in marka and not marka[-1] == "а":
    print('12%')
elif "а13" in marka and not marka[-1] == "а":
    print('13%')
elif "а14" in marka and not marka[-1] == "а":
    print('14%')
elif "а15" in marka and not marka[-1] == "а":
    print('15%')
elif "а16" in marka and not marka[-1] == "а":
    print('16%')
elif "а17" in marka and not marka[-1] == "а":
    print('17%')
elif "а18" in marka and not marka[-1] == "а":
    print('18%')
elif "а19" in marka and not marka[-1] == "а":
    print('19%')
else:
    print('Азота нет')

# Никель
if "н" in marka:
    print('Никель есть')
if "н" in marka and "н2" not in marka and "н3" not in marka and "н4" not in marka and "н5" not in marka \
        and "н6" not in marka and "н7" not in marka and "н8" not in marka and "н9" not in marka and "н10" \
            not in marka and "н11" not in marka and "н12" not in marka and "н13" not in marka and "н14" \
        not in marka and "н15" not in marka and "н16" not in marka and "н17" not in marka and "н18" \
        not in marka and "н19" not in marka:
    print('1%')
elif "н2" in marka:
    print('2%')
elif "н3" in marka:
    print('3%')
elif "н4" in marka:
    print('4%')
elif "н5" in marka:
    print('5%')
elif "н6" in marka:
    print('6%')
elif "н7" in marka:
    print('7%')
elif "н8" in marka:
    print('8%')
elif "н9" in marka:
    print('9%')
elif "н10" in marka:
    print('10%')
elif "н11" in marka:
    print('11%')
elif "н12" in marka:
    print('12%')
elif "н13" in marka:
    print('13%')
elif "н14" in marka:
    print('14%')
elif "н15" in marka:
    print('15%')
elif "н16" in marka:
    print('16%')
elif "н17" in marka:
    print('17%')
elif "н18" in marka:
    print('18%')
elif "н19" in marka:
    print('19%')
else:
    print('Никеля нет')

# Молибден
if "м" in marka:
    print('Молибден есть')
if "м" in marka and "м2" not in marka and "м3" not in marka and "м4" not in marka and "м5" \
        not in marka and "м6" not in marka and "м7" not in marka and "м8" not in marka and "м9" \
    not in marka and "м10" not in marka and "м11" not in marka and "м12" not in marka and "м13" \
        not in marka and "м14" not in marka and "м15" not in marka and "м16" not in marka and "м17" \
        not in marka and "м18" not in marka and "м19" not in marka:
    print('1%')
elif "м2" in marka:
    print('2%')
elif "м3" in marka:
    print('3%')
elif "м4" in marka:
    print('4%')
elif "м5" in marka:
    print('5%')
elif "м6" in marka:
    print('6%')
elif "м7" in marka:
    print('7%')
elif "м8" in marka:
    print('8%')
elif "м9" in marka:
    print('9%')
elif "м10" in marka:
    print('10%')
elif "м11" in marka:
    print('11%')
elif "м12" in marka:
    print('12%')
elif "м13" in marka:
    print('13%')
elif "м14" in marka:
    print('14%')
elif "м15" in marka:
    print('15%')
elif "м16" in marka:
    print('16%')
elif "м17" in marka:
    print('17%')
elif "м18" in marka:
    print('18%')
elif "м19" in marka:
    print('19%')
else:
    print('Молибдена нет')

# Кобальт
if "к" in marka and not marka[-1] == "к":
    print('Кобальт есть')
if "к" in marka and not marka[-1] == "к" and "к2" not in marka and "к3" not in marka and "к4" \
        not in marka and "к5" not in marka and "к6" not in marka and "к7" not in marka and "к8" \
    not in marka and "к9" not in marka and "к10" not in marka and "к11" not in marka and "к12" \
        not in marka and "к13" not in marka and "к14" not in marka and "к15" not in marka and "к16" \
        not in marka and "к17" not in marka and "к18" not in marka and "к19" not in marka:
    print('1%')
elif "к2" in marka:
    print('2%')
elif "к3" in marka:
    print('3%')
elif "к4" in marka:
    print('4%')
elif "к5" in marka:
    print('5%')
elif "к6" in marka:
    print('6%')
elif "к7" in marka:
    print('7%')
elif "к8" in marka:
    print('8%')
elif "к9" in marka:
    print('9%')
elif "к10" in marka:
    print('10%')
elif "к11" in marka:
    print('11%')
elif "к12" in marka:
    print('12%')
elif "к13" in marka:
    print('13%')
elif "к14" in marka:
    print('14%')
elif "к15" in marka:
    print('15%')
elif "к16" in marka:
    print('16%')
elif "к17" in marka:
    print('17%')
elif "к18" in marka:
    print('18%')
elif "к19" in marka:
    print('19%')
else:
    print('Кобальта нет')

# Ниобий
if "б" in marka:
    print('Ниобий есть')
if "б" in marka and "б2" not in marka and "б3" not in marka and "б4" not in marka and "б5" \
        not in marka and "б6" not in marka and "б7" not in marka and "б8" not in marka and "б9" \
    not in marka and "б10" not in marka and "б11" not in marka and "б12" not in marka and "б13" \
        not in marka and "б14" not in marka and "б15" not in marka and "б16" not in marka and "б17" \
        not in marka and "б18" not in marka and "б19" not in marka:
    print('1%')
elif "б2" in marka:
    print('2%')
elif "б3" in marka:
    print('3%')
elif "б4" in marka:
    print('4%')
elif "б5" in marka:
    print('5%')
elif "б6" in marka:
    print('6%')
elif "б7" in marka:
    print('7%')
elif "б8" in marka:
    print('8%')
elif "б9" in marka:
    print('9%')
elif "б10" in marka:
    print('10%')
elif "б11" in marka:
    print('11%')
elif "б12" in marka:
    print('12%')
elif "б13" in marka:
    print('13%')
elif "б14" in marka:
    print('14%')
elif "б15" in marka:
    print('15%')
elif "б16" in marka:
    print('16%')
elif "б17" in marka:
    print('17%')
elif "б18" in marka:
    print('18%')
elif "б19" in marka:
    print('19%')
else:
    print('Ниобия нет')

# Селен
if "е" in marka:
    print('Селен есть')
if "е" in marka and "е2" not in marka and "е3" not in marka and "е4" not in marka and "е5" not in marka \
        and "е6" not in marka and "е7" not in marka and "е8" not in marka and "е9" not in marka and "е10" \
            not in marka and "е11" not in marka and "е12" not in marka and "е13" not in marka and "е14" \
        not in marka and "е15" not in marka and "е16" not in marka and "е17" not in marka and "е18" \
        not in marka and "е19" not in marka:
    print('1%')
elif "е2" in marka:
    print('2%')
elif "е3" in marka:
    print('3%')
elif "е4" in marka:
    print('4%')
elif "е5" in marka:
    print('5%')
elif "е6" in marka:
    print('6%')
elif "е7" in marka:
    print('7%')
elif "е8" in marka:
    print('8%')
elif "е9" in marka:
    print('9%')
elif "е10" in marka:
    print('10%')
elif "е11" in marka:
    print('11%')
elif "е12" in marka:
    print('12%')
elif "е13" in marka:
    print('13%')
elif "е14" in marka:
    print('14%')
elif "е15" in marka:
    print('15%')
elif "е16" in marka:
    print('16%')
elif "е17" in marka:
    print('17%')
elif "е18" in marka:
    print('18%')
elif "е19" in marka:
    print('19%')
else:
    print('Селена нет')

# Цирконий
if "ц" in marka:
    print('Цирконий есть')
if "ц" in marka and "ц2" not in marka and "ц3" not in marka and "ц4" not in marka and "ц5" not in marka \
        and "ц6" not in marka and "ц7" not in marka and "ц8" not in marka and "ц9" not in marka and "ц10" \
            not in marka and "ц11" not in marka and "ц12" not in marka and "ц13" not in marka and "ц14" not in marka \
        and "ц15" not in marka and "ц16" not in marka and "ц17" not in marka and "ц18" not in marka \
        and "ц19" not in marka:
    print('1%')
elif "ц2" in marka:
    print('2%')
elif "ц3" in marka:
    print('3%')
elif "ц4" in marka:
    print('4%')
elif "ц5" in marka:
    print('5%')
elif "ц6" in marka:
    print('6%')
elif "ц7" in marka:
    print('7%')
elif "ц8" in marka:
    print('8%')
elif "ц9" in marka:
    print('9%')
elif "ц10" in marka:
    print('10%')
elif "ц11" in marka:
    print('11%')
elif "ц12" in marka:
    print('12%')
elif "ц13" in marka:
    print('13%')
elif "ц14" in marka:
    print('14%')
elif "ц15" in marka:
    print('15%')
elif "ц16" in marka:
    print('16%')
elif "ц17" in marka:
    print('17%')
elif "ц18" in marka:
    print('18%')
elif "ц19" in marka:
    print('19%')
else:
    print('Циркония нет')

# Алюминий
if "ю" in marka:
    print('Алюминий есть')
if "ю" in marka and "ю2" not in marka and "ю3" not in marka and "ю4" not in marka and "ю5" not in marka \
        and "ю6" not in marka and "ю7" not in marka and "ю8" not in marka and "ю9" not in marka and "ю10" \
            not in marka and "ю11" not in marka and "ю12" not in marka and "ю13" not in marka and "ю14" \
        not in marka and "ю15" not in marka and "ю16" not in marka and "ю17" not in marka and "ю18" \
        not in marka and "ю19" not in marka:
    print('1%')
elif "ю2" in marka:
    print('2%')
elif "ю3" in marka:
    print('3%')
elif "ю4" in marka:
    print('4%')
elif "ю5" in marka:
    print('5%')
elif "ю6" in marka:
    print('6%')
elif "ю7" in marka:
    print('7%')
elif "ю8" in marka:
    print('8%')
elif "ю9" in marka:
    print('9%')
elif "ю10" in marka:
    print('10%')
elif "ю11" in marka:
    print('11%')
elif "ю12" in marka:
    print('12%')
elif "ю13" in marka:
    print('13%')
elif "ю14" in marka:
    print('14%')
elif "ю15" in marka:
    print('15%')
elif "ю16" in marka:
    print('16%')
elif "ю17" in marka:
    print('17%')
elif "ю18" in marka:
    print('18%')
elif "ю19" in marka:
    print('19%')
else:
    print('Алюминия нет')

# Быстрорез
if marka[0] == "р":
    print('-'*50)
    print('* Примечание: Во всех быстрорежущих сталях содержится Хром около 4%.')
    print()
