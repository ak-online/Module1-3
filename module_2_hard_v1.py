def get_password(n):
    passdict = {}
    passdict.update({3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645, 10: 141923283746, 11: 11029384756})
    passdict.update({12: 12131511124210394857, 13: 112211310495867, 14: 1611325212343114105968,})
    passdict.update({15: 1214114232133124115106978,16: 1317115262143531341251161079, 17: 11621531441351261171089})
    passdict.update({18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910})
    passdict.update({20: 13141911923282183731746416515614713812911})
    passw = passdict.get(n)
    return passw

while True:
    n = int(input('Перввй шифр :'))
    if n >2 and n <21:
        break
    else:
        continue


pair1 = list(range(1, n))
pair2 = list(range(1, n))
finalpairs = []
res = ''

for i in pair1:
    for j in pair2:
        c1 = i
        c2 = j
        if c1 >= c2:
            #print('c1',c1, 'c2', c2 )
            continue
        else:
            delenie = n % (c1 + c2)
            #print(delenie)
            if delenie == 0:
                finalpairs.append([c1, c2])
                res = res + str(c1) + str(c2)
print('Пары чисел', *finalpairs)
if int(res) == get_password(n):
    print('Ура!')