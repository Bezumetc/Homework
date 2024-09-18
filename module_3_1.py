calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    print(len(string), string.upper(), string.lower())
    count_calls()
    return string
def is_contains(string, list_to_search):
    count_calls()
    return string.upper() in [s.upper() for s in list_to_search]

string_info('Capybara')
string_info('Armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)