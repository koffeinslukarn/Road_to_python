# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from lab8.cal_ui import get_calendar
from settings import CHECK_AGAINST_FACIT
from lab8c import *
from lab8b import*

if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *


def show_free(name: str, inpt_day: int, month:str, start: str, end: str):
    '''Shows free times for given calendar name and day, between given times'''
    day = new_day(inpt_day)
    month = new_month(month)

    cal_year = get_calendar(name)
    cal_month = cy_get_month(month, cal_year)
    cal_day = cm_get_day(cal_month, day)

    free_start_time = new_time_from_string(start)
    free_end_time = new_time_from_string(end)

    free_time_span = free_spans(cal_day, free_start_time, free_end_time)

    for lst in free_time_span:
        for times in lst:
            start_free = new_str_from_time(ts_start(times))
            end_free = new_str_from_time(ts_end(times))

            print(f"{start_free}-{end_free}")


def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    '''Sorts appointments and returns a TimeSpanSeq with time between appointmensts'''
    app_time = []
    free_time = []

    for app in cd_iter_appointments(cal_day):
        time_app = app_span(app)

        if time_precedes_or_equals(end, ts_end(time_app)):
            if time_precedes(ts_start(time_app), end):    # if appointment is after or same end
                app_time.append(new_time_span(ts_start(time_app), end))

        elif time_precedes_or_equals(ts_start(time_app), start):
            if time_precedes(start, ts_end(time_app)):   # if appointment is before or same as start
                app_time.append(new_time_span(start, ts_end(time_app)))

        elif time_precedes_or_equals(ts_start(time_app), start) and time_precedes_or_equals(end, ts_end(time_app)):
            app_time.append(new_time_span(start, end)) # if 1 appointment precedes both start and end

        else:
            app_time.append(time_app)


    if len(app_time) == 0: # No appointments that day
        free_time.append(new_time_span(start, end))

    elif len(app_time) == 1 and time_precedes_or_equals(ts_start(app_time[0]), start) and time_precedes_or_equals(end, ts_end(app_time[0])):
        print("No free time available")

    else:
        if time_precedes(start, ts_start(app_time[0])):
            first_ts = new_time_span(start, ts_start(app_time[0]))  # adds first free-time if booking is not before or equal as start
            free_time.append(first_ts)

        if len(app_time) >= 1: #for several bookings
            for i in range(len(app_time) - 1):
                current_end = ts_end(app_time[i])
                next_start = ts_start(app_time[i + 1])

                if time_precedes(current_end, next_start): # if appointments starts next to each other
                    between_ts = new_time_span(current_end, next_start)
                    free_time.append(between_ts)

        if time_precedes_or_equals(ts_end(app_time[-1]), end):
           end_ts = new_time_span(ts_end(app_time[-1]), end) #adds last free time if appointment is not in the way
           free_time.append(end_ts)

    new_tss = new_time_span_seq(free_time)
    return new_tss


def new_str_from_time(time: Time) -> str:
    """ Convert and return a Time object into a string in the 'HH:MM' format. """
    hour = hour_number(time_hour(time))
    minute = minute_number(time_minute(time))
    return f"{hour:02d}:{minute:02d}"  # 02d to make sure it is 2 digits





create("Jayne")
book("Jayne", 20, "sep", "16:00", "17:00", "nehehe")
book("Jayne", 20, "sep", "11:00", "17:00", "Escape with loot")
book("Jayne", 20, "sep", "11:00", "12:00", "Rob train")
book("Jayne", 20, "sep", "14:00", "16:00", "Too easy")

#show("Jayne", 20, "sep")

#remove("Jayne", 20, "sep", "12:00")
#show("Jayne", 20, "sep")
show_free("Jayne", 20, "sep", "10:00", "18:00")