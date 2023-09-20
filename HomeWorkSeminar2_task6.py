#бакномат
def get_summ_money(operation:str) -> float:
    money=float(input(f'Введите сумму {operation} кратно 50: '))
    if money%50 != 0:
        money=0
    return money

def replenishment(money: float,count_r:int,gross_m:float) -> float:
    gross_m=gross_m+money
    if count_r==3:
        gross_m=gross_m*1.03
    return gross_m
    
def withdrawal(money: float,gross_m:float) -> float:
    percent=money*0.015
    if percent<30:
        percent=30
    if percent>600:
        percent=600
    if gross_m<(money+percent):
        print(f'Снятие суммы {money} невозможно, недостаточно средств')
    else:
        gross_m=gross_m-money-percent
    return gross_m

def luxury(gross_m:float) ->float:
    if gross_m>=5000000:
        gross_m=gross_m*0.9
    return gross_m

import os
gross_money = 0
count_r=0
choise=0
while choise!=1:
    print('Введите 1 для выхода из банкомата')
    print('Введите 2 пополнения')
    print("Введите 3 снятия")
    choise = int(input('Ваш выбор: '))
    if choise == 1:
        print('Вы выбрали выход')
        False
    if choise == 2:
        if count_r<=3:
            count_r+=1
        else:
            count_r=0
        print("выбрано пополнение")
        gross_money=replenishment(get_summ_money('пополнения'),count_r,gross_money)
        gross_money=luxury(gross_money)
        print(f'Сумма на счете {gross_money}')     
    if choise == 3:
        print("выбрано снятие")
        gross_money=withdrawal(get_summ_money('снятия'),gross_money) 
        gross_money=luxury(gross_money)
        print(f'Сумма на счете {gross_money}')
