import os
from threading import Thread

#вийшло зробити пошук файлу(аудіо) по всьому комп. і використовую багатопотоковість
 
class FindThread(Thread):
    def __init__(self, currDir, fileExt):
        Thread.__init__(self)
        self.daemon = True
        self.currDir = currDir
        self.fileExt = fileExt
        self.files = []
        
    def run(self):
        #прохожусь по директорії рекурсивно
        for root, dirs, files in os.walk(self.currDir):
            for name in files:
                #отримую повне імя файлу
                fullname = os.path.join(root, name)
                #розширення
                ext = os.path.splitext(fullname)[1]
                #якщо це те, що нам треба(тобто аудіофайл)
                if ext == self.fileExt:
                    #добавляємо в список файлів
                    self.files.append(fullname)
 #впринципі швидкість пошуку без використання потоків мала,
 #а використовуючи потоки швидкість пошуку збільшується, тому ок

if __name__ == "__main__":
    finder = FindThread("/", ".mp3")
    finder.start()