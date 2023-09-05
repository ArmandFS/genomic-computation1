import random
import numpy as np
import streamlit as st

DNA_Sequences = {
    "Isoleucine": {
        "Codon": ['ATT', 'ATC', 'ATA'],
        "Single_Letter": "I"
    },
    "Leucine": {
        "Codon": ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'],
        "Single_Letter": "L"
    },
    "Valine": {
        "Codon": ['GTT', 'GTC', 'GTA', 'GTG'],
        "Single_Letter": "V"
    },
    "Phenylalanine": {
        "Codon": ['TTT', 'TTC'],
        "Single_Letter": "F"
    },
    "Methionine": {
        "Codon": ['ATG'],
        "Single_Letter": "M"
    },
    "Cysteine": {
        "Codon": ['TGT', 'TGC'],
        "Single_Letter": "C"
    },
    "Alanine": {
        "Codon": ['GCT', 'GCC', 'GCA', 'GCG'],
        "Single_Letter": "A"
    },
    "Glycine": {
        "Codon": ['GGT', 'GGC', 'GGA', 'GGG'],
        "Single_Letter": "G"
    },
    "Proline": {
        "Codon": ['CCT', 'CCC', 'CCA', 'CCG'],
        "Single_Letter": "P"
    },
    "Threonine": {
        "Codon": ['ACT', 'ACC', 'ACA', 'ACG'],
        "Single_Letter": "T"
    },
    "Serine": {
        "Codon": ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
        "Single_Letter": "S"
    },
    "Tyrosine": {
        "Codon": ['TAT', 'TAC'],
        "Single_Letter": "Y"
    },
    "Tryptophan": {
        "Codon": ['TGG'],
        "Single_Letter": "V"
    },
    "Glutamine": {
        "Codon": ['CAA', 'CAG'],
        "Single_Letter": "Q"
    },
    "Asparagine": {
        "Codon": ['AAT', 'AAC'],
        "Single_Letter": "N"
    },
    "Histidine": {
        "Codon": ['CAT', 'CAC'],
        "Single_Letter": "H"
    },
    "Glutamic acid": {
        "Codon": ['GAA', 'GAG'],
        "Single_Letter": "E"
    },
    "Aspartic acid": {
        "Codon": ['GAT', 'GAC'],
        "Single_Letter": "D"
    },
    "Lysine": {
        "Codon": ['AAA', 'AAG'],
        "Single_Letter": "K"
    },
    "Arginine": {
        "Codon": ['CGT', 'CGC', 'CGA', 'AGA', 'AGG'],
        "Single_Letter": "R"
    },
    "Stop Codon": {
        "Codon": ['TAA', 'TAG', 'TGA'],
        "Single_Letter": "Stop"
    }
}


#create a function for randomizing generated sequence
def gen_random_sequence(sequence_type, nitrogen_base, num_sequences):
    #create the random sequence inside a list
    random_sequence = []
    for i in range(0, num_sequences):
        number = random.randint(0, len(nitrogen_base) - 1)
        if sequence_type == "RNA" and number == 3:
            number = 4
        elif sequence_type == "DNA" and number == 4:
            number = 3
        random_sequence.append(nitrogen_base[number])
    return random_sequence

#create a function to split the sequence into codons
def codon_split(random_sequence):
    split_sequence = []
    current_string = ""
    for base in random_sequence:
        current_string += base
        if len(current_string) == 3:
            split_sequence.append(current_string)
            current_string = ""
    return split_sequence

#mapping function to amino acids
def map_amino(split_sequence, DNA_Sequences):
    for base in split_sequence:
        for amino_acid, data in DNA_Sequences.items():
            if base in data["Codon"]:
                st.write(f"Codon {base}: {amino_acid} ({data['Single_Letter']})")
                
                
def main():
    purines = ["A", "G"]
    pyrimidines = ["C", "T", "U"]
    nitrogen_base = purines + pyrimidines
    st.title("Komputasi Genomik_Assignment 1_Armand Faris A Surbakti_5023201051")
    
    select = st.radio("Select an RNA or DNA sequence.", ("DNA", "RNA"))
    num_sequences = st.number_input("Manually Enter the Number of Sequences: ", min_value=3, step=3)
    random_sequence = gen_random_sequence(select, nitrogen_base, num_sequences)
    
    
    if  st.button("Run Sequencing"):
        st.subheader("Generated Output Sequence")
        st.write("".join(random_sequence))
        
        if select == "RNA":
           random_sequence = [base if base != "U" else "T" for base in random_sequence]
            
        split_sequence = codon_split(random_sequence)

        st.subheader("Split Sequence into Codons")
        st.write(split_sequence)

        st.subheader("Codon to Amino Acid Mapping")
        map_amino(split_sequence, DNA_Sequences) 
        
if __name__ == "__main__":
    main()
