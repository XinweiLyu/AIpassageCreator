## AIpassageCreator

Repository layout:

- `backend`: FastAPI service and Python dependencies
- `frontend`: Vue 3 + Vite web app

### Backend (FastAPI)

```powershell
cd backend
uv sync
uv run uvicorn app.main:app --host 0.0.0.0 --port 8567 --reload
```

### Frontend (Vue)

```powershell
cd frontend
npm install
npm run dev
```

The frontend dev server proxies `/api` requests to `http://127.0.0.1:8567`.
