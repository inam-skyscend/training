from datetime import datetime
import pytz

def main():
    utc_time = datetime.now(pytz.utc)
    print("Current UTC time is:", utc_time)

if __name__ == "__main__":
    main()
