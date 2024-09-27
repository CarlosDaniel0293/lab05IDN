import subprocess
result = subprocess.run(['echo', 'Hello World'], capture_output=True, text=True, shell=True) 
print(result.stdout)