# 项目启动与结束命令

## 启动（按顺序）

### 1) 启动 MySQL

```powershell
Start-Service MySQL80
```

说明：启动本地 MySQL 服务（数据库）。

### 2) 启动 Redis

```powershell
docker start redis
```

说明：启动 Redis 容器（缓存/会话）。

### 3) 启动后端（FastAPI）

```powershell
cd C:\Users\Msi\PycharmProjects\AIpassageCreator\backend
uv run uvicorn app.main:app --reload --host 0.0.0.0 --port 8567
```

说明：后端接口地址为 `http://127.0.0.1:8567`。

### 4) 启动前端（Vue）

```powershell
cd C:\Users\Msi\PycharmProjects\AIpassageCreator\frontend
npm run dev
```

说明：前端开发地址通常为 `http://127.0.0.1:5173`。

## 结束（关闭项目）

### 1) 停止前后端

在前端和后端各自终端按：

```powershell
Ctrl + C
```

说明：停止 `npm run dev` 和 `uvicorn` 进程。

### 2) 可选：关闭 MySQL 与 Redis

```powershell
Stop-Service MySQL80
docker stop redis
```

说明：不开发时可关闭，节省资源。

