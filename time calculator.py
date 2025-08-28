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
    
def calculate_days_from_now(start_day, days_to_add):
    week_days = {'monday': 0, 'tuesday': 1 ,'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}
    week_days_number = {0: 'monday', 1: 'tuesday', 2: 'wednesday', 3: 'thursday', 4: 'friday', 5: 'saturnday', 6: 'sunday'}

    day_index = week_days[start_day.lower()]
    final_day_index = (day_index + days_to_add) % 7 
    return week_days_number[final_day_index]

def get_12_hours_format(hours):
    '''Convert 24 time to 12 hour format with AM/PM'''
    if hours == 0 or hours == 24:
        return 12 , 'AM' #midnight 
    elif 0 < hours < 12:
        return hours, 'AM'
    elif hours == 12: 
        return 12, 'PM'
    elif 12 < hours < 24:
        return hours - 12 , 'PM'
    else:
        return hours % 12, 'PM'
    

def add_time(start_time, duration, day = None):
    #Parse start time 
    start_time = start_time.upper()
    index_time = start_time.index(':')
    am_pm_index = start_time.index(' ') if ' ' in start_time else -1 

    start_hours = int(start_time[:index_time])
    start_minutes = int(start_time[index_time + 1 : am_pm_index] if am_pm_index != -1 else None)

    # Convert to 24-hour format 
    if 'PM' in start_time and start_hours != 12:
        start_hours = start_hours + 12
    elif 'AM' in start_time and start_hours == 12:
        start_hours = 0

    # Parse duration 
    duration_time_index = duration.index(':')
    duration_hours = int(duration[:duration_time_index])
    duration_minutes  = int(duration[duration_time_index + 1:])

    # Add time 
    total_minutes = start_minutes + duration_minutes
    extra_hours, final_minutes = turn_minutes_into_hours(total_minutes)

    total_hours = start_hours + duration_hours + start_hours
    days_passed, final_hours_24 = turn_hours_into_days(total_hours)
    
    # convert to 12-hour format
    final_hours_12, am_pm = get_12_hours_format(final_hours_24)

    # Build final string
    result = f"{final_hours_12}:{final_minutes} {am_pm}"

    # Add day information
    if day:
        final_day = calculate_days_from_now(day, days_passed)
        result += f", {final_day}"
    
    #Add days later information 
    if days_passed == 1:
        result += f" (next day)"
    elif days_passed > 1:
        result += f"{days_passed} days later"

    return result 
    
print(add_time('3:00 PM', '3:10'))















































 



















