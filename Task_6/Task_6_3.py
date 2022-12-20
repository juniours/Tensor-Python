def xor(string, key):
    len_key = len(key)
    encoded = []

    for i in range(0, len(string)):
        encoded.append(string[i] ^ key[i % len_key])
    return bytes(encoded)


filename, key = input("Введите имя файла с расширением (например, text.txt) и ключ шифрования ").split()
key_b = key.encode('utf-8')
words_b = []
with open(filename) as f:
    codew = []
    for line in f:
        words = line.split()
        
        for i in range(len(words)):
            words_b.append(words[i].encode('utf-8'))
            words_b.append(b' ')

print("Исходный текст: ", words)
print("Текст в виде байт-строк: " + str(words_b)[1:-1])

res_b = []
for word in words_b:
    res_b.append(xor(word, key_b))
print("Зашифрованный текст в виде байт-строк: " + str(res_b)[1:-1])

res = []
for r in res_b:
    if r != b'I':
        res.append(xor(r, key_b).decode('utf-8'))
print("Итоговый текст в раскодированном виде: " + str(res)[1:-1])