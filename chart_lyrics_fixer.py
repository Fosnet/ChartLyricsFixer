import shutil
import os
import re

taken_words_list = ['Default', 'phrase_start', 'phrase_end', 'idle', '#play', 'half_tempo', 'normal_tempo', 'verse',
                    'chorus', 'end', 'music_start', 'lighting ()', 'lighting (flare)', 'lighting_blackout',
                    'lighting (chase)', 'lighting (strobe)', 'lighting (color1)', 'lighting (color2)',
                    'lighting (sweep)', 'crowd_lighters_fast', 'crowd_lighters_off', 'crowd_lighters_slow',
                    'crowd_half_tempo', 'crowd_normal_tempo', 'crowd_double_tempo', 'band_jump', 'sync_head_bang',
                    'sync_wag', 'section', 'solo', 'soloend', 'lighting', 'lyric']


def copy_file(file_path):
    folder, file_name = os.path.split(file_path)

    count = 1
    output_file_path = file_path

    while os.path.exists(output_file_path):
        output_file_name = f'{file_name}.old_{count}'
        output_file_path = os.path.join(folder, output_file_name)
        count += 1

    shutil.copyfile(file_path, output_file_path)


def lyricise_file(file_name):
    copy_file(file_name)
    with open(file_name, 'r') as file:
        lines = file.readlines()

    is_event = False
    for i in range(len(lines)):
        line = lines[i].rstrip()
        if '[Events]' in line:
            is_event = True
        if is_event:
            if line.strip() == '}':
                is_event = False
            else:
                regex = re.compile(fr'^\s{{2}}[0-9]+\s=\sE\s"(?!(?:{"|".join(taken_words_list)})\b)')
                line = regex.sub(fr'\g<0>lyric ', line)
                line = re.sub(r'(lyric\s)+', 'lyric ', line)  # removes duplicates in case of reruns
                line = re.sub(r'\s+', ' ', line)  # removes double spaces
                line = re.sub(r'\s"$', '"', line)  # removes spaces at ends of words

        lines[i] = line

    with open(file_name, 'w') as file:
        for line in lines:
            file.write(f'{line}\n')


def main():
    file_name = 'Test_folder/notes.chart'
    lyricise_file(file_name)


if __name__ == '__main__':
    main()
