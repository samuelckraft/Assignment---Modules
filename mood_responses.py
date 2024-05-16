def mood_responses(mood):
    good = ['happy', 'glad', 'good', 'excited']
    bad = ['sad', 'bad', 'mad','upset', 'angry']
    if mood in good:
        return "Yay it's gonna be a great day"
    elif mood in bad:
        return "Oh I'm sorry I hope you feel better"
    else:
        return "Invalid mood please try again"