from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(yesterday.date())
print(today.date())
print(tomorrow.date())
