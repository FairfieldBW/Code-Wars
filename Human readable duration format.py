"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
"""

def format_duration(seconds):
    hours = str(int(seconds / 3600))
    minutes = str(int((seconds % 3600) / 60))
    seconds = str(int((seconds % 3600) % 60))

    if 2 > len(hours):
        hours = "0" + hours

    if 2 > len(minutes):
        minutes = "0" + minutes

    if 2 > len(seconds):
        seconds = "0" + seconds

    if hours > 0:
        if hours > 1
            time = hours + ":" + minutes + ":" + seconds
        else:
            time = "1 hour, " + minutes + " min"
    elif minutes > 0:


    return time