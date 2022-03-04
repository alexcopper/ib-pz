print("Шифрование цезаря")
key, string = int(input('Введите длину сдвига: '))%33, input('Введите строку для шифрования: ')
answer = 0
while answer !=1 and answer != 2:
    answer = int(input("1 - зашифровать текст, 2 - расшифровать: "))
if(answer==2): key=-key
[print(chr(ord(i)+key), end='') if i.isalpha() else print(i, end = '') for i in string]