import string

class Cesar:
    def __init__(self, word, key):
        self.word = word
        self.key = key

    def get_shifr(self):
        shifrword = ""
        self.key = self.key%26
        for i in self.word:
            c = ord(i)
            if i in string.ascii_letters:
                ci = (c + self.key)
                if 97<=ci<=122 or 65 <= ci <= 90:
                    shif = chr(ci)
                else:
                    ci = ci-26
                    shif = chr(ci)
            else:
                shif = chr(c)
            shifrword += shif
        return shifrword

shifr = Cesar(input("Введіть слово яке потрібно зашифрувати>> "), int(input("Введіть ключ>> ")))
print(shifr.get_shifr())



