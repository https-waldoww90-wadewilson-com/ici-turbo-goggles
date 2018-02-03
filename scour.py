from creatures import (
    glyptidotea,
    gnorimosphaeroma,
)

def scour():
    print "Found 'em in the back of the Mira!"
    print "----------------------------------"
    print "-", glyptidotea.Glyptidotea()
    print "-", gnorimosphaeroma.Gnorimosphaeroma()

if __name__ == '__main__':
    scour()
