from datetime import datetime, timedelta

current_date = datetime.now()
date_minus_five = current_date - timedelta(days=5)
print(date_minus_five)
