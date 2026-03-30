"""DashScope OpenAI 兼容接口连通性演示（非流式 + 流式）。

在 backend 目录下执行::

    uv run python scripts/dashscope_chat_demo.py
"""
from __future__ import annotations

import asyncio
import sys
from pathlib import Path

# 允许直接 `python scripts/xxx.py` 时解析 `app` 包
_BACKEND_ROOT = Path(__file__).resolve().parent.parent
if str(_BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(_BACKEND_ROOT))

from openai import AsyncOpenAI

from app.config import settings


async def main() -> None:
    client = AsyncOpenAI(
        api_key=settings.dashscope_api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1", 
    )

    # 非流式调用
    response = await client.chat.completions.create(
        model=settings.dashscope_model,
        messages=[{"role": "user", "content": "你好，请介绍一下你自己"}],
    )
    print(response.choices[0].message.content)

    print()

    # 流式调用
    stream = await client.chat.completions.create(
        model=settings.dashscope_model,
        messages=[{"role": "user", "content": "用一句话介绍 FastAPI"}],
        stream=True,
    )
    async for chunk in stream:
        if chunk.choices[0].delta.content: 
            print(chunk.choices[0].delta.content, end="", flush=True)
    print()


if __name__ == "__main__":
    asyncio.run(main())
