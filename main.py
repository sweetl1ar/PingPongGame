import turtle  # Модуль графики
from random import choice, randint

"""Создание окна"""
window = turtle.Screen()  # Создание окна
window.tracer(1)
window.title("Ping-Pong")  # Название окна
window.setup(width=1.0, height=1.0)  # Растягивание на полную ширину и высоту экрана
window.bgcolor("black")  # Цвет фона окна

"""
Отрисовка рабочей части
Поля рабочей зоны (500, 300), (-500, -300), (500, -300), (-500, 300)
Длина средней линии - 600 px, делим линию на 25 отрезков по 24 px пунктиром, нумерация с 0, нечетные не рисуются
"""
border = turtle.Turtle()  # Наследование от класса Turtle, отрисовка границы
border.speed(0)  # 0 - Убирает скорость отрисовки
border.color("green")  # Цвет границы
border.begin_fill()  # Начало заливки границы
border.goto(-500, 300)  # Идем в верхний левый угол
border.goto(500, 300)  # Идем в верхний правый угол
border.goto(500, -300)  # Идем в нижний левый угол
border.goto(-500, -300)  # Идем в нижний левый угол
border.goto(-500, 300)  # Идем в верхний левый угол
border.end_fill()  # Конец заливки границы

border.goto(0, 300)  # Начало середины стола(верх)
border.color("white")  # Белый цвет границы линии середины
border.setheading(270)  # Маркер будет идти не горизонтально, а вертикально(угол)
for i in range(25):  # Для отрисовки пунктира
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()  # Подъем маркера вверх, чтобы тот не оставлял следов
        border.forward(24)
        border.down()  # Маркер опускается
border.hideturtle()  # Выключает отображение рисующей "черепашки"(стрелочка)
# border.goto(0, -300)  # Конец середины стола(низ)

"""
Отрисовка ракеток, ракетки на пикселях 450 и -450
функции для движения ракеток
"""
# Левая ракетка
rocket_a = turtle.Turtle()  # Первая (левая) ракетка
rocket_a.color("white")
rocket_a.shape("square")  # Фигура квадрат
rocket_a.shapesize(stretch_len=1, stretch_wid=5)  # Размеры
rocket_a.penup()  # Отключение следов при перемещении
rocket_a.goto(-450, 0)  # Перемещение на координату 450
# Правая ракетка
rocket_b = turtle.Turtle()  # Вторая (правая) ракетка
rocket_b.color("white")
rocket_b.shape("square")
rocket_b.shapesize(stretch_len=1, stretch_wid=5)
rocket_b.penup()
rocket_b.goto(450, 0)

"""Создание счёта"""
FONT = ("Arial", 44)
score_a = 0
s1 = turtle.Turtle(visible=False)
s1.penup()
s1.color("white")
s1.setposition(-200, 300)
s1.write(score_a, font=FONT)

score_b = 0
s2 = turtle.Turtle(visible=False)
s2.penup()
s2.color("white")
s2.setposition(200, 300)
s2.write(score_a, font=FONT)


def move_up_left():
    """Функция обработки клавиш, движение вверх"""
    y = rocket_a.ycor() + 10
    if y > 250:
        y = 250
    rocket_a.sety(y)


def move_down_left():
    """Функция обработки клавиш, движение вниз"""
    y = rocket_a.ycor() - 10
    if y < -250:
        y = -250
    rocket_a.sety(y)


def move_up_right():
    """Функция обработки клавиш, движение вверх"""
    y = rocket_b.ycor() + 10
    if y > 250:
        y = 250
    rocket_b.sety(y)


def move_down_right():
    """Функция обработки клавиш, движение вниз"""
    y = rocket_b.ycor() - 10
    if y < -250:
        y = -250
    rocket_b.sety(y)


"""Отрисовка и работа с мячом"""
ball = turtle.Turtle()  # Создание мяча
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.dx = 3  # скорость по x
ball.dy = 3  # скорость по y
ball.penup()

"""Вызов окна и работа с ним"""
window.listen()  # реагирование на разные события
window.onkeypress(move_up_left, "w")  # реагирование на клавиши, двигаемся вверх левая
window.onkeypress(move_down_left, "s")  # реагирование на клавиши, двигаемся вниз левая
window.onkeypress(move_up_right, "o")  # реагирование на клавиши, двигаемся вверх правая
window.onkeypress(move_down_right, "l")  # реагирование на клавиши, двигаемся вниз правая

while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() >= 290:
        ball.dy = -ball.dy

    if ball.ycor() <= -290:
        ball.dy = -ball.dy

    if ball.xcor() >= 490:
        score_b += 1
        s2.clear()
        s2.write(score_b, font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if ball.xcor() <= -490:
        score_a += 1
        s1.clear()
        s1.write(score_a, font=FONT)
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

    if rocket_b.ycor() - 50 <= ball.ycor() <= rocket_b.ycor() + 50 \
            and rocket_b.xcor() - 5 <= ball.xcor() <= rocket_b.xcor() + 5:
        ball.dx = -ball.dx

    if rocket_a.ycor() - 50 <= ball.ycor() <= rocket_a.ycor() + 50 \
            and rocket_a.xcor() - 5 <= ball.xcor() <= rocket_a.xcor() + 5:
        ball.dx = -ball.dx

window.mainloop()  # Бесконечный вызов окна
