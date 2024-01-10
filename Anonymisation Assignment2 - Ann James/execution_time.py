import subprocess
import time

def measure_execution_time(script_path):
    start_time = time.time()
    subprocess.run(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

if __name__ == "__main__":
    script_path = "incognito.py"  # Replace with the actual path of your script
    time_taken = measure_execution_time(script_path)
    print(f"Execution time of {script_path}: {time_taken:.5f} seconds")