from . import jalali
from django.utils import timezone


def persian_number_converter(myStr):
    # values should be persian number
    numbers = {
        "0": "0",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
    }

    for e, p in numbers.items():
        myStr = myStr.replace(e, p)
    return myStr


def date_converter(time):
    jmonths = ["حمل", "ثور", "جوزا", "سرطان", "اسد",
               "سنبله", "میزان", "عقرب", "قوس", "جدی", "دلو", "حوت", ]

    time = timezone.localtime(time)

    time_to_str = "{}, {}, {}".format(time.year, time.month, time.day)
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)

    for index, month in enumerate(jmonths):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
            break

    output = "{} {} {}, ساعت {}:{}".format(
        time_to_list[2],
        time_to_list[1],
        time_to_list[0],
        time.hour,
        time.minute,
    )
    # below line if you want to change english numbers to persian numbers
    # return persian_number_converter(output)
    return output
