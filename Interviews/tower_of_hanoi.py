'''
Implementation of Towe of hanoi
'''

def TOH(n, a, b, c):
    if n == 1:
        print(f'Move Disk 1 from {a} to {c}')
        return
    TOH(n-1, a,c,b)
    print(f'Move Disk {n} from {a} to {c}')
    TOH(n-1,b,a,c)

TOH(3,'A','B','C')