def stras(n):
    for i in range(1, n, 2):
        print(" " * n + i * "*")
        n -= 1


stras(8)

dis = {'rno': '1', 'name': 'naynesh', 'city': 'pashte'}
print(dis.values())
dis1 = dis.popitem('rno')
print(dis1.values())
dis1 = dis.copy()
print(dis1.keys())
print(dis1.keys())
