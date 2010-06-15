from ftruck.address import extract

def extraction():
    """
    >>> extract("Mojo chicken is brand new today at 14th and New York! Free sample! Check out the photos")
    '14th and New York'

    >>> extract("The especial is gone!! Sold out amigos!!") is None
    True

    >>> extract("L'Enfant, here we come! ETA 5 minutes!")
    'L\'Enfant Plaza Metro'

    >>> extract("Here at L'Enfant Plaza at the corner or Maryland and 7th! http://bit.ly/ctRX6B")
    'Maryland and 7th S.W.'
    
    >>> extract("Gonna head over and try my luck at with parking @ 1st & D SE")
    '1st & D S.E.'

    >>> extract("CORRECTION: We also have Gluten Free Chocolate and Vanilla http://bit.ly/9Tz61H") is None
    True
    
    >>> extract("McPherson Square, we're here on the corner of 15th & I. We're parked by an awning (sp) so you can stay dry! Come... http://bit.ly/cEFBCN")
    '15th & I N.W.'
    """
    pass