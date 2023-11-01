def add_time(start, duration, *args):
    # Optional parameter handler
    show = True if args else False

    new_time = ''
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    clock = [i for i in range(13)]  # len=13

    start = start.split(':')
    hours = [start[0], duration.split(':')[0]]
    min = [start[1].split()[0], duration.split(':')[1]]
    time = start[1].split()[1]

    summing_hours = int(hours[0]) + int(hours[1])
    summing_min = int(min[0]) + int(min[1])

    ## Days debugger ##
    days_later = int(int(duration.split(':')[0]) / 24)
    if summing_hours >= 11 and time == 'PM':
        days_later += 1

    day_position = 0
    if show is True:
        day = args[0].casefold()
        if day in weekdays:
            for index, i in enumerate(weekdays):
                if day == i:
                    day_position = index  # Assign args an index

    new_day = day_position + days_later  # returns new day position

    if new_day > len(weekdays):
        while not new_day < (len(weekdays)):
            new_day -= len(weekdays)  # handling >7 days

    ## Minutes debugger ##
    if summing_min >= 60:
        summing_hours += 1
        summing_min = summing_min - 60
    if summing_min < 10: summing_min = f'''{0}{summing_min}'''

    ## Hours debugger ##
    count = 0
    if summing_hours >= 12:
        try:
            count += 1
            change = summing_hours - 12
            summing_hours = clock[0 + change]
        except IndexError:
            x = summing_hours - (len(clock) - 1)
            if x >= (len(clock) - 1):
                while not x < (len(clock) - 1):
                    count += 1
                    x -= (len(clock) - 1)
                summing_hours = clock[x]
        if summing_hours == 0:
            summing_hours = 12
        if count > 0 and count % 2 != 0:
            time = 'PM' if time == 'AM' else 'AM'

    ## Formatting days
    formatted_day = str()
    if days_later == 0:
        formatted_day = ''
    elif days_later == 1:
        formatted_day = f'''{'(next day)'}'''
    elif days_later > 1:
        formatted_day = f'''{'('}{days_later} {'days later)'}'''

    if show is True and days_later > 0:
        new_time += f'''{summing_hours}{':' + str(summing_min)} {time + ','} {weekdays[new_day].capitalize()} {formatted_day}'''
    elif show is True and days_later == 0:
        new_time += f'''{summing_hours}{':' + str(summing_min)} {time + ','} {weekdays[new_day].capitalize()}'''
    elif show is False and days_later >= 1:
        new_time += f'''{summing_hours}{':' + str(summing_min)} {time} {formatted_day}'''
    elif show is False and days_later == 0:
        new_time += f'''{summing_hours}{':' + str(summing_min)} {time}'''

    return new_time

# print(add_time("11:59 AM", "00:02",'wednesday'))
