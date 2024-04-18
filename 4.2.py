class Bot:
    def __init__(self):
        self.commands = {}

    def add_command(self, command, func):
        self.commands[command] = func

    def handle_message(self, message):
        if message.text in self.commands:
            self.commands[message.text](message)
        else:
            for command, func in self.commands.items():
                if 'func' in func.__name__ and func(message):
                    return func(message)
            print("Command not found")

# Пример функции, которая будет вызываться по команде '/start'
def start_command(message):
    print("Hello! Welcome to the bot.")

# Пример функции, которая будет вызываться по условию, если сообщение содержит определенный текст
def contains_hello(message):
    return 'hello' in message.text.lower()

# Создание экземпляра класса бота
my_bot = Bot()

# Добавление команды '/start' и связанной с ней функции start_command
my_bot.add_command('/start', start_command)

# Добавление функции, которая будет вызываться при наличии текста "hello" в сообщении
my_bot.add_command('func contains_hello', contains_hello)

# Пример входящего сообщения
class Message:
    def __init__(self, text):
        self.text = text

# Тестирование работы бота
message1 = Message('/start')
my_bot.handle_message(message1)  # Ответ: "Hello! Welcome to the bot."

message2 = Message('Say hello!')
my_bot.handle_message(message2)  # Ответ: "Command not found"

message3 = Message('Hello, bot!')
my_bot.handle_message(message3)  # Ответ: В зависимости от предпочтений, функция выполнит действие для текста содержащего "hello"
