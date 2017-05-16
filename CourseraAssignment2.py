def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)

def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    if len(dna1)>len(dna2):
            return True
    else:
            return False


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna1.count(dna2)>=1

def is_valid_sequence(DNA=''):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid.
    That is contains no characters other than 'A','T','C','G'.
    
    >>> is_valid_sequence('AAAAAA')
    True
    >>> is_valid_sequence('ATCTA')
    True
    >>> is_valid_sequence('aTCTA')
    False
    >>> is_valid_sequence('2TCTA')
    False
    >>> is_valid_sequence('YTCA')
    False
    >>> is_valid_sequence('TCAQ')
    False
    >>> is_valid_sequence()
    True
"""   
    valid=True
    
    if DNA!='':
        for i in DNA:
            if (i!='A') and (i!='T') and (i!='C') and (i!='G'):
                valid=False
    else:
        valid=True
        
    return(valid)

def insert_sequence(dna1,dna2,index):
    """(str, str, int) -> str

    Return the DNA sequence obtained by inserting
    the second DNA sequence into the first DNA
    sequence at the given index.
    

    >>> insert_sequence('CCGG','AT',2)
    'CCATGG'
    >>> insert_sequence('CCGG','AT',0)
    'ATCCGG'
    >>> insert_sequence('CCGG','AT',4)
    'CCGGAT'
    >>> insert_sequence('CCGG','AT',3)
    'CCGGAT'
"""
   
    return(dna1[0:index]+dna2+dna1[index:])

def get_complement(nuc):
    """(str) -> str

    Return the nucleotide's complement.
    

    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('G')
    'C'
    >>> get_complement('Y')
    ''
"""
    if nuc=='A':
        return 'T'
    elif nuc=='T':
        return 'A'
    elif nuc=='G':
        return 'C'
    elif nuc=='C':
        return 'G'
    else:
        return ''

def get_complementary_sequence(dna=''):
    """(str) -> str

    Return the DNA sequence that is
    complementary to the given DNA sequence. 
    

    >>> get_complementary_sequence('ATA')
    'TAT'
    >>> get_complementary_sequence('CGTA')
    'GCAT'
    >>> get_complementary_sequence('CCGGTAT')
    'GGCCATA'
    >>> get_complementary_sequence('CCGYA')
    ''
"""
    comp=''
    if len(dna)>0:
        for i in dna:
            if i=='A':
                comp=comp+'T'
            elif i=='T':
                comp=comp+'A'
            elif i=='G':
                comp=comp+'C'
            elif i=='C':
                comp=comp+'G'
            else:
                return('')
  
    return(comp)

