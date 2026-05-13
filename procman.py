import psutil
import time 
import msvcrt
print("-"*30)
print("----Simple Process Monitor -Press q  to stop ----\n")

while True:
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    print(f"CPU : {cpu}%  RAM : {ram}%")
        
    print("-"*15)
    print("--- Top Processes ---\n")
    for proc in psutil.process_iter(['name','cpu_percent']):
        try:
            name = proc.info['name']
            cpu_usage = proc.info['cpu_percent']
            if cpu_usage > 0:
                print(f"{name} : {cpu_usage}%")
        except:
            continue
    print("-"*30)
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('ascii').lower()
        if key == 'q':
            print("\n--- Stopped by user ---")
            break
    time.sleep(2)


    
    



            
            



