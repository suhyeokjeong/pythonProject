# a = [1,2,3,4,5]
# a.append(10)
# a.append(20)
#
# print(a)
#
# a.pop()
# print(a)
# a.pop()
# print(a)

# 가사 주고 받기
# def chr_to_ord(chr_original):
#     lyrics_ord = []
#
#     for word in chr_original:
#         word_ord = ""
#         for chr in word:
#             word_ord += str(ord(chr)) + " "
#         lyrics_ord.append(word_ord)
#
#     return lyrics_ord
#
# def ord_to_chr(contents_2):
#     chr_lyrics = []
#
#     for line in contents_2:
#         chr_word = line.split()
#         chr_abc = ""
#         for ord in chr_word:
#             chr_line = chr(int(ord))
#             chr_abc += chr_line
#         chr_lyrics.append(chr_abc)
#
#     return chr_lyrics
#
# f = open("yesterday.txt", 'r')
# yesterday_lyrics = f.readlines()
# f.close()
#
# contents =""
# for line in yesterday_lyrics:
#     contents = contents + line.strip() + "\n"
#
# # print(contents, '\n')

#
# ord_lyrics = []
# for alphabet in contents:
#     ord_lyrics.append(ord(alphabet))
# # print(ord_lyrics, '\n')

# # 파일 읽기
# f = open("newFile", 'w')
# f.write(str(ord_lyrics))
# f.close()
#
# f = open("newFile", 'r')
# newFile_lyrics = f.readlines()
# f.close()
#
# ascii_lyrics =""
# for line in newFile_lyrics:
#     ascii_lyrics = ascii_lyrics + line.strip() + "\n"
#
# print(ascii_lyrics)
# print(type(ascii_lyrics))
# print(ascii_lyrics.split(','))

#
# for ord_num in ascii_lyrics:

# for line in newFile_lyrics:
#     contents =
# print(contents_2)

# ascii_lyrics = ""
# for number in ord_lyrics:
#     ascii_lyrics += chr(number)
#
# print(ascii_lyrics, '\n')


# lyrics_in_list = contents.split()
# print(lyrics_in_list)
#
# contents_2 = chr_to_ord(lyrics_in_list)
# print(contents_2)
#
# answer = ord_to_chr(contents_2)
# print(answer)

# 속성, 기능, 메서드, 함수

# f = open("yesterday.txt", 'r')
# yesterday_lyrics = f.readlines()
# f.close()
#
# contents =""
# for line in yesterday_lyrics:
#     contents = contents + line.strip() + "\n"
#
# print(contents)
#
# ord_lyrics = []
# for alphabet in contents:
#     ord_lyrics.append(ord(alphabet))
# print(ord_lyrics)
#
# ascii_lyrics = ""
# for number in ord_lyrics:
#     ascii_lyrics += chr(number)
#
# print(ascii_lyrics)

f = open("yesterday.txt", 'r')
yesterday_lyrics = f.readlines()
f.close()

original =""
for line in yesterday_lyrics:
    original = original + line.strip() + "\n"

print(original)

ord_version = []
for alphabet in original:
    ord_version.append(ord(alphabet))
print(ord_version)

chr_version = ""
for number in ord_version:
    chr_version += chr(number)

print(chr_version)