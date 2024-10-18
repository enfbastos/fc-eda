source .venv/bin/activate

uvicorn src.main:app --port 3003 --reload --log-level debug --workers 1
