# import sys
# print(sys.getsizeof("a"), sys.getsizeof("ab"), sys.getsizeof("abc"))

# # 1. Yesterday 갯수 세기
#
# f = open("yesterday.txt", 'r')
# yesterday_lyrics = f.readlines()
# f.close()
#
# contents =""
# for line in yesterday_lyrics:
#     contents = contents + line.strip() + "\n"
#
# n_of_yesterday = contents.lower().count("yesterday")
# print("Number of a Word 'Yesterday' :", n_of_yesterday)
#
# # 2. Dynamite에서 Dynamite 갯수 찾기
#
# f = open("Dynamite.txt", 'r')
# dynamite_lyrics = f.readlines()
# f.close()
#
# contents=""
# for line in dynamite_lyrics:
#     contents = contents + line.strip() + '\n'
#
# n_of_dynamite = contents.upper().count("DYNAMITE")
# print("Number of a Word 'Dynamite' :", n_of_dynamite)

# # 3. ord함수, 문자를 아스키코드로 변환
print(ord('a'))
print(ord('A'))

# # 대소문자 자동 판별, 문자만 판별
# def upper_lower_transformer_chr(alphabet):
#     if alphabet.isupper():
#         return chr(ord(alphabet) + 32)
#     else:
#         return chr(ord(alphabet) - 32)
#
# print(upper_lower_transformer_chr('a'))
#
# # 대소문자 자동 변경, string
# def upper_lower_transformer_string(string):
#     result = ""
#     for char in string:
#         if char.isupper():
#             result += chr(ord(char) + 32)
#         elif char.islower():
#             result += chr(ord(char) - 32)
#         else:
#             result += char
#     return result
#
# print(upper_lower_transformer_string("HELLO!, WORLD!"))
#
