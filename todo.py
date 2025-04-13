import json
import os

tasks = []  # タスクリスト
FILENAME = "tasks.json"

def load_tasks():
    global tasks
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            tasks = json.load(f)
    else:
        tasks = []ef save_tasks():
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def save_tasks():
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def show_menu():
    print("\n==== ToDo メニュー ====")
    print("1. タスクを追加")
    print("2. タスクを表示")
    print("3. 終了")
    print("4. タスクを削除") 
    print("5. タスクを完了にする") # 新機能

def add_task():
    title = input("追加するタスクを入力してください: ")
    tasks.append({"title": title, "done": False})
    print(f"タスク「{title}」を追加しました。")

def show_tasks():
    if not tasks:
        print("タスクはまだありません。")
    else:
        print("\n現在のタスク一覧：")
        for i, task in enumerate(tasks, start=1):
            status = "[☑]" if task["done"] else "[ ]"
            print(f"{i}. {status} {task['title']}")

def delete_task():
    show_tasks()  # 現在のタスクを表示
    if not tasks:
        return  # タスクがなければ終了
    try:
        index = int(input("完了するタスクの番号を入力してください: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True  # タスクを完了にする
            print(f"タスク「{tasks[index - 1]['title']}」を完了にしました。")
        else:
            print("無効な番号です。")
    except ValueError:
        print("数字を入力してください。")

def complete_task():
    show_tasks()
    if not tasks:
        return
    try:
        index = int(input("完了にするタスクの番号を入力してください: "))
        if 1 <= index <= len(tasks):
            tasks[index - 1]["done"] = True
            print(f"タスク「{tasks[index - 1]['title']}」を完了にしました。")
        else:
            print("無効な番号です。")
    except ValueError:
        print("数字を入力してください。")

load_tasks()  # プログラム起動時に読み込み

while True:
    show_menu()
    choice = input("番号を選んでください: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        save_tasks()
        # プログラム終了時に保存
        print("ToDoアプリを終了します。")
        break
    elif choice == "4":
        delete_task()
    elif choice == "5":
        complete_task()
    else:
        print("無効な選択です。もう一度試してください。")







