# The six line version!

import pandas as pd

voter_file = pd.read_csv('voter_file_n5.csv')
voter_file['Voted'] = 'Yes'

voter_election_pivot = voter_file.pivot('Voter ID', 'Election')
voter_election_pivot = voter_election_pivot.fillna('No')

voter_election_pivot.to_csv('voter_election_pivot.csv')
