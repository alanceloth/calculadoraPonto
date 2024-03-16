from datetime import datetime, timedelta

def calculate_exit_time(enter_time: str, lunch_time: str, return_from_lunch_time: str) -> str:
    # Convert strings to datetime objects
    enter_time_dt = datetime.strptime(enter_time, '%H:%M')
    lunch_time_dt = datetime.strptime(lunch_time, '%H:%M')
    return_from_lunch_time_dt = datetime.strptime(return_from_lunch_time, '%H:%M')

    # Calculate lunch duration
    lunch_duration = return_from_lunch_time_dt - lunch_time_dt

    # Calculate total time until now
    total_time_until_now = (lunch_time_dt - enter_time_dt) + (datetime.now() - return_from_lunch_time_dt)

    # Calculate remaining time for 8 hours of work
    remaining_time = timedelta(hours=8) - total_time_until_now

    # Calculate time to clock out
    exit_time = datetime.now() + remaining_time

    # Format and return the results
    duration_str = f"Your total lunch duration was: {lunch_duration}"
    exit_time_str = f"You can clock out at: {exit_time.strftime('%H:%M')}"

    return duration_str, exit_time_str
