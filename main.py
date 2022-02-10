

lrus = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
brus = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
        'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
lend = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z']
bend = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z']

def encryptCaesar(msg, shift):
        ret = ""
        for x in msg:
                if x in lrus:
                        ind = lrus.index(x)
                        ret += lrus[(ind + shift) % len(lrus)]
                elif x in brus:
                        ind = brus.index(x)
                        ret += brus[(ind + shift) % len(lrus)]
                elif x in lend:
                        ind = lend.index(x)
                        ret += lend[(ind + shift) % len(lend)]
                elif x in bend:
                        ind = bend.index(x)
                        ret += bend[(ind + shift) % len(lend)]
                else:
                        ret += x

        return ret


def decryptCaesar(msg, shift):
        ret = ""
        for x in msg:
                if x in lrus:
                        ind = lrus.index(x)
                        ret += lrus[(ind - shift) % len(lrus)]
                elif x in brus:
                        ind = brus.index(x)
                        ret += brus[(ind - shift) % len(lrus)]
                elif x in lend:
                        ind = lend.index(x)
                        ret += lend[(ind - shift) % len(lend)]
                elif x in bend:
                        ind = bend.index(x)
                        ret += bend[(ind - shift) % len(lend)]
                else:
                        ret += x


        return ret

def dec(msg):
        q = open('abc.txt', 'w', encoding='utf-8')
        ret = ""
        shift = 0
        for shift in range(len(lrus)):
                for x in msg:
                        if x in lrus:
                                ind = lrus.index(x)
                                ret += lrus[(ind - shift) % len(lrus)]
                        elif x in brus:
                                ind = brus.index(x)
                                ret += brus[(ind - shift) % len(lrus)]
                        elif x in lend:
                                ind = lend.index(x)
                                ret += lend[(ind - shift) % len(lend)]
                        elif x in bend:
                                ind = bend.index(x)
                                ret += bend[(ind - shift) % len(lend)]
                        else:
                                ret += x

                q.write('ключ = %s\n %s \n' % (shift, ret))
                ret = ""
        return ret

f = open('a.txt', encoding='utf-8')
b = open('ab.txt', 'w', encoding='utf-8')

a = f.read()
c = encryptCaesar(a, 10)
print(encryptCaesar(a, 10))
print(decryptCaesar(c, 10))
s = dec(c)
b.write(c)

