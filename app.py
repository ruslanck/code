import random
import os

class EcoGame:
    def __init__(self):
        self.pollution = random.randint(3, 6)
        self.food = random.randint(4, 7)
        self.lives = 3
        self.score = 0
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def display_bar(self, value, max_value, label):
        filled = value
        empty = max_value - value
        bar = "[" + "#" * filled + "_" * empty + "]"
        return f"{label}: {bar}"
    
    def show_status(self):
        print("статистика")
        print(self.display_bar(self.pollution, 10, "Загрязнение"))
        print(self.display_bar(self.food, 10, "Еда"))
        print(self.display_bar(self.lives, 3, "Жизни"))
        print(f"Счет: {self.score}")
    
    def check_game_over(self):
        died = False
        
        if self.pollution >= 8:
            self.lives -= 1
            self.pollution = 5
            died = True
            print("\nзагрязнение высокое! -1 жизнь!")
        
        if self.food <= 0:
            self.lives -= 1
            self.food = 5
            died = True
            print("\nеда закончилась -1 жизнь!")
        
        self.pollution = max(1, min(10, self.pollution))
        self.food = max(1, min(10, self.food))
        
        if self.lives <= 0:
            return True
        
        return False
    

    
    def play_round(self):
        QUESTIONS = [
            {
                'question': 'Что делать с мусором?',
                'options': [
                    {'text': 'Выбросить в реку', 'pollution': 2, 'food': 0},
                    {'text': 'Отнести на переработку', 'pollution': -1, 'food': 0}
                ]
            },
            {
                'question': 'Как добраться до работы?',
                'options': [
                    {'text': 'Поехать на машине', 'pollution': 1, 'food': -1},
                    {'text': 'Поехать на велосипеде', 'pollution': -1, 'food': 0}
                ]
            },
            {
                'question': 'Где взять еду?',
                'options': [
                    {'text': 'Купить в магазине', 'pollution': 1, 'food': 2},
                    {'text': 'Вырастить самому', 'pollution': -1, 'food': 1}
                ]
            },
            {
                'question': 'Построить что-то?',
                'options': [
                    {'text': 'Построить завод', 'pollution': 3, 'food': 2},
                    {'text': 'Построить парк', 'pollution': -2, 'food': 1}
                ]
            },
            {
                'question': 'Чем топить печь?',
                'options': [
                    {'text': 'Дровами из леса', 'pollution': 2, 'food': 1},
                    {'text': 'Солнечными батареями', 'pollution': -1, 'food': -1}
                ]
            },
            {
                'question': 'Что делать с отходами?',
                'options': [
                    {'text': 'Слить в реку', 'pollution': 2, 'food': 0},
                    {'text': 'Очистить на станции', 'pollution': -1, 'food': -1}
                ]
            },
            {
                'question': 'Новая упаковка?',
                'options': [
                    {'text': 'Купить пластик', 'pollution': 1, 'food': -1},
                    {'text': 'Использовать бумагу', 'pollution': 0, 'food': -1}
                ]
            },
            {
                'question': 'Что посадить?',
                'options': [
                    {'text': 'Овощи для еды', 'pollution': 0, 'food': 3},
                    {'text': 'Деревья для леса', 'pollution': -2, 'food': 1}
                ]
             },
        #     {
        #         'question': 'Что ?',
        #         'options': [
        #             {'text': 'Овощи для еды', 'pollution': 0, 'food': 3},
        #             {'text': 'Деревья для леса', 'pollution': -2, 'food': 1}
        #         ]
        #     },
        #     {
        #         'question': 'Что посадить?',
        #         'options': [
        #             {'text': 'Овощи для еды', 'pollution': 0, 'food': 3},
        #             {'text': 'Деревья для леса', 'pollution': -2, 'food': 1}
        #         ]
        #     },
        #     {
        #         'question': 'Что посадить?',
        #         'options': [
        #             {'text': 'Овощи для еды', 'pollution': 0, 'food': 3},
        #             {'text': 'Деревья для леса', 'pollution': -2, 'food': 1}
        #         ]
        #     }
        ]

        
        question = random.choice(QUESTIONS)
        
        print(question['question'])
        
        for i, option in enumerate(question['options'], 1):
            print(f"{i}. {option['text']}")
        
        while True:
            try:
                choice = int(input("\nТвой выбор (1-2): "))
                if choice in [1, 2]:
                    break
                else:
                    print("Выбери 1 или 2!")
            except ValueError:
                print("Введи число 1 или 2!")
        
        chosen = question['options'][choice - 1]
        
        self.pollution += chosen['pollution']
        self.food += chosen['food']
        self.score += 1
        
        print("\n" + "-"*40)
        print(f"Ты выбрал: {chosen['text']}")
        if chosen['pollution'] != 0:
            sign = "+" if chosen['pollution'] > 0 else ""
            print(f"Загрязнение: {sign}{chosen['pollution']}")
        if chosen['food'] != 0:
            sign = "+" if chosen['food'] > 0 else ""
            print(f"Еда: {sign}{chosen['food']}")
        print("-"*40)
    
    def run(self):
        self.clear_screen()
        input("\nПравила:\n- Отвечай на вопросы, выбирая 1 или 2\n- Каждый выбор влияет на природу и еду\n- У тебя 3 жизни\n- Загрязнение >=8 или еда <=0 = минус жизнь\n- Набери как можно больше очков\n\nНажми Enter, чтобы начать...")
        
        while self.lives > 0:
            self.clear_screen()
            self.show_status()
            self.play_round()
            
            if self.check_game_over():
                break
            
            input("\nНажми Enter для следующего вопроса...")
        
        self.clear_screen()
        print("="*40)
        print("ИГРА ОКОНЧЕНА")
        print("="*40)
        self.show_status()
        print(f"\nТвой итоговый счет: {self.score}")
        print("\nСпасибо за игру!")
        print("="*40)

if __name__ == "__main__":
    game = EcoGame()
    game.run()
    
    while True:
        play_again = input("\nХочешь сыграть еще? (да/нет): ").lower()
        if play_again in ['да', 'yes', 'y', 'д']:
            game = EcoGame()
            game.run()
        else:
            print("\nДо свидания!")
            break