import auto_vsqx_edit as vsqx
'''
Copyright (C) 2018  Gao Mengkai <gaomengkai0@outlook.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''


def get_notes_by_lrc_mode1(lrc, tone=1, accent=3):
    # inpot order: lrc as str, tone as int, accent as int
    # return order: notes as list
    # list order: lists in the main list, following this order:
    # y as str, n as int, p as str
    basic_tone = [64, 64, 65, 65, 66]
    basic_drop = [1, 3, 5, 6, 7]
    if tone not in range(0, 5):
        return
    if accent not in range(1, 6):
        return
    phonetic = vsqx.pinyin2xsampa.pinyin2xsampa(lrc)
    crt_tone = basic_tone[accent]
    crt_drop = basic_drop[accent]
    if tone == 1:
        n = crt_tone
    elif tone == 2:
        n = crt_tone - int(crt_drop / 2)
    elif tone == 3:
        n = crt_tone + int(crt_drop / 3) - 3
    elif tone == 4:
        n = crt_tone + int(crt_drop / 2)
    # n is the first note's n
    first_note = [lrc, n, phonetic]
    notes = []
    notes.append(first_note)
    if tone == 1:
        return notes
    if tone == 2:
        n = crt_tone + int(crt_drop / 2)
        second_note = ['-', n, '-']
        notes.append(second_note)
        return notes
    if tone == 3:
        n = n - int(crt_drop / 1.5)
        second_note = ['-', n, '-']
        notes.append(second_note)
        return notes
    if tone == 4:
        n = crt_tone - int(crt_drop / 2)
        second_note = ['-', n, '-']
        notes.append(second_note)
        return notes
    else:
        return


def main(path='lrcs.lab'):
    dat = open(path).read()
    dat = dat.split('\n')
    lrcs = []
    tones = []
    phonetics = []
    lens = 0
    for i in dat:
        lrcs.append(i.split(',')[0])
        tones.append(i.split(',')[1:])
        lens += len(i.split(',')[1:])
        phonetics.append(vsqx.pinyin2xsampa.pinyin2xsampa(i.split(',')[0]))
    notes = []
    note = {}
    remain = 0
    lrc_count = -1
    print("DEBUG: Lens = ", end='')
    print(lens)
    for i in range(lens):
        if remain is 0:
            lrc_count += 1
            remain = len(tones[lrc_count]) - 1
            new = True
        else:
            remain -= 1
            new = False
        if new:
            note['y'] = lrcs[lrc_count]
            note['n'] = int(tones[lrc_count][0])
            note['p'] = phonetics[lrc_count]
        else:
            note['y'] = '-'
            note['n'] = int(
                tones[lrc_count][len(tones[lrc_count]) - remain - 1])
            note['p'] = '-'
        print("DEBUG: APPEND NOTE:", end='')  # debug code
        print(note)
        will_add = []
        will_add.append(note['y'])
        will_add.append(note['n'])
        will_add.append(note['p'])
        # Appending data in the turn of 'y','n','p'
        notes.append(will_add)
# debug code
    print(lrcs)
    print(tones)
    print(notes)

def attach_file_mode1(path='lrcs.1.lab'):
    dat = open(path).read()
    dat = dat.split('\n')
    info1 = dat[0].split(':')
    if info1[0] == 'auto_vsqx_edit_fill_lrc_version':
        ver = int(info1[1])
    if ver != 1:
        return
    dat = dat[1:]
    notes = []
    for i in dat:
        i = i.split(",")
        inception_notes = get_notes_by_lrc_mode1(lrc=i[0], tone=int(i[1]), accent=int(i[2]))
        for j in inception_notes:
            notes.append(j)
    print(notes)
if __name__ == '__main__':
    attach_file_mode1()
