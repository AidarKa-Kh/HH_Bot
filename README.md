# 🤖 HH_Bot

- [English](#english)
- [Русский](#русский)

---

## English

**HH_Bot** — is a tool for automatically updating your resumes on the hh job aggregator platform.

---

## 📁 Project Structure

Below is the project structure with a description of each directory and file:

| **Directory/File** | **Description**                                                                                                                                                    |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`hh_client/`**   | Contains the `client` file for interacting with the platform and performing core functions. A session file is created after the first run (automatically updated). |
| **`logs/`**        | Contains logging settings. Logs are displayed in the console and saved to `./data/app.log` (created on the first run).                                             |
| **`core.py`**      | File for loading sensitive variables from the virtual environment.                                                                                                 |
| **`main.py`**      | The main file to run the program.                                                                                                                                  |

---

## ⚙ Installation

1. Create a project or clone it to your machine.


2. Create a virtual environment:
    ``` bash
   python -m venv venv

3. Activate the environment:


- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

4. Install dependencies:
    ``` bash
   pip install -r requirements.txt
5. Install Chromium for Playwright:
    ``` bash
   playwright install chromium

6. Add your platform login and password to the `.env` file.
7. Run the `main.py` file.

---

## Русский

**HH_Bot** — это инструмент для автоматического поднятия собственных резюме на агрегаторе вакансий hh.

---

## 📁 Структура проекта

Ниже представлена структура проекта с описанием каждой директории и файла:

| **Директория/Файл** | **Описание**                                                                                                                                                    |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **`hh_client/`**    | Содержит `client` файл для взаимодействия с платформой и выполнения основных функций. Файл сессии появляется после первого запуска программы (автообновляемый). |
| **`logs/`**         | Содержит настройки логирования. Логи отображаются в консоли и сохраняются в `./data/app.log` (создается  при первом запуске).                                   |
| **`core.py`**       | Файл с загрузкой чувствительных переменных из виртуального окружения.                                                                                           |
| **`main.py`**       | Основной файл для запуска программы.                                                                                                                            |

---

## ⚙ Установка

1. Создайте проект или клонируйте его себе.


2. Создайте виртуальное окружение:
    ``` bash
   python -m venv venv

3. Активируйте окружение:


- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

4. Установите зависимости:
    ``` bash
   pip install -r requirements.txt
5. Установите Chromium для работы с playwright:
    ``` bash
   playwright install chromium

6. Добавьте в файл `.env` свои логин и пароль от платформы
7. Запустите файл `main.py`
