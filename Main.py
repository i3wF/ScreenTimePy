import psutil
import datetime
import time

def calculate_screen_time():
    screen_time_dict = {}
    for proc in psutil.process_iter(['create_time', 'name']):
        try:
            create_time = datetime.datetime.fromtimestamp(proc.info['create_time'])
            run_time = datetime.datetime.now() - create_time
            process_name = proc.info['name']
            screen_time_dict[process_name] = run_time
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    return screen_time_dict

def format_screen_time(screen_time):
    hours, remainder = divmod(screen_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours} hours, {minutes} minutes, {seconds} seconds"

def save_to_text_file(screen_time_dict):
    with open('ScreenTime.txt', 'w') as file:
        for process_name, run_time in screen_time_dict.items():
            formatted_run_time = format_screen_time(run_time)
            file.write(f"{process_name}: {formatted_run_time}\n\n")

screen_time_dict = calculate_screen_time()
save_to_text_file(screen_time_dict)

print("""
 
   ▄████████  ▄█     █▄     ▄████████ 
  ███    ███ ███     ███   ███    ███ 
  ███    ███ ███     ███   ███    █▀  
  ███    ███ ███     ███  ▄███▄▄▄     
▀███████████ ███     ███ ▀▀███▀▀▀     
  ███    ███ ███     ███   ███        
  ███    ███ ███ ▄█▄ ███   ███        
  ███    █▀   ▀███▀███▀    ███        
                                      
 """)
time.sleep(1)
print("Done, Say Thx For @b7z0")