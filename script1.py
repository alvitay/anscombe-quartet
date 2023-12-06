import seaborn as sns
import seaborn.objects as so


anscombe = sns.load_dataset('anscombe')

print(anscombe.head())
print(
    anscombe
    .groupby('dataset')
    .agg(['mean', 'std'])


)
(
    so.Plot(
        anscombe,
        x='x',
        y='y',
        
    )
    .add(so.Dot())
    .facet('dataset',wrap=2)
    .save("./figures/plot.png", dpi=200)

)