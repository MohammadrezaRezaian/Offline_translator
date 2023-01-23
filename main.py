import fun

while True:
    num = fun.start_menu()
    if num == 1:
        fun.tranc_en(fun.words_source)
    elif num == 2:
        fun.tranc_fa(fun.words_source)
    elif num == 3:
        fun.edit()
    elif num == 4:
        fun.learn()
    elif num == 5:
        fun.view()
    elif num == 6:
        fun.about()
    elif num == 7:
        fun.exi()
        break
    else:
        fun.ekhtar()
