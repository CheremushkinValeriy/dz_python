import view

main_dict = {}
# main_dict = {'FIO:{'math':[4,5], 'phisic':[23,45]}, FIO:{} }'}
name_list = []
lessons_list = []


def start():
    while True:
        print(main_dict)
        op = view.get_op()
        if op == 1:
            name = view.input_student()
            if name not in name_list:
                name_list.append(name)
                main_dict[name] = {}
                for less in lessons_list:
                    main_dict[name][less] = []
                    
        if op == 2:
            less = view.input_les()
            if less not in lessons_list:
                lessons_list.append(less)
                for name in name_list:
                    main_dict[name][less] = []
        if op == 3:
            name, less, mark = view.get_mark()
            main_dict[name][less].append(mark) 
        if op == 4:
            print(main_dict)
        if op == 5:
            name = view.input_student_table()
            print(main_dict[name])
        if op == 6:
            break            



