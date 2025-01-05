import time
from unitree_sdk import Robot, MovementCommand

# Подключаемся к роботу
robot = Robot()

try:
    # Устанавливаем скорость движения вперед
    command = MovementCommand()
    command.linear_velocity_x = 0.5  # Скорость по оси X (вперед)
    command.linear_velocity_y = 0.0  # Без движения в стороны
    command.angular_velocity_z = 0.0  # Без вращения

    # Отправляем команду
    robot.send_command(command)

    # Держим команду активной на 5 секунд
    time.sleep(5)

finally:
    # Останавливаем робота
    stop_command = MovementCommand()
    robot.send_command(stop_command)
