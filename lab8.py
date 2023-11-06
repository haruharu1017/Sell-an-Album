class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def printItem(self):
        return ('{}/{}/{}'.format(self.month, self.day, self.year))

# date = Date(10, 17, 2004)
# date.printItem()


class Item:
    def __init__(self, name, singer, price, content, date):
        self.name = name
        self.singer = singer
        self.price = price
        self.content = content
        self.date = date.printItem()

    def printItem(self):
        print('Item: {}, by {} for ${}'.format(self.name, self.singer, self.price))
        ans = input('Would you like to "purchase", see more "details", or "pass"?')

        if ans == 'details':
            co = ''
            for i in self.content:
                co += i + ' '
            print('Name: {}, by {}\nPrice: {}\nContents: {}\nReleased: {}'.format(self.name, self.singer, self.price, co, self.date))
            ans_1 = input('Would you like to "purchase", or "pass"?')
            if ans_1 == 'purchase':
                self.price = self.price
            elif ans_1 == 'pass':
                self.price = 0
        elif ans == 'purchase':
            self.price = self.price
        elif ans == 'pass':
            self.price = 0



def fillCart(item):
    total_price = 0
    for i in item:
        total_price += i.price
    return total_price



sl_5 = Item("Slaughterhouse 5", "Kurt Vonnegut", 7.99, [], Date(3, 31, 1969))

tracks_r = ["I Will Dare", "Favorite Thing", "We're Comin' Out","Tommy Gets His Tonsils Out","Androgynous","Black Diamond","Unsatisfied","Seen Your Video","Gary's Got","Sixteen Blue","Answering Machine"]
let_it_be_replacements = Item( "Let it Be", "The Replacements", 11.49,tracks_r,Date(10, 2, 1984))

tracks_b = ["Two Of Us", "Dig A Pony","Across The Universe","I Me Mine","Dig It","Let It Be","Maggie Mae","I've Got A Feeling","One After 909", "The Long And Winding Road","For You Blue","Get Back"]

let_it_be_beatles = Item("Let it Be", "The Beatles", 16.29, tracks_b, Date(5, 11,1970))

sl_5.printItem()
let_it_be_replacements.printItem()
let_it_be_beatles.printItem()


cost = fillCart([sl_5, let_it_be_replacements, let_it_be_beatles])
print("Total cost: ", cost)

