import functions
import time

now = time.strftime("It is %b %d, %Y at %H:%M:%S ")
print(now)

while True:

    user_action = input("Type add, show, edit, complete, or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index+1}. {item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = f"{new_todo}\n"

            functions.write_todos(todos)

        except ValueError:
            print(f'The command "{user_action}" is invalid.')
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1

            todoToRemove = todos[index].strip("\n").lower()
            todos.pop(index)

            functions.write_todos(todos)

            message = f'Todo "{todoToRemove}" was removed.'
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
        except ValueError:
            print(f'The command "{user_action}" is invalid.')
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print(f'Command "{user_action}" is not valid.')


print("Bye!")
