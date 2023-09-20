# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.
decimal_number = int(input('Введите целое число:'))
hex_number = format(decimal_number, "x")
verification_hex=hex(decimal_number)
print(hex_number,verification_hex)  
hex_list=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
my_hex = ""
flag = True
while flag==True:
    my_hex = hex_list[int(decimal_number%16)] + str(my_hex)
    decimal_number=decimal_number//16
    if decimal_number==0:
        flag=False
print('0x'+ my_hex)
