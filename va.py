from neuralintents import BasicAssistant
import pandas_datareader as web
import sys
import webbrowser

stock_tickers = ['AAPL', 'FB', 'GS', 'TSLA']

todos = ["Go Shopping", "Go for Training", "Learn Java"]

reminders = ["Birthday Party on 21|1|24", "Wedding Anniversary on 8|2|24"]

def stock_function():
    for ticker in stock_tickers:
        data = web.DataReader(ticker, 'yahoo')
        print("The last price of {ticker} was {data ['Close'].iloc[-1]} ")


    webbrowser.open("https://www.tripadvisor.com/Attractions-g154943-Activities-Vancouver_British_Columbia.html")

def todo_show():
    print("Your TODO List:")
    for todo in todos:
        print(todo)

def todo_add():
    print("What TODO do you want to add to the list:")
    todos.append(todo)

def todo_remove():
    idx = int(input("Which TODO to remove (number) :")) -1
    if idx < len(todos):
        print(f"Removing {todos[idx]}")
        todos.pop(idx)
    else: print("There is no TODO at this position.")

def bye():
    print("Bye")
    sys.exit(0)



mappings = {'goodbye':bye,
            'todoshow':todo_show,
            'todoadd':todo_add,
            'todoremove':todo_remove,
              }
            



assistant = BasicAssistant('intents.json')

assistant.fit_model(epochs=50)
assistant.save_model()



while True:
    message = input("Enter a message: ")
    print(assistant.process_input(message))






















