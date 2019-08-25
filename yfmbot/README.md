# Yu-Gi-Oh! Forbidden Memories Farm Bot

## Descrição

Este é um simples bot que joga com alguns [personagens específicos](#personagens-disponíveis) para automatizar o processo de _farm_ no jogo, para ser possível ganhar cartas que são difíceis de conseguir.

## Personagens disponíveis

- Meadow Mage (Not implemented yet)
- Pegasus (Not implemented yet)
- Heishin (Not implemented yet)

## Comportamento dos personagens

### Meadow Mage

O Meadow Mage possui comportamentos de duelistas normais, sendo possível cometer erros como atacar monstros mais fortes que o que ele tem (quando a carta está setada para baixo) e ativar carta de campo (Sogen) sem monstros no campo. O objetivo com o duelo contra ele se tem pela qualidade das cartas que ele oferece quando se há uma vitória de rank alto (A-POW e S-POW), podendo oferecer as seguintes cartas:

- [Dark Magician](https://yugioh.fandom.com/wiki/Dark_Magician_(FMR)) (2500/2100)
- [Gaia the Fierce Knight](https://yugioh.fandom.com/wiki/Gaia_the_Fierce_Knight_(FMR)) (2300/2100)
- [Curse of Dragon](https://yugioh.fandom.com/wiki/Curse_of_Dragon_(FMR)) (2000/1500)
- [Kaminari Attack](https://yugioh.fandom.com/wiki/Kaminari_Attack_(FMR)) (1900/1400)
- [Skull Knight](https://yugioh.fandom.com/wiki/Skull_Knight_(FMR)) (2650/2250)
- [Meteor Dragon](https://yugioh.fandom.com/wiki/Meteor_Dragon_(FMR)) (1800/2000)
- [Meteor B. Dragon](https://yugioh.fandom.com/wiki/Meteor_B._Dragon_(FMR)) (3500/2000)
- [Firewing Pegasus](https://yugioh.fandom.com/wiki/Firewing_Pegasus_(FMR)) (2250/1800)

Para o duelo contra ele, o bot tentará sempre realizar alguma fusão (ou combo) que consiga ultrapassar as principais cartas dele. Ele também precisa tomar cuidado com os combos preparados pelo Meadow Mage, sendo eles:

- [Sogen](https://yugioh.fandom.com/wiki/Sogen_(FMR)) + [Millenium Shield](https://yugioh.fandom.com/wiki/Millennium_Shield_(FMR)) (500/3500)
- [Sogen](https://yugioh.fandom.com/wiki/Sogen_(FMR)) + Qualquer guerreiro (na média de 2000 à 2500 de atk)
- [Sogen](https://yugioh.fandom.com/wiki/Sogen_(FMR)) + [Judge Man](https://yugioh.fandom.com/wiki/Judge_Man_(FMR)) (2700/2000)
- [Sogen](https://yugioh.fandom.com/wiki/Sogen_(FMR)) + [Empress Judge](https://yugioh.fandom.com/wiki/Empress_Judge_(FMR)) (2600/2200)

#### Observações

O guardião do Millenium Shield será sempre Uranos, sendo forte contra a carta principal a ser possível fusionar: Twin-Headed Thunder Dragon (2800/2100), onde ele pode ser Pluto (Fraco contra Uranos), ou Moon (Fraco contra Sun). Logo, com o Sogen no campo, é grande a chance do duelo falhar caso não seja usado algum recurso para eliminar as principais cartas dele: Millenium Shield, Judge Man e Empress Judge (que podem ocasionar problemas relacionados ao ranking e até ao estado do duelo).

## Comportamento do Bot

O bot precisa estar atento tanto nas cartas principais citadas acima quanto nos guardiões relacionado as cartas setadas pelo oponente, sabendo os momentos necessários para atacar ou até arriscar um ataque, realizando fusões de acordo com a base de dados de combos, fusões e equipes, realizando uma análise de qual o melhor movimenento para determinado caso.

## Description

This simple bot have to be able to play with some [specifics characters](#characters-available) to automate the farm process,to be able to earn cards that are hard to get.

## Characters available

- Meadow Mage (Not implemented yet)
- Pegasus (Not implemented yet)
- Heishin (Not implemented yet)

## Bot Behaviour

The bot needs to be aware of both the main cards of each characters and the guardians related to the cards set by the opponent, knowing the moments required to attack or even risk an attack, performing mergers according to the combos, mergers and teams database, performing an analysis of what is the best move for a given case.
