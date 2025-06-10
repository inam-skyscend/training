from datetime import datetime
import pytz

def main():
    utc_time = datetime.now(pytz.utc)
    print("Current UTC time is:", utc_time)
    print("SUCCESS")

if __name__ == "__main__":
    main()
