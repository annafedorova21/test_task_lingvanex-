with open('file.txt') as file:
    for lines in file:
        line_list = list(line.strip().split("\t"))
        new_line_list = [list(set(y.split(' ; '))) for y in line_list]
        eng = open("English.txt", "a")
        rus = open("Russian.txt", "a")
        for eng_word in new_line_list[0]:
            for rus_word in new_line_list[1]:
                eng.write(eng_word + "\n")
                rus.write(rus_word + '\n')











