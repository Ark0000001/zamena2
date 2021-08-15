# replacements = [('Картотека', ''), ('Шкаф', ''), ('для раздевалок усиленный', ''), ('Сейф', '')]
# with open ('modif.csv', 'r') as f:
#     old_data = f.read()
# for line in  old_data:
#     line = line[:-1]
#     for oldtext, newtext in replacements:
#         line = line.replace(oldtext, newtext)
#
# with open ('modif2.txt', 'w') as f:
#     f.write(line)

# list1 = ['Картотека ', 'Шкаф', 'для раздевалок усиленный', 'Сейф']
# list2 = ['', '', '', '']
# with open ('modif.csv', 'r') as f:
#     old_data = f.read()
# for line in old_data:
#     for index, old in enumerate(list1):
#         line = line.replace(old, list2[index])
# with open ('modif2.txt', 'w') as f:
#     f.write(line)



def refine_ang(ang1):
    ang = str.upper(ang1)
    intab = 'А, В, С, Е, Н, К, М, О, Р, Т, Х'
    outtab = 'A, B, C, E, H, K, M, O, P, T, X'
    trantab = ang.maketrans(intab,outtab)
    return ang.translate(trantab)

with open ('sur_железная-мебель.csv', 'r') as f:
  old_data = f.read()

new_data = refine_ang(old_data)

with open ('prom.csv', 'w') as f:
  f.write(new_data)


def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str

# создаем словарь со значениями и строку, которую будет изменять
replace_values = {'KAPТOТEKA':'','ШKAФ':'','PAЗДEВAЛOK':'','PAЗДEBAЛOK':'','(ПPИCTABHAЯ CEKЦИЯ)':'','(ПPOMEЖУTOЧHAЯ CEKЦИЯ)':'','(CEKЦИЯ)':'','ФOPMATA':'','PAЗДEBAЛKИ':'','KAPTOTEЧHЫЙ':'','KAPAT':'','УCИЛEННЫЙ':'','УCИЛEHHЫЙ':'','БУXГAЛTEPCKИЙ':'','УHИBEPCAЛЬHЫЙ':'','ДЛЯ':'','AHTИBAHДAЛЬHЫЙ':'','BRANDMAUER':'','APMEЙCKИЙ':'','APМEЙCKИЙ':'','(БAЗA)':'','(ВEPX)':'','(ПPOМEЖ.CEKЦИЯ)':'','(НИЗ)':'','(4 ПOЛKИ)':'','ДЛЯ':'','ДOП':'','БAЗOВЫЙ':'','УНИВEPCAЛЬНЫЙ':'','AНТИВAНДAЛЬНЫЙ':'','CEЙФ':'','KAPAТ':'','HOTEL':'','OФИCA':'','ПPAKTИK':'','VALBERG':'','БУXГAЛТEPCKИЙ':'','AIKO':'','PAЗДEВAЛKИ':'','(ДOП.CEKЦИЯ)':'','(ПPOМEЖУТOЧНAЯ CEKЦИЯ)':'','БOЛЬШOГO':'','ФOPМAТA':'','KAPТOТEЧНЫЙ':'','OГHECTOЙKAЯ':'','OPУЖEЙHЫЙ':'','ПИCTOЛETHЫЙ':'','ДEПOЗИTHЫЙ':'','(BRANDMAUER)':'','ДOПOЛHИTEЛЬHЫЙ':'','MOДУЛЬ':'','OДEЖДЫ':'','CУMOK':'','OФИCHЫЙ':'','APXИBHЫЙ':'','BЗЛOMOCTOЙKИЙ':'','OГHECTOЙKИЙ':'','KAPTOTEKA':'','(BEPX)':'','(ПPOMEЖ.CEKЦИЯ)':'','(HИЗ)':'','БAЗOBЫЙ':'','-':'','.':'',' ':''}
replace_values2 = {'-':'','.':'',' ':''}
with open ('prom.csv', 'r') as f:
    old_data = f.read()

# изменяем и печатаем строку
my_str1 = multiple_replace(old_data, replace_values)
my_str = multiple_replace(my_str1, replace_values2)
with open ('modif2.csv', 'w') as f:
    f.write(my_str)
