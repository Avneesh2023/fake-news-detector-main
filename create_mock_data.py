import pandas as pd

data = {
    'title': ['Real News 1', 'Fake News 1', 'Real News 2', 'Fake News 2', 'Real News 3', 'Fake News 3', 'Real News 4', 'Fake News 4', 'Real News 5', 'Fake News 5'],
    'text': [
        'The quick brown fox jumps over the lazy dog. The economy is doing well today with stocks rising.',
        'Aliens have landed in New York. The government is hiding them in secret underground bunkers.',
        'Scientists have discovered a new species of frog in the Amazon rainforest.',
        'Drinking bleach cures all diseases, a new fake study claims without any evidence.',
        'The local sports team won the championship game last night by a score of 3 to 1.',
        'The earth is actually flat and space is a projection on a giant dome.',
        'A new law was passed yesterday that will lower taxes for small businesses.',
        'Zombies are attacking the city center, people are running for their lives.',
        'The mayor inaugurated a new public park downtown this morning.',
        'Water makes you shrink! Avoid drinking water at all costs.'
    ],
    'label': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)
df.to_csv('train.csv', index=False)
print("Mock train.csv created.")
