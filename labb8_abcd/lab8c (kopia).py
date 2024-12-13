# Write your code for lab 8C (remove) here.

from cal_ui import *
from lab8b import *


def remove(name: str, day: CalendarDay, month: str, start: str) -> None:
    '''Removes the booking in input from the big calendar from given name'''
    day = new_day(day)
    month = new_month(month)

    old_cal_year = get_calendar(name)
    old_cal_month = cy_get_month(month, old_cal_year)
    old_cal_day = cm_get_day(old_cal_month, day)

    start_time = new_time_from_string(start)

    appointments_lst = new_app_list(old_cal_day, start_time)

    if not is_booked_from(old_cal_day, start_time):
        print("No booking found on given day")
    else:
        new_cal_day = new_calendar_day(day, appointments_lst)
        new_cal_month = cm_plus_cd(old_cal_month, new_cal_day)
        new_cal_year = cy_plus_cm(old_cal_year, new_cal_month)
        print("Booking has been removed")

        insert_calendar(name, new_cal_year) #Inserts new calendar to global Calendar


def new_app_list(day: CalendarDay, start_time: Time) -> List:
    '''Returns a list with appointments of the appointments with different start times from input'''

    ensure_type(day, CalendarDay)
    ensure_type(start_time, Time)

    appointments = []

    if cd_is_empty(day):
        print(f"No appointments on {day}")
        return appointments

    for app in cd_iter_appointments(day):
        if start_time != ts_start(app_span(app)):
            appointments.append(app)
    return appointments

#create("Jayne")

#book("Jayne", 20, "sep", "12:00", "14:00", "Rob train")
#book("Jayne", 20, "sep", "15:00", "16:00", "Escape with loot")
#show("Jayne", 20, "sep")
#print("------")

#remove("Jayne", 20, "sep", "12:00")
#show("Jayne", 20, "sep")