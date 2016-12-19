import re

def _sgdict( fastafile ):

    '''Reads a Saccharomyces Genome Database (SGD) fasta file 
    and enables protein summary information access by trivial or systematic name

    :param fastafile: file path of fasta file. 

    :returns: A dictionary with a protein's trivial and systematic name (uppercase!)
    as key to access SGD summary information
    (systematic name, trivial name, gene & protein description, sequence)
    '''

    fastapattern = '(?P<sys>(\S{5,7}\s))(?P<triv>(\S{4,5}\s))(?P<descr>SGDID.+\n)(?P<seq>[A-Z\*\n]+)' #[\*\n)
    _stripline = lambda s: s.replace('\n', '').replace('\r', '').strip('*')
    with open(fastafile, 'rb') as openfile: #with: closes file at end of 'loop', also when error occurs and you don't reach file.close()
        readfile = openfile.read() #reads the whole file character by charactrer, incl. \n
        sgdict = dict()

        regex_fastapattern = re.compile(fastapattern, re.VERBOSE) #'save' regex pattern for further use, already compiled
        fastapattern_iters = regex_fastapattern.finditer(str(readfile)) #applies pattern to fastafile

        for iterable in fastapattern_iters:
            sys = iterable.group('sys').replace('>', '').strip()
            triv = iterable.group('triv').strip()
            descr = iterable.group('descr').replace('\n', '').strip()
            seq = _stripline(iterable.group('seq'))
            prot_info = {'sys': sys, 'triv': triv, 'descr': descr, 'seq': seq}
            sgdict[sys] = prot_info
            sgdict[triv] = prot_info
    return sgdict

exampledata = #path
sgd = _sgdict(exampledata)

''' 
Tasks:

- check if protein 'HOG1' is in the list
- check if protein 'TFC3' is a subunit of RNA polymerase III transcription initiation complex
- print the first 10 aa of protein VPS8 and YAL003W 

:)
'''

