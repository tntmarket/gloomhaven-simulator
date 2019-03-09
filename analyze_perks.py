import matplotlib.pyplot as plt
import numpy as np

from simulate import simulate_games


def compare_perks(perks, attack_sequence, iterations):
    perk_results = [
        perk_result(perk_name, deck, attack_sequence, iterations) 
        for perk_name, deck in perks.items()
    ]
    
    plt.boxplot(
        [result['samples'] for result in perk_results],
        labels=[result['title'] for result in perk_results]
    )
    plt.title('Comparison of Perks')
    plt.xlabel('perk')
    plt.xticks(rotation=45)
    plt.ylabel('bonus damage')

    
def perk_result(perk_name, deck, attack_sequence, iterations): 
    damage_samples = np.array(simulate_games(deck, attack_sequence, iterations))
    mean_damage = damage_samples.mean()
    std_dev = damage_samples.std()/np.sqrt(iterations)
    return {
        'samples': [
            mean_damage - std_dev, 
            mean_damage, 
            mean_damage + std_dev,
        ],
        'title': '{perk_name}: {mean} σ {stddev}'.format(
            perk_name=perk_name,
            mean=round(mean_damage, 2),
            stddev=round(std_dev, 2),
        ),
    }
