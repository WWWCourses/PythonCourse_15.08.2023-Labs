import re

HOURS_RE = re.compile(r'^(\d+):(\d+)$')

def astro_to_acad(hours1, minutes=0):
    total_minutes = hours*60 + minutes
    acad_hours = total_minutes/40
    return acad_hours

def acad_to_astro(hours, minutes=0):
    pass

print(f'1. Convert Astronomical to Academical Hours:30')
print(f'2. Convert Academical to Astronomical Hours:30')

choice = input('Enter your choice: [1/2]: ')

input_type = 'Astronomical' if choice=='1' else 'Academical'
output_type = 'Academical' if choice=='1' else 'Astronomical'

input_hours = input(f'Enter {input_type} hours [HH:MM]:')

m = HOURS_RE.match(input_hours)
if m:
    hours, minutes = (int(el) for el in m.groups())
    # print(hours, minutes)
else:
    raise Exception('No match')

output_hours = astro_to_acad(hours,minutes) if input_type == 'Astronomical' else \
               acad_to_astro(hours, minutes)


print(f'{input_hours} {input_type} hours are equal to {output_hours} {output_type}')





