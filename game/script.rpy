# Вы можете расположить сценарий своей игры в этом файле.

define t = Character('Tim', color = "#c8ffc8")
define m = Character('Makeev', color = "#ff8484")
# Определение персонажей игры.
image Tim = "Tim/TimHappy.png"
image TimVipuskn = "Tim/TimV.png"
image TimArmy = "Tim/TimArmy.png"

image Makeev = "Makeev/MakeevHappy.png"
transform slightleft:
    xalign 0.1
    yalign 1.0
transform slightRight:
    xalign 0.8
    yalign 0.5
transform slightCenter:
    xalign 0.7
    yalign 0.5
image ugatu = "bg/Ugatu.jpg"
image army = "bg/army.jpg"
label start:
    scene ugatu
    show Makeev at slightRight
    show Tim at slightleft
    t "Здравствуйте, я пришел сдать лабы."
    m "Хорошо, но тебе придется ходить в универ и сдать мне экзамен."
    t "Ок."
    menu:
        "Ходить в универ и сдавать лабы":
            play music "win.mp3"  
            hide Makeev  # Скрыть Makeev
            hide Tim
            show TimVipuskn
            t "Ура! Я закончил универ"
           
            
            

        "Как-нибудь само сдастся":
            play music "army.mp3"  # Добавление музыки

            hide Makeev  # Скрыть Makeev
            hide Tim
            scene army
            show TimArmy

            t "Зря я не ходил в универ..."
            # scene bg_makeev  # Смена фона на bg_makeev
            # show Tim at slightleft  # Показать Tim с новым костюмом
           

    return