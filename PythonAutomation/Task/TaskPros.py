import os
import time
import psutil  
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from typing import Optional


CPU_LIMIT = 1.0
MEM_LIMIT = 0.5


app = FastAPI(
    title="Process Monitor API",
    description="Мониторинг на процеси в реално време",
    version="1.0"
)


static_dir = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


@app.get("/")
def serve_index():
    return FileResponse(os.path.join(static_dir, "index.html"))


@app.get("/processes")
def read_processes(
    sort_by: Optional[str] = Query("cpu_percent", enum=["pid", "name", "cpu_percent", "memory_percent"]),
    descending: bool = Query(True),
    filter_name: Optional[str] = Query(None)
):
    
    for proc in psutil.process_iter():
        try:
            proc.cpu_percent(interval=None)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    time.sleep(0.2)

    processes = []

    
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            name = proc.info['name']

         
            if filter_name and filter_name.lower() not in name.lower():
                continue

            cpu = proc.cpu_percent(interval=None)
            mem = proc.memory_percent()

            alert = []
            if cpu > CPU_LIMIT:
                alert.append("High CPU")
            if mem > MEM_LIMIT:
                alert.append("High MEM")

            
            processes.append({
                "pid": proc.pid,
                "name": name,
                "cpu_percent": cpu,
                "memory_percent": mem,
                "alert": ", ".join(alert) if alert else ""
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


    sorted_procs = sorted(
        processes,
        key=lambda x: x.get(sort_by, 0) or 0,
        reverse=descending
    )

   
    return JSONResponse(content=sorted_procs[:15])
