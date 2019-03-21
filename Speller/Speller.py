import sys
import time
from collections import Counter
start_time = time.time()

def load1():
    if len(sys.argv) != 3:
        print("Введіть шлях до словника та файлу")
        exit(1)

    file_name = str(sys.argv[1])

    return file_name




def load2():

    dictionar = str(sys.argv[2])

    return dictionar


class Alice:
    def __init__(self, file_name, dictionar, dictin = ""):
        self.file = file_name
        self.dictionar = dictionar
        self.dictin = dictin

    def clear_text(self):
        file = open(self.file, "r")
        word = file.read()
        words = word.replace(",", "").replace(".", "").replace("?", "").replace("!", "")\
            .replace("'s", "").replace(":", "").replace(";", "").replace('"', "").replace("'", "")\
            .replace("-", "").replace("(", "").replace(")","")\
            .replace("[", "").replace("]", "").replace("*", "")
        words = words.lower().split()
        file.close()
        return words

    def abort(self, words):
        for i in words:
            if not i.isalpha():

                words.remove(i)

        return words


    def check(self, wordss):
        reads = open(self.dictionar, "r")
        write = open("alice.key", "w")
        text = reads.read()
        for word in wordss:
            if word not in text:
                write.write(word + "\n")
        reads.close()
        write.close()




alice1 = load1()
alice2 = load2()
alice = Alice(alice1, alice2)
tez = alice.abort(alice.clear_text())
alice.check(tez)


count = Counter(alice.abort(alice.clear_text()))
print(count)


finist_time = time.time()
app_time = round(finist_time - start_time, 2)
print(f"Program running {app_time}s")
