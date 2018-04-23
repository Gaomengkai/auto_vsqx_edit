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
    for i in range(lens):
        if remain is 0:
            lrc_count += 1
            remain = len(tones[lrc_count])
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
            note['p'] = '-'
            note['n'] = int(
                tones[lrc_count][len(tones[lrc_count]) - remain - 1])
        notes.append(note)

    print(lrcs)
    print(tones)
    print(notes)


if __name__ == '__main__':
    main()
