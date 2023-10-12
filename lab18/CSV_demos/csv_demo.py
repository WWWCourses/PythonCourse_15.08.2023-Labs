import csv
persons = [
    {
        'empid': 1236,
        'lname': 'Smith',
        'fname': 'John',
        'bdate': '05-01-1962'
    },
    {
        'empid': 2398,
        'lname': 'Adams',
        'fname': 'John',
        'bdate': '03-22-1962'
    },
    {
        'empid': 4534,
        'lname': 'Johnson',
        'fname': 'Mary',
        'bdate': '05-07-1971'
    }
]

file_name = 'employees.csv'



def write_csv(file_name, add_header = True):
    with open(file_name, mode='w') as writer:
        lines = []
        if add_header:
            # lines.append(f'empid,lname,fname,bdate\n')
            keys = persons[0].keys()
            lines = ','.join(list(keys))
            print(lines)
            exit()

        for p in persons:
            lines.append(f'{p["empid"]},{p["lname"]},{p["fname"]},{p["bdate"]}\n')
        writer.writelines(lines)


def read_csv(file_name):
    with open(file_name, mode='r') as reader:
        csv_reader = csv.reader(reader)
        for r in csv_reader:
            print(r)

write_csv('employees.csv', True)
# write_csv('persons.csv', True)

# read_csv('persons.csv')


