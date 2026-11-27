# Лабораторна робота №2. Створення та використання функцій, реалізація рекурсії
# Варіант: 3
# ПІБ: Сич Аріна Олегівна

# Тут має бути Ваш код

import random
from typing import List, Dict, Callable

# звичайні функції 
def calculate_area(width: float, height: float) -> float:
    return width * height

def get_canvas_type(w: float, h: float) -> str:
    if w == h:
        return "Квадрат"
    if w > h:
        return "Пейзаж"
    else:
        return "Портрет"

# функція з параметром за замовчуванням
def mix_paint(c1: str, c2: str, volume: float = 100.0) -> str:
    return f"Суміш {c1} і {c2} по {volume} мл"

# функція зі змінною кількістю аргументів
def average_volume(*volumes: float) -> float:
    if not volumes:
        return 0.0
    return sum(volumes) / len(volumes)

# додаткові функції для перевірки
def is_bright(hex_color: str) -> bool:
    # берем перші дві цифри після решітки і перевіряємо чибільші за 150
    return int(hex_color[1:3], 16) > 150

# замість множення на 2 просто додаємо 10% на запас, щоб числа були адекватні
def add_spare(vol: float) -> float:
    return round(vol * 1.1, 1)

# рекурсія
def find_max_paint(volumes: List[float], i: int = 0) -> float:
    if i == len(volumes) - 1:
        return volumes[i]
    
    max_rest = find_max_paint(volumes, i + 1)
    if volumes[i] > max_rest:
        return volumes[i]
    else:
        return max_rest

# функція вищого порядку 
def apply_to_all_paint(volumes: List[float], func: Callable[[float], float]) -> List[float]:
    result = []
    for v in volumes:
        result.append(func(v))
    return result

# генерація даних (20 елементів)
def generate_data(n: int) -> List[Dict]:
    colors = ["#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#FFFFFF", "#000000"]
    data = []
    for i in range(n):
        data.append({
            'title': f"Картина {i+1}",
            'width': random.randint(20, 100),
            'height': random.randint(20, 100),
            'paint_ml': random.randint(50, 500),
            'palette': random.sample(colors, 3) # 3 випадкові кольори
        })
    return data

# --- Головна програма ---
def main():
    print("Програма для аналізу картин")
    data = generate_data(20)
    
    while True:
        print("\n--- МЕНЮ ---")
        print("1. Розрахувати площу та тип полотна")
        print("2. Показати світлі кольори (та макс. фарби)")
        print("3. Середня витрата фарби")
        print("4. Вихід")
        
        try:
            user_choice = int(input("\nВаш вибір: "))
            
            # 1: звичайні функції
            if user_choice == 1:
                for item in data[:5]:
                    # виводимо розмір у форматі 45x60 см і тип
                    c_type = get_canvas_type(item['width'], item['height'])
                    print(f"{item['title']}: {item['width']}x{item['height']} см, {c_type}")
            
            # 2: звичайні функції, фільтр та рекурсія 
            elif user_choice == 2:
                print("\nСвітлі кольори першої картини:")
                for color in data[0]['palette']:
                    if is_bright(color):
                        print(f"{color} - світлий")
                    else:
                        print(f"{color} - темний")
                
                # тут рекурсія і фільтр
                print("\n--- Додатково ---")
                volumes = [item['paint_ml'] for item in data]
                max_paint = find_max_paint(volumes)
                print(f"Максимальна витрата фарби (рекурсія): {max_paint} мл")
                
                # філтр і звичайна функція
                large_canvases = list(filter(lambda item: calculate_area(item['width'], item['height']) > 5000, data))
                print(f"Кількість великих картин (площа > 5000): {len(large_canvases)}")
            
            # 3: *args, функція вищого порядку та map
            elif user_choice == 3:
                volumes = [item['paint_ml'] for item in data]
                avg = average_volume(*volumes)
                print(f"Середня витрата фарби: {avg:.1f} мл")
                
                print("\n--- Додатково ---")
              
                added = apply_to_all_paint(volumes[:5], add_spare)
                print(f"Фарба з запасом 10% (перші 5): {added}")
                
                areas = list(map(lambda item: calculate_area(item['width'], item['height']), data[:5]))
                print(f"Площі перших 5 картин (через map): {areas}")
                
            elif user_choice == 4:
                print("До побачення")
                break
            else:
                print("Невірний вибір, спробуй ще.")
                
        except ValueError:
            print("Помилка: треба число")

if __name__ == "__main__":
    main()()
