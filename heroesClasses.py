class Hero:
    """Базовый класс Hero"""

    __mage_skills = ["огненный шар", "ледяная стрела", "удар молнии"]
    __warrior_skills = ["удар в прыжке", "вой", "берсерк"]
    __ranger_skills = ["быстрая стрельба", "двойной выстрел", "скрытность"]

    def __init__(self, name):
        """Конструктор класса"""
        self._name = name
        self._my_hero_skills = []
        self._level = 0
        self._exp = 0

    def get_name(self):
        """Геттер для имени"""
        return self._name

    def get_my_hero_skills(self):
        """Геттер для списка навыков"""
        return self._my_hero_skills

    def get_level(self):
        """Геттер для уровня"""
        return self._level

    def get_exp(self):
        """Геттер для опыта"""
        return self._exp

    def get_skills(self, character_class):
        """Метод для получения списка навыков, результат зависит от выбранного класса"""
        if character_class == 'воин':
            return self.__class__.__warrior_skills
        elif character_class == 'маг':
            return self.__class__.__mage_skills
        elif character_class == 'рейнджер':
            return self.__class__.__ranger_skills
        else:
            exit("Ошибка перезапустите программу!")

    def get_new_level(self):
        """Метод для получения нового уровня и добавления навыков"""
        if self._exp >= 1000:
            self._level = 3
            self.add_skill()
        elif self._exp >= 500:
            self._level = 2
            self.add_skill()
        elif self._exp >= 200:
            self._level = 1
            self.add_skill()
        else:
            self._level = 0
        return f"Герой {self.get_name()}, теперь {self.get_level()} уровня, навыки: {', '.join(self.get_my_hero_skills())}"

    def add_exp(self, exp=0):
        """Метод для добавления опыта"""
        self._exp += exp
        new_level = self.get_new_level()
        return new_level

    def add_skill(self):
        """Метод для добавления навыков"""
        pass


class MyHero(Hero):
    """Класс MyHero - наследник класса Hero"""

    def __init__(self, name, character_class):
        """Конструктор класса"""
        super().__init__(name)
        self._character_class = character_class
        self._skill_list = self.get_skills(self._character_class)
        self._my_hero_skills = []

    def get_character_class(self):
        """Геттер для класса персонажа"""
        return self._character_class

    def get_skill_list(self):
        """Геттер для списка навыков"""
        return self._skill_list

    def add_skill(self):
        """Метод для добавления навыков"""
        for i in range(self._level - len(self._my_hero_skills)):
            while True:
                print(f"{self.get_name()}, выберите навык:", ", ".join(self._skill_list))
                skill = input().lower()
                if skill in self._skill_list:
                    self._my_hero_skills.append(skill)
                    self._skill_list.remove(skill)
                    break
                else:
                    print("НЕВЕРНЫЙ ВЫБОР!! Выберите навык:", ", ".join(self._skill_list))
        return f"Герой {self.get_name()} получает новые навыки: {', '.join(self._my_hero_skills)}"


if __name__ == '__main__':
    gimli = MyHero("Гимли", "воин")
    print(gimli.add_exp(200))
    print(gimli.add_exp(300))
    print(gimli.add_exp(500))

    print()

    legolas = MyHero("Леголас", "рейнджер")
    print(legolas.add_exp(500))
    print(legolas.add_exp(500))

    print()

    gendalf = MyHero("Гендальф", "маг")
    print(gendalf.add_exp())
