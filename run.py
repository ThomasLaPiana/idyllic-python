#!/usr/bin/env python3
"""Simple script to run the Idyllic Python application."""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "idyllic_python.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )
