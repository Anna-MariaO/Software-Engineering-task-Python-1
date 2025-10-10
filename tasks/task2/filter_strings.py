def filter_strings(filter_func, strings):
    
    result = []
    for x in strings:
        if filter_func(x):  
            result.append(x)
    return result


words = [
    "Apple pie",
    "banana",
    "Alaska",
    "night sky",
    "car",
    "spaceship",
    "aqua",
    "dream",
    "good morning",
    "Sky",
    "art",
    "Pythonista",
    "snow fall",
    "AI",
    "Aurora",
    "coffee",
    "rain",
    "moonlight",
    "a",
    "Magic forest"
]

no_spaces = filter_strings(lambda x: " " not in x, words)
print(f'Без пробелов: {no_spaces}\n')

not_start_a = filter_strings(lambda x: not x.strip().lower().startswith("a"), words)
print(f'Не начинаются с "a": {not_start_a}\n')


length_5_or_more = filter_strings(lambda x: len(x) >= 5, words)
print(f'Длина 5 и больше: {length_5_or_more}')