from rabbit import Rabbit
from wolf import Wolf
        


if __name__ == '__main__':
    wolf = Wolf()
    rabbit1 = Rabbit()
    rabbit2 = Rabbit()

    wolf.start((rabbit1, rabbit2))  