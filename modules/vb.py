# Служебный скрипт для подсчета количества строк в проекте
#
# Примечание. Этот скрипт полезен только во время разработки/тестирования.
# Боевое использование не предполагается.


import os
import os.path as path

lang_lines = {'py-comment': 0}
files_cnt = 0

for current_dir, dirs, files in os.walk(path.abspath(path.join(__file__, "../.."))):
    if any([name in current_dir for name in ['.\.git', '.\.idea', '\\venv']]):
        continue

    for file in files:
        lang = file.split('.')[-1]
        if lang in {'py', 'html', 'css', 'md'}:
            files_cnt += 1

            # print(current_dir, file)
            with open(current_dir + '/' + file, 'r', encoding='utf8') as f:
                lines_now = f.readlines()

            if lang not in lang_lines:
                lang_lines[lang] = 0

            for line in lines_now:
                if lang == 'py' and line.count('#'):
                    lang_lines['py-comment'] += 1
                else:
                    lang_lines[lang] += 1

print('=======')
print(f'Количество строк кода в проекте: {sum(lang_lines.values())}')
print(f'Из них строк кода: {sum(lang_lines.values()) - lang_lines["py-comment"]}, '
      f'строк комментариев: {lang_lines["py-comment"]}')
print('=======')
for lang, lines in sorted(list(lang_lines.items()), key=lambda x: (-x[1], x[0])):
    print(f'{lang}: {lines} строк')
print('=======')
print(f'Всего файлов кода: {files_cnt}')
print('=======')
