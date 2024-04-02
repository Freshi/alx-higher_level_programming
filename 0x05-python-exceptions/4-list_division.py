#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_to_print = []
    for i in range(0, list_length):
        try:
            list_to_print.append(my_list_1[i]/my_list_2[i])
        except TypeError:
            print('wrong type')
            list_to_print.append(0)
            continue
        except ZeroDivisionError:
            print('division by 0')
            list_to_print.append(0)
        except IndexError:
            print('out of range')
            list_to_print.append(0)
        finally:
            return list_to_print
