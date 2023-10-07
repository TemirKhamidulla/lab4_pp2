# Считываем количество школьников
n = int(input())

# Создаем множество для языков, которые знают все школьники
all_known_languages = set()

# Создаем множество для языков, которые знает хотя бы один школьник
any_known_languages = set()

# Считываем данные о языках для каждого школьника
for _ in range(n):
    num_languages = int(input())
    languages = set()
    for _ in range(num_languages):
        language = input()
        languages.add(language)
    if len(all_known_languages) == 0:
        all_known_languages.update(languages)
    all_known_languages.intersection_update(languages)
    any_known_languages.update(languages)

# Выводим количество языков, которые знают все школьники, и сами языки
print(len(all_known_languages))
for language in sorted(all_known_languages):
    print(language)

# Выводим количество языков, которые знает хотя бы один школьник, и сами языки
print(len(any_known_languages))
for language in sorted(any_known_languages):
    print(language)
