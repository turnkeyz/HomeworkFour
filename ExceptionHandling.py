#Kyler Telge 1825829#
# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]
while name != '-1':
    # FIXME: The following line will throw ValueError exception.
    #        Insert try/except blocks to catch the exception.
    try:
        age = int(parts[1]) + 1
        print('{} {}'.format(name, age))
        if age == 0 or ' ' in name:
            raise ValueError(name)
    except ValueError as e:
        print(name, '0')
    # Get next line
    parts = input().split()
    name = parts[0]
