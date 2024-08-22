calls = 0
def count_calls():
      global calls
      calls += 1
      # print(calls)
def string_info(String):
    count_calls()
    word = str(String)
    res = (len(word), word.upper(),word.lower())
    return res
def is_contains(string, list_to_search):
    count_calls()
    string = str(string).lower()
    list_to_search = list(list_to_search)
    for i in range(len(list_to_search)):
        if str(list_to_search[i].lower()) == string:
          res = True
          break
        else:
          res = False
          continue
    return res

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print('Вызовы функций : ', calls)