'''
print('pam' + "pam" + 'pam') 
print('hello, ' + 'buddy!') 
print("my uncle" + 'true man')
'''


#print('*' * 15) # ���������� ��� ��������� ���������
#print('kekw' * 3) # �������� ��������: ������� �� ����������, ����� ���������� � ����
#print('lul ' * 3) # � ����� ������� �����, ������ ��� � ����� ������ ������� ����
#print('Hello! ' * 2 + 'Buddy!') # ����� �������� ��������� ��������� �� �����


#print('-' + 'O-' * 40) 

'''
stars = '*' * 5
print((stars + ' ') * 3)
'''

'''
n = int(input())
s = '*'
print(s * n)  
'''

'''
n = int(input())
m = int(input())

for i in range(m):
    if i != m - 1:
        print('r' * n + 'u', end = '')
    else:
        print('r' * n + 'u')
'''

#print(input())

'''
a = input()
b = input()
print(a, ' and ', b, ' are ', a, b, 'together', sep = '')
'''

'''
a = int('5')
print(a + 1)
b = str(15)
print(b * 2) 
'''

'''
a = int(input())
b = int(input())
print(int(str(a) + str(b)) - a - b)
'''

'''
s = input()
if s == 'Hello!':
  print('Hello!')
else:
  print('I dont understand you')
  '''

'''
a = input()
b = input()
c = input()

if a == c or b == c or a + b == c or b + a == c:
    print('YES')
else:
	print('NO')
    '''

'''
n = int(input())
t = input()
s = 0

for i in range(n):
    a = input()
    if a == t:
        s += 1

print(s)
'''

'''
n = int(input())
s = ''

for i in range(n):
    a = input()
    s += a + ' '

print(s)
'''
