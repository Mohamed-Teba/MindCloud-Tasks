import time

minutes = int(input("Enter test minutes: "))
seconds = int(input("Enter test seconds: "))

if minutes < 0 or seconds < 0 or seconds > 59:
    print("Invalid test duration.")
    exit()

total_seconds = minutes * 60 + seconds

if total_seconds == 0:
    print("Invalid test duration.")
    exit()

if total_seconds > 300:
    print("Safety limit exceeded! Test duration capped to 05:00")
    total_seconds = 300

while total_seconds > 0:
    mins = total_seconds // 60
    secs = total_seconds % 60

    if total_seconds > 30:
        print(f"\r POWER ON | Remaining: {mins:02}:{secs:02}", end="")
    elif total_seconds > 10:
        print(f"\r STABILIZING SYSTEM | Remaining: {mins:02}:{secs:02}", end="")
    else:
        print(f"\r COOLDOWN PHASE | Do not touch | {mins:02}:{secs:02}", end="")

    time.sleep(1)
    total_seconds -= 1

print("\n Power test completed successfully")