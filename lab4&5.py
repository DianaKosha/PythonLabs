import collections
import re
import urllib.request

#клас в якому знаходяться методи чи функції для
#виконання лаборатоної
class count_of_word:
    def this_one(one, adress):
        one.adress = adress #адреса сторінки
        one.got = "" #для отриманого файлу
        one.words = {} #для слів
        one.cleaner = [] #для чистого тексту

    def file_get(one):
        #отримує файли
        #з отриманового під час функції
        #this_one адреси
        result = urllib.request.urlopen(one.adress)
        one.got = result.read().decode('utf-8')

    def text_clean(one):
        one.cleaner = re.findall(r"[\w']+", one.got)

    def number_words(one):
        #рахує кількість унікальних слів
        #в отриманому файлі
        for word in one.cleaner:
            one.words[word] = one.cleaner.count(word)

    def result_main(one):
        #виводить слова по статистиці
        #в порядку за ключем - словник ключ, значення
        """Prints words statistics in ordered by key representation"""
        result_dictionary = collections.OrderedDict(sorted(one.words.items()))
        for x, y in result_dictionary.items(): print("{} : {}".format(x, y))


lab4_count =  count_of_word("https://www.wikipedia.org") #звідки береться файл записуємо
#в змінну lab4_count
#виклик ф-цій з класу
lab4_count.file_get()
lab4_count.text_clean()
lab4_count.number_words()
lab4_count.result_main()
