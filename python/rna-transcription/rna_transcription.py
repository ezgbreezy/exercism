def to_rna(dna_strand: str) -> str:
    """Transcribes DNA strand to RNA strand.

    :param dna_stand: str - DNA stand to transcribe
    :return: str - transcribed RNA strand
    """

    # Create translation map
    rna_map = str.maketrans('CGTA', 'GCAU')

    return dna_strand.translate(rna_map)
