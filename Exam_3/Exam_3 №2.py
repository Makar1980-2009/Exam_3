 # Напишите функцию, которая возвращает True, если введенный текст читается одинаково
 # слева-направо и справа-налево. Иначе – False.

a = input('Введите текст: ')

def Palindrome(a):
    if a[::-1] == a[:]:
        return True
    else:
        return False
print(Palindrome(a))


