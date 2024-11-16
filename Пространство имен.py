calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)

def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()
    for item in list_to_search:
        if item.lower() == string_lower:
            return True
    return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)


    for (i, j) in pairs:
        pair_sum = i + j
        if n % pair_sum == 0:
            password += f"{i}{j}"

    return password

for n in range(3, 21):
    result = generate_password(n)
    print(f"{n} - {result}")
