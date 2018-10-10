image Protif0 = "/images/Bob_work/entrance/M/Protif0.jpg"
image Protif1 = "/images/Bob_work/entrance/M/Protif1.jpg"
image Protif2 = "/images/Bob_work/entrance/M/Protif2.jpg"
default company_profit = 0

label bob_receptiondiagram:
    $ can_hide_windows = True
    hide screen map_button
    if company_profit == 0:
        scene Protif0
        if renpy.loadable("patch.rpy"):
            MC "(Эх ... Прибыли не выглядят слишком плохо для папы.)"
        else:
            MC "(Эх ... Прибыли не выглядят слишком плохо для Боба.)"
        MC "(В последние месяцы они попали в хит, но, по крайней мере, похоже, что в итоге все стабилизируется.)"
        MC "(Должно быть, поэтому он был так занят.)"

    if company_profit ==1:
        scene Protif1
        if renpy.loadable("patch.rpy"):
            MC "(Ох ... Похоже, что я раздаю конфиденциальную информацию о компании Зури, что привело к падению прибыли папы!)"
        else:
            MC "(Ох ... Похоже, что я раздавал конфиденциальную информацию о компании Зури, что привело к падению прибыли Боба!)"


    if company_profit == 2:
        scene Protif2
        if renpy.loadable("patch.rpy"):
            MC "(А? Ложь Зури обеспечила возвращение компании папы в выгодное положение. Хорошо видеть!)"
            MC "(Прогнозы выглядят еще сильнее, чем до крушения. Папа будет доволен этим!)"
        else:
            MC "(Ложь Зури гарантирует, что компания Боба вернется в выгодное положение. Это приятно видеть!)"
            MC "(Прогнозы выглядят еще сильнее, чем до аварии. Боб будет доволен этим!)"
    $ can_hide_windows = False
    jump bob_entrance_M1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
