

lrus = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
brus = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
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
        q = open('decoded_b_f.txt', 'w', encoding='utf-8')
        ret = ""
        shift = 1
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

                q.write('Shift = %s\n %s \n' % (shift, ret))
                ret = ""
        return ret


print("Choose a type of the process:\n1. Encyption\n2. Decryption\n3. Decryption (brute force attack)")
type = int(input())
if type == 1:
        f = open('sample.txt', encoding='utf-8')
        b = open('encoded.txt', 'w', encoding='utf-8')
        k = open('shift.txt', encoding='utf-8')
        sh = int(k.read())
        a = f.read()
        c = encryptCaesar(a, sh)
        b.write(c)
elif type == 2:
        f = open('encoded.txt', encoding='utf-8')
        b = open('decoded.txt', 'w', encoding='utf-8')
        k = open('shift.txt', encoding='utf-8')
        sh = int(k.read())
        a = f.read()
        c = decryptCaesar(a, sh)
        b.write(c)
elif type == 3:
        f = open('encoded.txt', encoding='utf-8')
        a = f.read()
        s = dec(a)
else:
        print('Oops! Start again')
