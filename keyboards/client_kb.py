from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

#Основные кнопк
a1 = KeyboardButton('Добавить новые параметры поиска')
a2 = KeyboardButton('Мои поисковые запросы')
a3 = KeyboardButton(' Управление подпиской ')
a4 = KeyboardButton('О боте')

#Кнопки с выбором марки авто
car0 = KeyboardButton('Любая')
car1 = KeyboardButton('LADA')
car2 = KeyboardButton('Audi')
car3 = KeyboardButton('BMW')
car4 = KeyboardButton('Chery')
car5 = KeyboardButton('Chevrolet')
car6 = KeyboardButton('Citroen')
car7 = KeyboardButton('Daewoo')
car8 = KeyboardButton('Ford')
car9 = KeyboardButton('Geely')
car10 = KeyboardButton('Haval')
car11 = KeyboardButton('Honda')
car12 = KeyboardButton('Hyundai')
car13 = KeyboardButton('Infiniti')
car14 = KeyboardButton('Jaguar')
car15 = KeyboardButton('Jeep')
car16 = KeyboardButton('Kia')
car17 = KeyboardButton('Land Rover')
car18 = KeyboardButton('Lexus')
car19 = KeyboardButton('MINI')
car20 = KeyboardButton('Mazda')
car21 = KeyboardButton('Mercedes-Benz')
car22 = KeyboardButton('Mitsubishi')
car23 = KeyboardButton('Nissan')
car24 = KeyboardButton('Opel')
car25 = KeyboardButton('Peugeot')
car26 = KeyboardButton('Porsche')
car27 = KeyboardButton('Renault')
car28 = KeyboardButton('Skoda')
car29 = KeyboardButton('Subaru')
car30 = KeyboardButton('Suzuki')
car31 = KeyboardButton('Toyota')
car32 = KeyboardButton('Volkswagen')
car33 = KeyboardButton('Volvo')
car34 = KeyboardButton('Skoda')

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(a1).insert(a2).add(a3).insert(a4)

car_kb = ReplyKeyboardMarkup(resize_keyboard=True)
car_kb.row(car0, car1, car2, car3).row(car4, car5, car6, car7).row(car8, car9, car10, car11).row(car12, car13, car14, car15).row(car16, car17, car18, car19).row(car20, car21, car22, car23).row(car24, car25, car26, car27).row(car28, car29, car30, car31).row(car32, car33, car34)