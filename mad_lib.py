def mad_lib():
    simple_mad_lib = "(Name) is having a (Theme) party! It's going to be at (A Place) on (Day of the week). Please make sure to show up at (Time), or else you will be required to (verb) a/an (Animal) with your (Body Part). RSVP at (Contact Information)."
    print(simple_mad_lib)
    _name = input("Please enter any Name: ")
    _theme = input("Please enter a Theme: ")
    a_place = input("Please enter A Place: ")
    day_of_the_week = input("Please enter Day of the week: ")
    _time = input("Please enter a Time: ")
    _verb = input("Please enter a verb: ")
    _animal = input("Place enter an Animal: ")
    body_part = input("Please enter a Body Part: ")
    contact_infmation = input("Please enter Contact Information: ")
    new_mab_lib = str(_name) + " is having a " + str(_theme) + "party! It's going to be at " + str(a_place) + " on " + str(day_of_the_week) + ". Please make sure to show up at  " + str(_time) + " , or else you will be required to " + str(_verb)+ " a/an " + str(_animal) + " with your" + str(body_part) + "." + "RSVP at " + str(contact_infmation) + "."
    print(new_mab_lib)

   
