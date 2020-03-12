def to_rna(dna_strand):
    Code_rnd = {'A': 'U', 'G': 'C', 'C': 'G', 'T': 'A'}
    return ''.join([Code_rnd[i] for i in dna_strand])
