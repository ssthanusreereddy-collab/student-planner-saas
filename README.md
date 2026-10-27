# Student Planner SaaS

A beginner-friendly student planner web application built with Python and Flask. It helps students add study tasks, assign subjects and due dates, mark tasks as completed, and track progress.

## Features

- Add tasks with a subject and due date
- Mark tasks as completed or incomplete
- Delete tasks
- View total, completed, and remaining task counts
- Save tasks locally in a JSON file
- Responsive dashboard for desktop and mobile

## Technology stack

- Python
- Flask
- HTML
- CSS
- JSON file storage

## Run locally

1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Create and activate a virtual environment (recommended):

   **Windows**
   ```bash
   py -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the app:

   ```bash
   python app.py
   ```

7. Open `http://127.0.0.1:5000` in your browser.

## Project structure

```text
student-planner-saas/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── tasks.json          # Created automatically when you add a task
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## GitHub upload

1. Sign in to GitHub and create a new repository named `student-planner-saas`.
2. Keep the repository public or private as your teacher requires.
3. Upload the project files/folders, or use Git:

   ```bash
   git init
   git add .
   git commit -m "Initial Student Planner SaaS project"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/student-planner-saas.git
   git push -u origin main
   ```

   Replace `YOUR-USERNAME` with your GitHub username.

## Notes

This is a starter academic project, not a production-ready SaaS service. It currently stores tasks in a local JSON file and does not include user login or cloud database support. Do not use it to store sensitive information.
