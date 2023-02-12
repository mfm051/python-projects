def add_time(start, duration, day = None):
  hours = int(start.split(':')[0])
  min = int(start.split(':')[1].split()[0])
  period = start.split(':')[1].split()[1]
  week = {'Sunday':0,'Monday':1,'Tuesday':2,
  'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6}

  add_hours = int(duration.split(':')[0])
  add_min = int(duration.split(':')[1])
  add_days = 0

  min += add_min

  if min >= 60:
    add_hours += min//60
    min = min%60

  if add_hours >= 24:
    add_days = add_hours//24
    add_hours = add_hours%24

  hours += add_hours

  if period == 'AM':
    if hours >= 24:
      hours -= 24
      add_days += 1
    if hours > 12:
      hours -= 12
      period = 'PM'
    if hours == 12:
      period = 'PM'

  elif period == 'PM':
    if hours >= 24:
      hours -= 24
      add_days +=1
    if hours > 12:
      hours -= 12
      period = 'AM'
      add_days += 1
    if hours == 12:
      add_days += 1
      period = 'AM'

  new_time = f'{str(hours)}:{str(min).zfill(2)} {period}'

  revweek = dict()
  for k,v in week.items():
    revweek[v] = k

  if day != None:
    day = day.capitalize()
    count = (week[day] + add_days)%7
    new_time = f'{new_time}, {revweek[count]}'

  if add_days == 1:
    new_time = f'{new_time} (next day)'
  if add_days > 1:
    info = f'({add_days} days later)'
    new_time = f'{new_time} {info}'

  return new_time