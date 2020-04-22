import numpy as np

def get_odds(p):
    return p / (1 - p)

def get_inv_odds(p):
    return (1 - p) / p

def get_att_weight(df, p, outcome, treat):
    """ Get weighted ATT.
    
    Calculates the weighted ATT basd on a provided
    dataset and the propensity score.
    
    Args:
        df: A dataframe with the observed data.
        p: A numpy array with the weights.
        
    Returns:
        A float which corresponds to the ATT.
    """
    weights = get_odds(p)
    
    is_control = (df[treat] == 0)
    is_treated = (df[treat] == 1)
    value, weights = df[outcome][is_control], weights[is_control]
    att = df[outcome][is_treated].mean() - np.average(value, weights=weights)
    
    return att
    
def get_atc_weight(df, p, outcome, treat):
    """ Get weighted ATC.
    
    Calculates the weighted ATC basd on a provided
    dataset and the propensity score.
    
    Args:
        df: A dataframe with the observed data.
        p: A numpy array with the weights.
        
    Returns:
        A float which corresponds to the ATC.
    """
    weights = get_inv_odds(p)

    is_control = (df[treat] == 0)
    is_treated = (df[treat] == 1)

    value, weights = df[outcome][is_treated], weights[is_treated]
    atc = np.average(value, weights=weights) - df[outcome][is_control].mean()
    
    return atc

def get_ate_weight(df, p, outcome, treat):
    """ Get weighted ATE.
    
    Calculates the weighted ATE basd on a provided
    dataset and the propensity score.
    
    Args:
        df: A dataframe with the observed data.
        p: A numpy array with the weights.
        
    Returns:
        A float which corresponds to the ATE.
    """
    share_treated = df[treat].value_counts(normalize=True)[1]

    atc = get_atc_weight(df, p, outcome = outcome, treat = treat)
    att = get_att_weight(df, p, outcome = outcome, treat = treat)

    return share_treated * att + (1.0 - share_treated) * atc