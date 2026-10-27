from flask import Flask, render_template, request, redirect, url_for
import json
import os
from datetime import date

app = Flask(__name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2, ensure_ascii=False)


@app.route("/")
def index():
    tasks = load_tasks()
    tasks.sort(key=lambda task: (task.get("done", False), task.get("due_date", "")))
    completed = sum(1 for task in tasks if task.get("done"))
    return render_template(
        "index.html",
        tasks=tasks,
        completed=completed,
        today=date.today().isoformat()
    )


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    subject = request.form.get("subject", "").strip()
    due_date = request.form.get("due_date", "").strip()

    if title:
        tasks = load_tasks()
        tasks.append({
            "id": max([task.get("id", 0) for task in tasks], default=0) + 1,
            "title": title,
            "subject": subject or "General",
            "due_date": due_date,
            "done": False
        })
        save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>", methods=["POST"])
def toggle_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            task["done"] = not task.get("done", False)
            break
    save_tasks(tasks)
    return redirect(url_for("index"))


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    tasks = [task for task in load_tasks() if task.get("id") != task_id]
    save_tasks(tasks)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
