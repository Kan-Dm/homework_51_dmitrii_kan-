from random import randint


class CatDB:
    name = None
    age = 1
    satiety_level = 40
    mood_level = 40
    is_sleeping = False
    cat_photo = '/static/img/cat.jpg'
    sad_cat_photo = '/static/img/sad_cat.jpg'
    happy_cat_photo = '/static/img/happy_cat.jpg'

    @classmethod
    def choose_photo(cls):
        if 40 < cls.mood_level < 60:
            return cls.cat_photo
        elif cls.mood_level <= 40:
            return cls.sad_cat_photo
        elif cls.mood_level >= 60:
            return cls.happy_cat_photo

    @classmethod
    def to_dict(cls):
        return {'name': cls.name, 'age': cls.age, 'satiety_level': cls.check_characteristic_level(cls.satiety_level),
                'mood_level': cls.check_characteristic_level(cls.mood_level), 'cat_photo': cls.choose_photo()}

    @classmethod
    def choose_action(cls, action):
        if action == 'play':
            cls.play_cat()
        elif action == 'sleep':
            cls.sleep()
        elif action == 'feed':
            cls.feed_cat()

    @classmethod
    def feed_cat(cls):
        if not cls.is_sleeping:
            if cls.satiety_level <= 100:
                cls.satiety_level += 15
                cls.mood_level += 5
            elif cls.satiety_level > 100:
                cls.mood_level -= 30

    @classmethod
    def play_cat(cls):
        angry = randint(1, 3)
        if not cls.is_sleeping:
            if angry != 1:
                cls.mood_level += 15
                cls.satiety_level -= 10
            else:
                cls.mood_level = 0
                cls.satiety_level -= 10
        elif cls.is_sleeping:
            if angry != 1:
                cls.is_sleeping = False
                cls.mood_level -= 5
                cls.satiety_level -= 10
            else:
                cls.is_sleeping = False
                cls.mood_level = 0
                cls.satiety_level -= 10

    @classmethod
    def sleep(cls):
        cls.is_sleeping = True

    @classmethod
    def check_characteristic_level(cls, characteristic):
        if characteristic > 100:
            return 100
        elif characteristic < 0:
            return 0
        else:
            return characteristic
