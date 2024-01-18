class Room:
    def __init__(self, room_number, room_type, price, status="вільно"):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.status = status  # "вільно" або "заброньовано"

class Hotel:
    def __init__(self):
        self.rooms = []  # список для зберігання об'єктів кімнат

    def add_room(self, room):
        self.rooms.append(room)

    def display_available_rooms(self):
        available_rooms = [room for room in self.rooms if room.status == "вільно"]
        if available_rooms:
            print("Доступні кімнати:")
            for room in available_rooms:
                print(f"Номер: {room.room_number}, Тип: {room.room_type}, Ціна: {room.price}, Статус: {room.status}")
        else:
            print("Усі кімнати заброньовані.")

    def change_reservation_status(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.status == "вільно":
                    room.status = "заброньовано"
                    print(f"Кімнату {room_number} заброньовано.")
                else:
                    room.status = "вільно"
                    print(f"Статус бронювання кімнати {room_number} змінено на вільно.")
                return True
        print(f"Кімнату {room_number} не знайдено.")
        return False

# Створення готелю та взаємодія з користувачем
hotel = Hotel()

while True:
    print("\n1. Додати кімнату")
    print("2. Переглянути доступні кімнати")
    print("3. Змінити статус бронювання кімнати")
    print("4. Вийти")
    
    choice = input("Виберіть опцію: ")

    if choice == "1":
        room_number = int(input("Введіть номер кімнати: "))
        room_type = input("Введіть тип кімнати: ")
        price = float(input("Введіть ціну за ніч: "))
        new_room = Room(room_number, room_type, price)
        hotel.add_room(new_room)
        print(f"Кімната {room_number} додана.")
    elif choice == "2":
        hotel.display_available_rooms()
    elif choice == "3":
        room_to_change_status = int(input("Введіть номер кімнати для зміни статусу бронювання: "))
        hotel.change_reservation_status(room_to_change_status)
    elif choice == "4":
        break
    else:
        print("Невірний вибір. Спробуйте ще раз.")
