# =========================================================================
# Type definition
# =========================================================================
from collections import namedtuple
from cal_abstraction import *

# Define the type somehow...  The initial "" is simply here as a placeholder.
TimeSpanSeq = NamedTuple("TimeSpanSeq", [("timespan", List[TimeSpan])])

# =========================================================================
#  Function implementations
# =========================================================================

# Implement these functions!  Also determine if you need *additional* functions.

def new_time_span_seq(timespan: List[TimeSpan] = None):
    '''Creates a new timespan and sorts the list by time'''
    if timespan is None:
        timespan = []
    else:
        timespan = sorted(timespan, key=lambda ts: ts_start(ts)) 
    return TimeSpanSeq(timespan)


def tss_is_empty(tss) -> bool:
    '''Returns true if the timespan is empty'''
    return not tss         


def tss_plus_span(tss: TimeSpanSeq, ts: TimeSpan):
    '''Adds a timespan to the TimeSpanSeq'''
    ensure_type(ts, TimeSpan)
    ensure_type(tss, TimeSpanSeq)

    new_tss = tss.timespan + [ts]
    return new_time_span_seq(new_tss)


def tss_iter_spans(tss):
    '''Iterates thru the TimeSpanSeq 1 at a time'''
    for ts in tss:
        yield ts
    

def show_time_spans(tss):
    '''Prints out all timespans in TimeSpanSeq'''
    for all_time_spans in tss_iter_spans(tss):
       print(all_time_spans)
    


# Keep only time spans that satisfy pred.
# You do not need to modify this function.
def tss_keep_spans(tss, pred):
    result = new_time_span_seq()
    for span in tss_iter_spans(tss):
        if pred(span):
            result = tss_plus_span(result, span)

    return result


if __name__ == "__main__":
    # Skapa några TimeSpan-objekt
    ts1 = TimeSpan({"start": 1, "end": 5})
    ts2 = TimeSpan({"start": 6, "end": 10})
    ts3 = TimeSpan({"start": 2, "end": 4})
    ts4 = TimeSpan({"start": 3, "end": 4})

    # Skapa en TimeSpanSeq
    tss = new_time_span_seq([ts1, ts2])

    #print("Before adding ts3:", tss)

    # Lägg till en ny TimeSpan
    tss = tss_plus_span(tss, ts3)
    tss = tss_plus_span(tss, ts4)
    show_time_spans(tss)
