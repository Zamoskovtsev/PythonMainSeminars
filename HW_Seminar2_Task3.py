# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для 
# проверки своего кода используйте модуль fractions.
import fractions

string_1 = str(input('Введите первую простую дробь вида X/X где "Х" любые целые числа: '))
string_2 = str(input('Введите первую простую дробь вида X/X где "Х" любые целые числа: '))
numerator_1,denumerator_1=string_1.split('/')
numerator_2,denumerator_2=string_2.split('/')
numerator_1=int(numerator_1)
denumerator_1=int(denumerator_1)
numerator_2=int(numerator_2)
denumerator_2=int(denumerator_2)

f_one = fractions.Fraction(numerator_1, denumerator_1)
f_two = fractions.Fraction(numerator_2, denumerator_2)
print('{} + {} = {}'.format(f_one, f_two, f_one + f_two)) 
print('{} - {} = {}'.format(f_one, f_two, f_one - f_two)) 
print('{} * {} = {}'.format(f_one, f_two, f_one * f_two)) 
print('{} / {} = {}'.format(f_one, f_two, f_one / f_two))

sum_num = (numerator_1 * denumerator_2) + (numerator_2 * denumerator_1)
sum_denom = denumerator_1 * denumerator_2
sum_of_fractions=str(sum_num )+'/'+str(sum_denom)
mult_fractions=str(numerator_1 *numerator_2) + '/'+ str(denumerator_1 * denumerator_2)

print(sum_of_fractions,mult_fractions)
