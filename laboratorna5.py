#код пайтону, що демонструє solid principles

import re

#Наступний клас CheckInfo представляє єдиний принцип відповідальності
class CheckInfo(object):
    def checkingMail(self, mail):
        return re.match('[^@]+@[^@]+\.[^@]+', mail)

    def checkingAge(self, age):
        return isinstance(age, int)

    def checkingLength(self, name):
        return len(name) <= 15

# Наступний клас розширений AdvancedCheckInfo представляє поганий приклад !
# принципів заміщення Liskova та відкритих / закритих принципів

# У цьому випадку у нас є новий клас AdvancedCheckInfo, який успадковується від класу CheckInfo:
# checkingMail метод з класу AdvancedCheckInfo переважає
# checkingMail метод з класу CheckInfo, але не використовує його до кінця.

class AdvancedCheckInfo(CheckInfo):
    def __init__(self):
        self.usableDomains = ['.com', '.net', '.edu']

    def checkingMail(self, mail):
        pattern = re.search(r'[^@]+@[^@]+(\.[^@]+)', mail)
        if pattern:
            if pattern.group(1) in self.usableDomains:
                return True


class info_of_users_plus(CheckInfo):
    def __init__(self):
        super(info_of_users_plus, self).__init__()
        self.identification_of_user = 0
        self.information_about_user = {}

    def information_about_user_plus(self, name, age, mail):
        self.identification_of_user += 1

        if self.checkingAge(age) and self.checkingMail(mail) and self.checkingLength(name):
            self.information_about_user.update({
                self.identification_of_user: {
                    'name': name,
                    'mail': mail,
                    'age': age
                }})

    def information_getting(self):
        return self.information_about_user

    # наступний метод реалізує delete_first_information_about_user представляє Interface Segregation Principle
    def delete_first_information_about_user(self):
        del self.information_about_user[1]
        return self.information_about_user


users = info_of_users_plus()

users.information_about_user_plus('Lilia', 28, 'liliapodlesna@gmail.com')
users.information_about_user_plus('Diana', 21, 'dianakoshtura@gmail.com')
users.information_about_user_plus('Artem', '2', 'polyalovartem@gmail.com')
users.information_about_user_plus('Oleg', 21, 'olegsoprun@gmail.com')

print(users.information_getting())
# users.delete_first_information_about_user()
