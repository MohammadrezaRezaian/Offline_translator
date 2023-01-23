import vis

words_source = dict(hello="سلام", world="دنيا", python="پايتون", mohammadreza="محمدرضا", rezaian="رضايان")

def start_menu():
    num = int(input(vis.vis["start"]))
    return num

def tranc_en(word_sorce):
    txt_in = input(vis.vis["tranc_en_1"])
    txt = txt_in.split(" ")
    er_wo = []
    for word in txt:
        if word in word_sorce:
            index_word = txt.index(word)
            txt[index_word] = word_sorce[word]
        else:
            er_wo.append(word)
    r = " ,".join(er_wo)
    print(vis.vis["tranc_en"]%(txt_in, " ".join(txt),r))
    num_vor = input("")
    if num_vor == "a":
        tranc_en(words_source)
    elif num_vor == "e":
        edit()
    else:
        pass

def tranc_fa(word_sorce):
    num = input(vis.vis["dar_sa"])
    if num != " ":
        pass




def edit():
    print(vis.vis["update_ed"])
    en_word = input(vis.vis["en_word"])
    fa_word = input(vis.vis["fa_word"]%en_word)
    words_source[en_word] = fa_word
    word = input(vis.vis["update_word"])
    if word == "y":
        edit()
    else:
        pass

def view():
    print(vis.vis["list_word"])
    for i in words_source:
        print(f"   {i}               {words_source[i]}")
    ok_e = input(vis.vis["list_word_end"])
    if ok_e != " ":
        pass

def learn():
    print("dar hal sakht")

def about():
    en=input(vis.vis["about"])
    if en != " ":
        pass

def exi():
    print(vis.vis["exi"])

def ekhtar():
    print(vis.vis["ekhtar"])


