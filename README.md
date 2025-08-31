# CrewAI Agents with Django Integration

This repository contains a collection of 20 intelligent agents built using [CrewAI](https://github.com/joaomdmoura/crewAI) and served to the internet via a Django backend. The agents are designed for various automation and AI tasks, and can be run individually or integrated into the Django web application.

## Project Structure

- **core/**: Django project root
  - **project/**: Contains the CrewAI agent scripts and related logic
  - **requirements.py**: Lists all Python dependencies required for the project

## Getting Started

### Prerequisites

- Python 3.8+
- [Django](https://www.djangoproject.com/) (if running the web application)
- [CrewAI](https://github.com/joaomdmoura/crewAI)
- All dependencies listed in `requirements.py`

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/crewai-django-agents.git
   cd crewai-django-agents/core
   ```

2. **Set up a Python virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.py
   ```

### Running Agents Individually

To run any agent script directly, navigate to the `project` subdirectory and execute the desired script:

```bash
cd code/project

select the directory of the script you want to run and then ...

python main.py
```

### Running with Django

If you want to use the Django web interface, ensure Django is installed in your virtual environment and follow standard Django project setup steps (`migrate`, `runserver`, etc.).

in the root directory of your file, run this in your terminal

```bash
\\ To create necessary database
python manage.py migrate

\\ To start the development server
python manage.py runserver
```

Then you can head over to localhost:8000

## License

Am available for collaborations so feel free to reach out to me.

