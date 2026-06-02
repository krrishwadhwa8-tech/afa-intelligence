def get_verdict(score):

    if score >= 70:
        return "Exceptional Technical Alignment"

    elif score >= 50:
        return "Strong Technical Alignment"

    elif score >= 25:
        return "Moderate Technical Alignment"

    return "Weak Technical Alignment"