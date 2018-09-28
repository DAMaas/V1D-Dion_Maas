# Homework Lesson 6 - 4

import re

oldpassword = "admin"
newpassword = "root123321toor"


def new_password(oldpassword, newpassword):
    wachtwoordenZijnNietGelijkAanElkaar = newpassword != oldpassword
    nieuwWachtwoordLangGenoeg = len(newpassword) >= 6
    nieuwWachtwoordBevatNummer = bool(re.match('^(?=.*\d)', newpassword))
    res = wachtwoordenZijnNietGelijkAanElkaar and nieuwWachtwoordLangGenoeg and nieuwWachtwoordBevatNummer
    return res


print(new_password(oldpassword, newpassword))
