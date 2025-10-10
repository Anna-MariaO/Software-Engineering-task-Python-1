def is_palindrome(text):
    text = ''.join(text.lower().split())
    return text == text[::-1]

text = input("Введите строку: ")

if is_palindrome(text):
    print("Строка является палиндромом")
else:
    print("Строка НЕ является палиндромом")