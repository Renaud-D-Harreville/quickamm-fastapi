# 🚀 quickamm-frontend

Quickamm is a smart Multiple Choice Question (MCQ) platform designed to help candidates prepare for the French "Accompagnateur en montagne" (AEM) hiking guide diploma.

here is the deployed app running using Google Cloud Platform (GCP): **[Quick AMM website](https://quickamm.valier.ovh/)**

---

### ⛰️ The Challenge

The "Accompagnateur en moyenne montagne" (AMM) diploma requires candidates to pass an MCQ test at the very beginning of the course. 
Most existing preparation tools use static questions, where the questions and answers are always in the same order.

This leads to a common problem: **candidates start to memorize the *pattern* of the answers rather than *understanding* the concepts.**

### ✨ Our Solution: Quickamm

Quickamm was built to solve this exact problem by focusing on two core principles: smart randomization and detailed explanations.

It began as a simple command-line tool (hence the name "Quick"), but has been rebuilt as a modern web application to help more candidates.

### 🎯 Key Features

* **🧠 Smart Randomization**
    To prevent "learning the test" by heart, Quickamm dynamically builds every question:
    * **Random Answer Order:** The order of potential answers is shuffled every time.
    * **Dynamic Answer Pool:** The algorithm pulls from a large bank of possible answers (often more than 4) and selects at least one correct answer and several incorrect ones (following the diploma's rules).
    * **Massive Variety:** This approach creates a huge number of unique question combinations, making it highly unlikely you'll see the exact same question twice.

* **📚 Detailed Explanations**
    Passing the test isn't just about getting the right answer; it's about knowing *why* it's right.
    * **Question Explanations:** After you answer, you get a detailed explanation for the question as a whole.
    * **Per-Answer Feedback:** Each individual answer (both correct and incorrect) also includes a short explanation.
    * **Go Deeper:** To encourage further learning and verify the information, explanations include references so you can read more about the topics.

---


### 🏗️ Project Architecture

This project is split into a separate frontend and backend API.

* **Frontend (Vue.js):** `[`quickamm-frontend`](https://github.com/Renaud-D-Harreville/quickamm-frontend)`
* **Backend (This Repo):** `quickamm-fastapi`
* **Original Project (Archived):** The first version was a monolithic Django project, which you can find [here](https://github.com/Renaud-D-Harreville/quickamm).

---

### ⚙️ Getting Started

To run this project locally:

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Renaud-D-Harreville/quickamm-fastapi.git
    cd quickamm-fastapi
    ```

2.  **Install project:**
    ```sh
    chmod +x setup.sh
    ./setup.sh
    ```

3.  **get into the project environment:**
    ```sh
    source .venv/bin/python
    ```

4. **Run the dev server:**
    ```sh
    python -m uvicorn webapi.main:app --reload 
    ```
   
5. The application will be available at `http://localhost:8000`.


---

### 🤝 Contributing

Contributions are welcome! If you have a feature request, bug report, or want to add new questions, please feel free to:

* Open an issue to discuss your idea.
* Fork the repository and submit a pull request.

