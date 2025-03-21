# a = input().lower()
# t = str.maketrans('', '', '!,.?;:#$%^&*()')
# a = a.translate(t).split()
# b = {}
# for i in a:
#     b[i] = b.get(i, 0) + 1
# fk = [key for key, value in b.items() if value > 2 ]
# fs = [s for s in fk if len(s) >= 5 and len(set(s)) >=4]
# fs.sort()
# print('\n'.join(fs))


words = input().lower().translate(str.maketrans('', '', '!,.?;:#$%^&*()')).split()
fs = sorted(word for word in set(words) if words.count(word) > 2 and len(word) >= 5 and len(set(word)) >= 4)
print('\n'.join(fs))