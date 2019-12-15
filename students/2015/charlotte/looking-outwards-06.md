#Looking Outwards 6

## Experiments in Map Generation using Markov Chains

[Link to article](http://www.fdg2014.org/papers/fdg2014_paper_29.pdf)

Authors: Sam Snodgrass & Santiago Ontañón from Drexel University



![link](images/ssb.png)

In this paper they used a matrix representation of a Super Smash Bro level and ran > 5000 levels through the learning software.
They determined if the level was playable using the 2009 Mario AI competition software, which is an automatic mario playing software that is not so apt to get out of crevases. They got that 44% of the maps they created were playable.

Concerning Markov chain training, the paper presents and explores the idea of learning higher-order Markov chains based on a dependency matrix, which captures the dependencies between the tiles in the map.

Higher order Markov chains in order to learn the probabilistic distribution of tiles in a given set of maps. In order to learn the Markov chain, it is needed to specify the Bayesian network structure. For example, we could learn a Markov chain defined by the probability of one tile in the map given the previous horizontal tile, or we could learn another one defined by the probability of a tile given the previous tile horizontally and the tile immediately above, etc. Automatically learning the structure of a Bayesian network is a well known hard problem, finally they configure the dependencies by hand.