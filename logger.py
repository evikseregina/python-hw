
from data_create import name_data, surname_data,address_data,phone_data

def input_data():
    name = name_data()
    surname = surname_data()
    address = address_data()
    phone = phone_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 вариант: \n"
    f"{name};{surname};{phone};{address}\n"                                                                
    f"Выберите вариант "))

    while var != 1 and var != 2:
      print("Неправильный ввод")
      var = int(input("Введите число "))
    if var == 1:
       with open('data_first_variant.csv','a',encoding='utf-8') as f:
          f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
      with open('data_second_variant.csv','a',encoding='utf-8') as f:
        f.write(f"{name};{surname};{phone};{address}\n\n")      


def print_data():
    print('Вывожу данные из первого файла: \n')
    with open('data_first_variant.csv','r',encoding='utf-8') as f:
       data_first = f.readlines()
       data_first_list = []
       j = 0
       for i in range(len(data_first)):
          if data_first[i] == '\n' or i == len(data_first)-1:
             data_first_list.append(''.join(data_first[j:i+1]))
             j = i
       print(''.join(data_first_list))      

    print('Вывожу данные из второго файла: \n\n'
          )
    with open('data_second_variant.csv','r',encoding='utf-8') as f:
        data_second = f.readlines()
        print(*data_second)


print_data()   

def change_data():
   print("Какую строчку вы хотите изменить?: \n 1 имя \n 2 фамилия")
   change = int(input("Введите число: "))

   while change != 1 and change != 2:
        print("Неправильный ввод")
        change = int(input("Введите число"))
   if change == 1:        
      with open('data_first_variant.csv','r',encoding='utf-8') as f:
            data_read = f.readlines()
            data_first_list2 = []
            first_name = input("Введите новое имя: ")
            data_first_list2.append(f'{first_name}\n')
            j = 1
            for i in range(len(data_read)):
               if data_read[i]== '\n'or i == len(data_read)-1 :
                data_first_list2.append(''.join(data_read[j:i+1]))
                j = i
            print("Ваш результат: \n")           
            print(''.join(data_first_list2))   
      with open('data_second_variant.csv','r',encoding='utf-8') as f:
            data_second = f.readlines()
            j = data_second[0].index(";")
            data_second_list2 =[]
            data_second_list2.append(f'{first_name}{data_second[0][j:]}{''.join(data_second[1:])}')
            print(*data_second_list2)
                
   if change == 2: 
      with open('data_first_variant.csv','r',encoding='utf-8') as f:
             data_read2 = f.readlines() 
             data_first_list_surname =[] 
             first_surname = input("Введите вашу новую фамилию : ")
             j = 2
             for i in range(len(data_read2)):
               if i == j-2:
                  data_first_list_surname.append(''.join(data_read2[:j-1]))
                  data_first_list_surname.append(f'{first_surname}\n')
               elif  data_read2[i]== '\n'or i == len(data_read2)-1:
                  data_first_list_surname.append(''.join(data_read2[j:i+1]))
                  j=i 
                  
             print("Ваш результат: \n")                 
             print(''.join(data_first_list_surname))   
      with open('data_second_variant.csv','r',encoding='utf-8') as f:
            data_second = f.readlines() 
            j = data_second[0].index(";")
            data_second_surname=[]
            data_second_surname.append(f'{data_second[0][:j+1]}{first_surname}{data_second[0][j+8:]}{''.join(data_second[1:])}')                                
            print(*data_second_surname)

def delete_data():
   print("Какую строчку вы хотите удалить?; \n 1 имя \n 2 фамилию")
   delete = int(input("Введите число: "))
   while delete != 1 and delete != 2:
        print("Неправильный ввод")
        delete = int(input("Введите число"))
   if delete == 1:        
      with open('data_first_variant.csv','r',encoding='utf-8') as f:
            data_read = f.readlines()
            data_first_delete = []  
            j = 1
            for i in range(len(data_read)):
                if i != 0 and data_read[i]== '\n':
                   data_first_delete.append(' '.join(data_read[j:i+1]))   
                   j = i
            print("Ваш результат: \n")                 
            print(''.join(data_first_delete))  
      with open('data_second_variant.csv','r',encoding='utf-8') as f:
            data_second = f.readlines()  
            j = data_second[0].index(";")
            data_second_list2 =[]
            data_second_list2.append(f'{data_second[0][j+1:]}{''.join(data_second[1:])}')
            print(*data_second_list2)     

   if delete == 2:
        with open('data_first_variant.csv','r',encoding='utf-8') as f:
            data_read = f.readlines()
            data_first_delete_surname = []  
            j = 1 
            for i in range(len(data_read)):
                if i == 0:
                   data_first_delete_surname.append(''.join(data_read[:j]))
                if i != 1 and data_read[i]== '\n':
                    data_first_delete_surname.append(''.join(data_read[j+1:i+1]))
                    j = i   
            print("Ваш результат: \n")                 
            print(''.join(data_first_delete_surname))
        with open('data_second_variant.csv','r',encoding='utf-8') as f:
            data_second = f.readlines()  
            j = data_second[0].index(";")
            data_second_list2 =[]
            data_second_list2.append(f'{data_second[0][:j+1]}{data_second[0][j+9:]}{''.join(data_second[1:])}')
            print(*data_second_list2)             