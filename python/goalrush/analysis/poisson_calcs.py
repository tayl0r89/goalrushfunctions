from scipy.stats import poisson

def home_win_probability(FTHG, FTAG):        # a function to calculate the probability of a home win
    """ a function to calculate the probability of a home win"""

    probability = 0

    for i in range(10):
        for j in range(10):
            if i > j:
                scoreProbability = poisson.pmf(i, FTHG) * poisson.pmf(j, FTAG)
                probability = probability + scoreProbability

    return probability

def away_win_probability(FTHG, FTAG):        # a function to calculate the probability of an away win
    """ a function to calculate the probability of an away win"""

    probability = 0

    for i in range(10):
        for j in range(10):
            if i < j:
                scoreProbability = poisson.pmf(i, FTHG) * poisson.pmf(j, FTAG)
                probability = probability + scoreProbability

    return probability

def draw_probability(FTHG, FTAG):        # a function to calculate the probability of a draw
    """ a function to calculate the probability of a draw"""

    probability = 0

    for i in range(10):
        for j in range(10):
            if i == j:
                scoreProbability = poisson.pmf(i, FTHG) * poisson.pmf(j, FTAG)
                probability = probability + scoreProbability

    return probability

def score_draw_probability(FTHG, FTAG):        # a function to calculate the probability of a score draw
    """ a function to calculate the probability of a score draw"""

    probability = 0

    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                scoreProbability = poisson.pmf(i, FTHG) * poisson.pmf(j, FTAG)
                probability = probability + scoreProbability

    return probability

def under_x_goals_probability(FTHG, FTAG, x = 2.5):        # a function to calculate probability total game goals less than x based on HexpG and AexpG
    """ a function to calculate probability total game goals less than x based on HexpG and AexpG"""

    probability = 0

    for i in range(10):
        for j in range(10):
            if (i + j) < x:
                scoreProbability = poisson.pmf(i, FTHG) * poisson.pmf(j, FTAG)
                probability = probability + scoreProbability

    return probability

def btts_probability(FTHG, FTAG):        # a function to calculate probability both teams score based on HexpG and AexpG
    """ a function to calculate probability both teams score based on HexpG and AexpG"""

    homeProbability = 1 - poisson.pmf(0, FTHG)
    awayProbability = 1 - poisson.pmf(0, FTAG)
    
    return (homeProbability * awayProbability)

def home_win_to_nil_probability(FTHG, FTAG):        # a function to calculate probability the home team wins to nil based on HexpG and AexpG
    """ a function to calculate probability the home team wins to nil based on HexpG and AexpG"""

    probability = 0

    for i in range(1, 10):
        
        scoreProbability = poisson.pmf(i, FTHG) * poisson.pmf(0, FTAG)
        probability = probability + scoreProbability

    return probability

def away_win_to_nil_probability(FTHG, FTAG):        # a function to calculate probability the away team wins to nil based on HexpG and AexpG
    """ a function to calculate probability the away team wins to nil based on HexpG and AexpG"""

    probability = 0

    for j in range(1, 10):
        
        scoreProbability = poisson.pmf(0, FTHG) * poisson.pmf(j, FTAG)
        probability = probability + scoreProbability

    return probability

def home_win_btts_probability(FTHG, FTAG):        # a function to calculate probability the home team wins and btts based on HexpG and AexpG
    """ a function to calculate probability the home team wins and btts based on HexpG and AexpG"""

    probability = 0
    
    for i in range(10):
        for j in range(10):
            if i > j and j > 0:
                scoreProbability = poisson.pmf(i, FTHG) * poisson.pmf(j, FTAG)
                probability = probability + scoreProbability

    return probability

def away_win_btts_probability(FTHG, FTAG):        # a function to calculate probability the away team wins and btts based on HexpG and AexpG
    """ a function to calculate probability the away team wins and btts based on HexpG and AexpG"""

    probability = 0
    
    for i in range(10):
        for j in range(10):
            if i < j and i > 0:
                scoreProbability = poisson.pmf(i, FTHG) * poisson.pmf(j, FTAG)
                probability = probability + scoreProbability

    return probability
