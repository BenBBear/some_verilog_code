import csv
import sys
import util
from collections import defaultdict


def parseKey(key):
    d = {}
    ks = key.split('_')
    for k in ks:
        s1, s2 = k.split('-')
        d[s1] = s2
    return d

HEADER = ['Iteration', 'Image_ID', 'Register_Power',
          'Sequential_Power', 'Combinational_Power', 'Total_Power']


def toCSV(in_file, out_file):
    writer = csv.writer(outfile, delimiter=',')
    writer.writerow(HEADER)
    sum_power = lambda x: sum([float(v) for v in x])
    for line in in_file:
        line = line.split(',')
        params = util.parse_filename(line[:5])
        regP = sum_power(line[5].split(' '))
        seqP = sum_power(line[6].split(' '))
        comP = sum_power((line[7].split(' '))
        writer.writerow([
            params['iteration'],
            params['image'],
            regP,
            seqP,
            comP,
            float(line[-1])
        ])

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as infile:
        with open(sys.argv[2], 'w') as outfile:
            toCSV(infile, outfile, outfile_short)
