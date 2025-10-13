def todayUTC():
    utc_aware_dt = datetime.now(timezone.utc)
    return utc_aware_dt.date()

def strcommas(number):
    return f"{number:,}"

def str_time_yyyymmdd(thedate:datetime):
    return f"{thedate:%Y/%m/%d}"

def is_yyyymmdd(date_string: str) -> bool:
    try:
        datetime.strptime(date_string, "%Y/%m/%d")
        return True
    except:
        return False
        