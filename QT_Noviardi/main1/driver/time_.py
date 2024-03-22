from datetime import datetime

def get_date():
    return (datetime.now().date())

def get_jam():
    return(datetime.now().strftime("%I:%M:%S %p"))

if __name__ == "__main__":
    print(get_date())