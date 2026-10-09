# RunSure CI Workflow Risk Validator
# Transfer & Setup Instructions (Windows)

## Prerequisites
- Python 3.9+
- Node.js 18+

## Setup Backend
1. Open terminal in the project root.
2. Create virtual environment:
   python -m venv .venv
3. Activate virtual environment:
   .\.venv\Scripts\activate
4. Install Python requirements:
   pip install -r requirements.txt
5. Start backend:
   python scripts/run_api.py
   (Backend runs at http://127.0.0.1:8080)

## Setup Frontend
1. Open a new terminal in the `frontend` directory.
2. Install dependencies:
   npm install
3. Start frontend:
   npm run dev
   (Frontend runs at http://localhost:5173/ or similar)
