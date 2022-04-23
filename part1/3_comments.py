# В данном коде все прокомментировано как надо,
# но слишком избыточно.
# Избавьтесь от комментариев, изменив имена переменных,
# чтобы было понятно, за что эти переменные отвечают
# и что происходит и без комментариев
class Unit:
    # def mvmntobjbfld(self, field, feld_1_param, field_2_param, d, fl, cr, points_per_action = 1)
    def move(self, field, x_coord: int, y_coord: int, direction, is_fly: bool, crawl: bool, speed: int = 1):
        """Функция реализует перемещение юнита по полю"""
        if is_fly and crawl:
            raise ValueError('Рожденный ползать летать не должен!')

        if is_fly:
            speed *= 1.2
        if crawl:
            speed *= 0.5

        if direction == 'UP':
            new_y = y_coord + speed
            new_x = x_coord
        elif direction == 'DOWN':
            new_y = y_coord - speed
            new_x = x_coord
        elif direction == 'LEFT':
            new_y = y_coord
            new_x = x_coord - speed
        elif direction == 'RIGTH':
            new_y = y_coord
            new_x = x_coord + speed

        field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
