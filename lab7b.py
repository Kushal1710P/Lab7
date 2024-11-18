#!/usr/bin/env python3
# Student ID: kparmar24
# Date: 2024-11-17
class Time:
    """Simple object type for time of the day.
    data attributes: hour, minute, second"""
    def __init__(self,hour,minute,second):
        """constructor for time object""" 
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objests and return the sum."""
    sum = Time(0,0,0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second = sum.second % 60

    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute = sum.minute % 60

    return sum

def change_time(time, seconds):
    time.second += seconds
    if valid_time(time) != True:
        while time.second >= 60:
             time.second -= 60
             time.minute +=1
        while time.minute >= 60:
             time.minute -= 60
             time.hour += 1

    total_seconds = time.hour *3600 + time.minute * 60 + time.second
    total_seconds %=86400

    if total_seconds < 0:
        total_seconds += 86400

    time.hour = total_seconds // 3600
    time.minute = (total_seconds % 3600) // 60
    time.second = total_seconds % 60

    return None

def valid_time(t):
    """check for the validity of the time object attributes:
        24 > hour > 0, 60 > minute > 0, 60 > second > 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True












