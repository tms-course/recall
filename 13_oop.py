####################################
############## Классы ##############
####################################
from typing import TypeVar

Sex = TypeVar('Sex')


class Human:
    """Докстрока для класса"""
    
    # Переменные класса, одинаковы для всех сущностей класса
    SEX_MALE = 'male'
    SEX_FEMALE = 'female'

    def __init__(self, name: str, sex: Sex, spouse: 'Human' = None) -> None:
        """
        :param str name: полное имя человека
        :param Sex sex: пол
        """
        # Переменные экземпляра, разнятся у каждого экземпляра
        self.__name = name
        self.__sex = sex
        self.__spouse = spouse

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def sex(self) -> Sex:
        return self.__sex

    @sex.setter
    def sex(self, sex: Sex) -> None:
        self.__sex = sex

    @property
    def spouse(self) -> 'Human':
        return self.__spouse

    @spouse.setter
    def spouse(self, person: 'Human') -> None:
        self.__spouse = person

    @staticmethod
    def can_get_married(one_person: 'Human', another_person: 'Human') -> bool:
        """Проверяет, могут ли эти люди жениться друг на друге"""
        return not (one_person is another_person \
            or one_person.sex == another_person.sex \
            or (one_person.spouse or another_person.spouse))

    @staticmethod
    def congrats(person: 'Human') -> None:
        """Выводит строку поздравления в зависимости от пола"""
        marry_line = 'женились на' if person.sex == Human.SEX_FEMALE else 'вышли замуж за'
        print(f'Ура, поздравляем! Вы {marry_line} {person.name}')

    def marry(self, person: 'Human'):
        """Делает людей супругами, если это возможно"""
        if not self.can_get_married(self, person):
            print('Это невозможно')
        else:
            self.congrats(person)
            self.spouse = person
            person.spouse = self


john = Human('John Wick', Human.SEX_MALE)
print(john.__dict__)
sandra = Human('Sandra Bullok', Human.SEX_FEMALE)
print(sandra.__dict__)
john.marry(sandra)
print(john.__dict__, sandra.__dict__)


##
## Магические методы
##
class MagicTest:
    def __call__(self, message):
        """__call__(self[, args...]) позволяет любому экземпляру класса вести себя как обычная функция"""
        print(message)
        return True

    def __enter__(self):
        """__enter__(self) — определяет начало блока контекстного менеджера, вызванного с помощью with"""
        print("entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """
        __exit__(self, exc_type, exc_value, traceback) — определяет конец блока контекстного менеджера. 
        Может использоваться для контролирования исключений, очистки, или любых действий, 
        которые должны быть выполнены после блока внутри with.
        """
        print("exiting context")

    def __getitem__(self, key):
        print(key)
        return 10

test = MagicTest()
test("Hello World")
test[10:20:"*"]

with MagicTest() as mt:
    print(mt)
