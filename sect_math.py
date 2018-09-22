

import os, sys
from itertools import izip

def parse_cvg_pair(file1, file2, outfilename, expresion):
    """
    Parses a pair of cvg files of the same reference and applys the operation kmerwise
    :param file1:
    :param file2:
    :return:
    """

    header = None
    outfile = open("%s.salida" %(outfilename), 'w')
    with open(file1) as f1, open(file2) as f2:
        for line_f1, line_f2 in izip(f1, f2):

            if line_f1[0] == '>':
                print line_f1
                assert line_f1 == line_f2
                if header is not None:
                    outfile.write("%s%s\n" %(header, ' '.join(map(str, result))))
                header = line_f1

            else:
                # print map(int, line_f1.split())
                # result = [k1 + k2 for k1, k2 in zip(map(int, line_f1.split()), map(int, line_f2.split()))]
                result = [eval(expresion) for k1, k2 in zip(map(int, line_f1.split()), map(int, line_f2.split()))]

    outfile.close()
    return None

if __name__ == "__main__":

    parse_cvg_pair(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])