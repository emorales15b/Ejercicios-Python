def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Gio", "lastname": "Morales"}

    super_list = [
        {"firstname": "Gio", "lastname": "Morales"},
        {"firstname": "Erick", "lastname": "Bustamante"},
        {"firstname": "Javier", "lastname": "Castro"},
        {"firstname": "Tony", "lastname": "Tenorio"},
        {"firstname": "Abel", "lastname": "Castillo"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    #for key, value in super_dict:
    #    print(key, "-", value)

    for values in super_list:
        for key, value in values.items():
            print(key + ': '+ value)


#entry point
if __name__ == '__main__':
    run()