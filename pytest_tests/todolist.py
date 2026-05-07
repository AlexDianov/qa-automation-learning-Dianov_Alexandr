class Task:
    def __init__(self, title: str, done: bool = False ):
        self.title = title
        self.done = done

    def __str__(self) -> str:
        status = '[x]' if self.done else '[ ]'
        return f'{status} {self.title}'


class TodoList:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, title: str) -> None:
        title = title.strip()
        if not title:
            print('Нельзя добавить пустую задачу!')
            return
        self.tasks.append(Task(title))
        print('Задача добавлена')

    def show_task(self) -> None:
        if not self.tasks:
            print('Список задач пуст.')
            print()
            return
        print('\nТекущий список задач:')
        for i, task in enumerate(self.tasks, start = 1):
            print(f'{i}. {task}')
        print()

    def complete_task(self, index: int) -> None:
        if not self.tasks:
            print('Невозможно отметить выполнение. Список задач пуст.')
            return
        if not 1 <= index <= len(self.tasks):
            print(f'Нет задачи с номером {index}. Диапазон: 1..{len(self.tasks)}')
            return
        task = self.tasks[index - 1]
        if task.done:
            print('Эта задача уже выполнена.')
        else:
            task.done = True
            print(f"Задача '{task.title}' отмечена как выполненная.")

    def delete_task(self, index: int) ->None:
        if not self.tasks:
            print('Нечего удалять, список задач пуст.')
            return
        if not 1 <=index <= len(self.tasks):
            print(f'Нет задачи с номером {index}. Допустимый диапазон: 1..{len(self.tasks)}')
            return
        task = self.tasks.pop(index - 1 )
        print(f"Задача '{task.title}' удалена")

    def show_stats(self) -> None:
        total = len(self.tasks)
        done = sum(1 for t in self.tasks if t.done)
        left = total - done
        print(f'Всего задач: {total}')
        print(f'Выполнено: {done}')
        print(f'Осталось: {left}')

def main():
    todo = TodoList()
    while True:
        print("=== Список задач ===")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Отметить задачу выполненной")
        print("4. Удалить задачу")
        print("5. Показать статистику")
        print("0. Выход")
        choice = input('Выберите действие: ').strip()
        print()
        match choice:
            case '1':
                title = input('Введите текст задачи - ')
                todo.add_task(title)
                print()
            case '2':
                todo.show_task()
            case '3':
                todo.show_task()
                if not todo.tasks:
                    continue
                s = input('Введите номер задачи для отметки: ').strip()
                try:
                    idx = int(s)
                    todo.complete_task(idx)
                except ValueError:
                    print(f'Ошибка: "{s}" не является числом.')
                print()
            case '4':
                todo.show_task()
                if not todo.tasks:
                    continue
                s = input('Введите номер задачи для удаления: ').strip()
                try:
                    idx = int(s)
                    todo.delete_task(idx)
                except ValueError:
                    print(f'Ошибка "{s}" не является числом.')
                print()
            case '5':
                todo.show_stats()
                print()
            case '0':
                print('Выход из программы выполнен')
                break
            case _:
                print(f'Неизвестная команда: "{choice}". Попробуйте снова.\n')


if __name__ == '__main__':
    main()