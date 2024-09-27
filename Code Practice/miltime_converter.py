def convert_to_miltime(time):
    hour = int(time[:2])
    minute = time[2:5]
    period = time[-2:]

    if period.lower() == 'am':
        if hour == 12:
            hour = 0
    elif period.lower() == 'pm':
        if hour != 12:
            hour += 12

    return f'{hour:02}{minute}'



time = input()

print(convert_to_miltime(time))