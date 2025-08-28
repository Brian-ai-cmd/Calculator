def turn_minutes_into_hours(minutes):
    if minutes >= 60:
        hours = minutes // 60 
        minutes = minutes % 60 
        return hours, minutes
    else:
        return 0, minutes
    
def turn_hours_into_days(hours):
    if hours >= 24:
        days = hours // 24
        hours = hours % 24
        return days, hours
    else:
        return 0, hours
    
















































 



















