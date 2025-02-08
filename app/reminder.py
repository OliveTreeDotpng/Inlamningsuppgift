import time

def reminder(service):
    time.sleep(10) # Vänta 10 sekunder
    return f"Kanske dags att ändra lösenord för {service}?" # Skicka påminnelse