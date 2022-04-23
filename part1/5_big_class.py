# в задании представлен один класс который нужно разбить на 4
# Воин      - Warrior
# Лекарь    - Healer
# Дерево    - Tree
# Ловушка   - Trap

# Для решения этой задачи не используйте наследование

class Warrior:
    """Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю"""

    def attack(self):
        pass

    def defense(self):
        pass

    def move(self):
        pass


class Healer:
    """Лекарь может защищаться, лечить воина и панически спасаться бегством"""

    def defense(self):
        pass

    def move(self):
        pass

    def heal(self):
        pass


class Tree:
    """Дерево может защищаться (попробуй разруби сходу) и гореть в огне"""

    def defense(self):
        pass

    def on_fire(self):
        pass


class Trap:
    """Ловушка не может ничего кроме как атаковать того, кто на нее наступит"""

    def attack(self):
        pass


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    trap = Trap()
