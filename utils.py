import calendar

def get_all_months():
    months = []
    for month in range(1, 13):
        months.append(calendar.month_name[month])
    return months