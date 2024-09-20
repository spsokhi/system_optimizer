import subprocess
import psutil

def optimize_drives(output_callback=print):
    try:
        subprocess.run('defrag C: /O', shell=True)
        output_callback("Drive C: optimized")
    except Exception as e:
        output_callback(f"Error optimizing drive: {e}")

def display_system_info(output_callback=print):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    output_callback(f"CPU Usage: {cpu_usage}%")
    output_callback(f"Memory Usage: {memory_info.percent}%")
    output_callback(f"Total Memory: {memory_info.total / (1024**3):.2f} GB")
    output_callback(f"Available Memory: {memory_info.available / (1024**3):.2f} GB")
