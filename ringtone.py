class Ringtone(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def phone_ringing(self):
        for line in self.lyrics:
            print(line)

club = Ringtone([" Met her in the club",
                          "All the ballers showing love",
                          " Can you party with a thug -"])



                 
