from datetime import datetime
import pytz

def main():
    # Get current UTC time
    utc_time = datetime.now(pytz.utc)
    print("✅ Current UTC time is:", utc_time.strftime("%Y-%m-%d %H:%M:%S %Z"))

    # Say Hello
    print("👋 Hello from Jenkins Pipeline!")

    # Simple calculation
    a = 5
    b = 3
    result = a + b
    print(f"🧮 The result of {a} + {b} is {result}")

if __name__ == "__main__":
    main()
