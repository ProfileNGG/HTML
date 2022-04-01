f=open('foo.txt','w')
f.write('This is line one.\nThis is line two.\nPython is great!\n')
f.close

f=open('foo.txt','br')
print('파일 포인터 위치: ',f.tell())
contents1=f.read()

print('파일 포인터 위치: ',f.tell())
contents2 =f.read()
print('contents2: [{}]\n'.format(contents2))

f.seek(0)
print('파일 포인터 위치: ',f.tell())
contents3 =f.read()
print('contents3: [{}]\n'.format(contents3))
