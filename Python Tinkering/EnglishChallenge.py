#Listening Test found at http://www.codeskulptor.org/#user35_RmD2iS0xIL4jF6H.py

import simplegui
import random

CARD_SIZE = (80, 100)
CARD_CENTER = (40, 50)
CARDS_PER_ROW_IMAGE = 20
ROWS_IN_IMAGE = 12
card_images0 = simplegui.load_image("https://dl.dropboxusercontent.com/u/13961479/ListeningTest2.png")
card_images1 = simplegui.load_image("https://dl.dropboxusercontent.com/u/13961479/ListeningTest1.png")

# initialize some useful global variables
turn_done = False
correct_cards = []
sounds = []
turns_taken = 2
score = 0
level = 0
past_score = 2
score_variance = 2
player_message = ""
language = "English"
challenge_mode = "Listening"

# initialize constants
CARDS_IN_ROW = 10
ROWS_ON_BOARD = 6
TOP_GAP = 50
WIDTH = (CARD_SIZE[0] * (CARDS_IN_ROW))
HEIGHT = ((CARD_SIZE[1] * ROWS_ON_BOARD) + TOP_GAP)

# Soundbites
sound_of_success = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Cheer.mp3")
sound_of_failure = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Buzzer.mp3")
ice_cream = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Ice%20Cream.m4a")
juice = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Juice.m4a")
kangaroo = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Kangaroo.m4a")
octopus = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Octopus.m4a")
queen = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Queen.m4a")
raccoon = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Raccoon.m4a")
shoes = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Shoes.m4a")
socks = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Socks.m4a")
violin = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Violin.m4a")
fox = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Fox.m4a")
yogurt = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Yogurt.m4a")
zebra = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Zebra.m4a")
go = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Go.m4a")
come = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Come.m4a")
walk = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Walk.m4a")
run = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Run.m4a")
sleep = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Sleep.m4a")
stand = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Stand.m4a")
wake_up = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Wake%20Up.m4a")
ear = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Ear.m4a")
hand = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Hand.m4a")
nose = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Nose.m4a")
feet = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Feet.m4a")
eyes = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Eyes.m4a")
bird = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Bird.m4a")
cat = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Cat.m4a")
dog = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Dog.m4a")
elephant = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Elephant.m4a")
fish = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Fish.m4a")
lion = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Lion.m4a")
monkey = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Monkey.m4a")
snake = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Snake.m4a")
tiger = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Tiger.m4a")
speak = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Speak.m4a")
one = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/One.m4a")
two = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Two.m4a")
three = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Three.m4a")
four = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Four.m4a")
five = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Five.m4a")
six = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Six.m4a")
seven = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Seven.m4a")
eight = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Eight.m4a")
nine = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Nine.m4a")
ten = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Ten.m4a")
eleven = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Eleven.m4a")
twelve = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Twelve.m4a")
thirteen = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Thirteen.m4a")
fourteen = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Fourteen.m4a")
fifteen = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Fifteen.m4a")
sixteen = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Sixteen.m4a")
seventeen = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Seventeen.m4a")
eighteen = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Eighteen.m4a")
nineteen = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Nineteen.m4a")
twenty = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Twenty.m4a")
turn_right = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Turn%20Right.m4a")
turn_left = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Turn%20Left.m4a")
stop = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Stop.m4a")
go_straight = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Go%20Straight.m4a")
coat = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Coat.m4a")
saturday = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Saturday.m4a")
swimsuit = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Swimsuit.m4a")
tshirt = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/T-shirt.m4a")
shorts = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Shorts.m4a")
tie = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Tie.m4a")
turtleneck = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Turtleneck.m4a")
gloves = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Gloves.m4a")
underwear = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Underwear.m4a")
drums = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Drums.m4a")
guitar = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Guitar.m4a")
harmonica = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Harmonica.m4a")
pianica = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Pianica.m4a")
piano = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Piano.m4a")
recorder = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Recorder.m4a")
saxophone = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Saxophone.m4a")
shamisen = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Shamisen.m4a")
trombone = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Trombone.m4a")
trumpet = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Trumpet.m4a")
tuba = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Tuba.m4a")
october = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/October.m4a")
social_studies = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Social%20Studies.m4a")
shop_class = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Shop%20Class.m4a")
science = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Science.m4a")
recess = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Recess.m4a")
gym_class = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Gym%20Class.m4a")
music = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Music.m4a")
math = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Math.m4a")
lunch_time = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Lunch%20Time.m4a")
japanese = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Japanese.m4a")
home_ec = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Home%20Ec.m4a")
english = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/English.m4a")
cleaning_time = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Cleaning%20Time.m4a")
art = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Art.m4a")
after_school = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/After%20School.m4a")
work = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Work.m4a")
study = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Study.m4a")
sing = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Sing.m4a")
shower = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Shower.m4a")
play = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Play.m4a")
laugh = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Laugh.m4a")
drink = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Drink.m4a")
dance = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Dance.m4a")
cry = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Cry.m4a")
cook = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Cook.m4a")
climb = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Climb.m4a")
clean = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Clean.m4a")
wednesday = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Wednesday.m4a")
thursday = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Thursday.m4a")
sunday = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Sunday.m4a")
monday = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Monday.m4a")
yesterday = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Yesterday.m4a")
tomorrow = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Tomorrow.m4a")
today = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Today.m4a")
friday = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Friday.m4a")
tuesday = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Tuesday.m4a")
september = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/September.m4a")
november = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/November.m4a")
may = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/May.m4a")
march = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/March.m4a")
june = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/June.m4a")
july = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/July.m4a")
january = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/January.m4a")
february = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/February.m4a")
december = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/December.m4a")
august = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/August.m4a")
april = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/April.m4a")
weak = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Weak.m4a")
tall = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Tall.m4a")
strong = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Strong.m4a")
slow = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Slow.m4a")
short_length = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Short%20Length.m4a")
old_person = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Old%20Person.m4a")
old_thing = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Old%20Thing.m4a")
new = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/New.m4a")
long1 = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Long.m4a")
light_weight = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Light%20Weight.m4a")
heavy = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Heavy.m4a")
fast = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Fast.m4a")
up = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Up.m4a")
right = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Right.m4a")
left = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Left.m4a")
down = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Down.m4a")
zombie = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Zombie.m4a")
witch = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Witch.m4a")
vampire = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Vampire.m4a")
spider_web = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Spider%20Web.m4a")
skeleton = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Skeleton.m4a")
pumpkin = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Pumpkin.m4a")
haunted_house = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Haunted%20House.m4a")
costume = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Costume.m4a")
candy = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Candy.m4a")
mouth = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Mouth.m4a")
hair = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Hair.m4a")
dirty = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Dirty.m4a")
penguin = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Penguin.m4a")
panda = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Panda.m4a")
horse = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Horse.m4a")
cow = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Cow.m4a")
chicken = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Chicken.m4a")
write = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Write.m4a")
wear = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Wear.m4a")
use = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Use.m4a")
touch = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Touch.m4a")
think = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Think.m4a")
swim = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Swim.m4a")
young = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Young.m4a")
ghost = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Ghost.m4a")
jump = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Jump.m4a")
eat = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Eat.m4a")
pig = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Pig.m4a")
spider = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Spider.m4a")
read = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Read.m4a")
push = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Push.m4a")
practice = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Practice.m4a")
paint = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Paint.m4a")
listen = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Listen.m4a")
help1 = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Help.m4a")
fly = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Fly.m4a")
fall = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Fall.m4a")
drive = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Drive.m4a")
draw1 = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Draw.m4a")
catch = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Catch.m4a")
can_swim = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Can%20Swim.m4a")
can_cook = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Can%20Cook.m4a")
cant_swim = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Can't%20Swim.m4a")
cant_cook = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Can't%20Cook.m4a")
ask = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Ask.m4a")
volleyball = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Volleyball.m4a")
track_and_field = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Track%20And%20Field.m4a")
tennis = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Tennis.m4a")
table_tennis = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Table%20Tennis.m4a")
speed_skate = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Speed%20Skate.m4a")
soccer = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Soccer.m4a")
snowboard = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Snowboard.m4a")
ski = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Ski.m4a")
rugby = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Rugby.m4a")
kendo = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Kendo.m4a")
judo = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Judo.m4a")
hockey = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Hockey.m4a")
figure_skate = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Figure%20Skate.m4a")
basketball = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Basketball.m4a")
baseball = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Baseball.m4a")
badminton = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Badminton.m4a")
show = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Show.m4a")
search = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Search.m4a")
remember = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Remember.m4a")
open1 = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Open.m4a")
forget = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Forget.m4a")
carry = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Carry.m4a")
call = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Call.m4a")
move = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Move.m4a")
red = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Red.m4a")
orange = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Orange.m4a")
yellow = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Yellow.m4a")
light_green = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Light%20Green.m4a")
green = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Green.m4a")
dark_green = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Dark%20Green.m4a")
light_blue = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Light%20Blue.m4a")
blue = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Blue.m4a")
dark_blue = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Dark%20Blue.m4a")
purple = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Purple.m4a")
white = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/White.m4a")
light_gray = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Light%20Gray.m4a")
gray = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Gray.m4a")
dark_gray = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Dark%20Gray.m4a")
black = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Black.m4a")
brown = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Brown.m4a")
pink = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Pink.m4a")
surprised = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Surprised.m4a")
embarrassed = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Embarassed.m4a")
scared = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Scared.m4a")
sad = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Sad.m4a")
mad = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Mad.m4a")
good = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Good.m4a")
bad = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Bad.m4a")
confused = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Confused.m4a")
bored = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Bored.m4a")
circle = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Circle.m4a")
square = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Square.m4a")
rectangle = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Rectangle.m4a")
oval = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Oval.m4a")
triangle = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Triangle.m4a")
star = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Star.m4a")
heart = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Heart.m4a")
diamond = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Diamond.m4a")
zoo = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Zoo.m4a")
train_station = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Train%20Station.m4a")
subway_station = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Subway%20Station.m4a")
stadium = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Stadium.m4a")
school = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/School.m4a")
museum = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Museum.m4a")
movie_theater = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Movie%20Theater.m4a")
library = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Library.m4a")
hospital = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Hospital.m4a")
art_gallery = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Art%20Gallery.m4a")
aquarium = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Aquarium.m4a")
amusement_park = simplegui.load_sound("https://dl.dropboxusercontent.com/u/13961479/Amusement%20Park.m4a")

# define globals for card pics
PICTURES = (card_images0, card_images1)

# define globals for cards
WORDS = ("ice cream", "juice", "kangaroo", "octopus", "queen", "raccoon", "shoes", "socks", "violin", "fox",
         "yogurt", "zebra", "go", "come", "walk", "run", "sleep", "stand", "wake up", "ear",
         "hand", "nose", "feet", "eyes", "bird", "cat", "dog", "elephant", "fish", "lion",
         "monkey", "snake", "tiger", "speak", "one", "two", "three", "four", "five", "six",
         "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
         "seventeen", "eighteen", "nineteen", "twenty", "turn right", "turn left", "stop", "go straight", "coat", "Saturday",
         "swimsuit", "T-shirt", "shorts", "tie", "turtleneck", "gloves", "underwear", "drums", "guitar", "harmonica",
         "pianica", "piano", "recorder", "saxophone", "shamisen", "trombone", "trumpet", "tuba", "October", "social studies",
         "shop class", "science", "recess", "gym class", "music", "math", "lunch time", "Japanese", "home ec", "English",
         "cleaning time", "art", "after school", "work", "study", "sing", "shower", "play", "laugh", "drink",
         "dance", "cry", "cook", "climb", "clean", "Wednesday", "Thursday", "Sunday", "Monday", "yesterday",
         "tomorrow", "today", "Friday", "Tuesday", "September", "November", "May", "March", "June", "July",
         "January", "February", "Decemeber", "August", "April", "weak", "tall", "strong", "slow", "short length",
         "old person", "old thing", "new", "long", "light weight", "heavy", "fast", "up", "right", "left",
         "down", "zombie", "witch", "vampire", "spider web", "skeleton", "pumpkin", "haunted house", "costume", "candy",
         "mouth", "hair", "dirty", "penguin", "panda", "horse", "cow", "chicken", "write", "wear",
         "use a computer", "touch", "think", "swim", "young", "ghost", "jump", "eat", "pig", "spider",
         "read", "push", "practice", "paint", "listen", "help", "fly", "fall", "drive", "draw",
         "catch", "can swim", "can cook", "can't swim", "can't cook", "ask", "play volleyball", "do track and field", "play tennis", "play table tennis",
         "speed skate", "play soccer", "snowboard", "ski", "play rugby", "do kendo", "do judo", "play hockey", "figure skate", "play basketball",
         "play baseball", "play badminton", "show a drawing", "search", "remember", "open a door", "forget", "carry some bags", "call", "move",
         "red", "orange", "yellow", "light green", "green", "dark green", "light blue", "blue", "dark blue", "purple",
         "white", "light gray", "gray", "dark gray", "black", "brown", "pink", "surprised", "embarrassed", "scared",
         "sad", "mad", "good", "bad", "confused", "bored", "circle", "square", "rectangle", "oval",
         "triangle", "star", "heart", "diamond", "zoo", "train station", "subway station", "stadium", "school", "museum",
         "movie theater", "library", "hospital", "art gallery", "aquarium", "amusement park")


# define canvas size
CANVAS_SIZE = [WIDTH, HEIGHT]

# define english sounds class
class EnglishSounds:
    def __init__(self):
        self.sounds = (ice_cream, juice, kangaroo, octopus, queen, raccoon, shoes, socks, violin, fox,
         yogurt, zebra, go, come, walk, run, sleep, stand, wake_up, ear,
         hand, nose, feet, eyes, bird, cat, dog, elephant, fish, lion,
         monkey, snake, tiger, speak, one, two, three, four, five, six,
         seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen,
         seventeen, eighteen, nineteen, twenty, turn_right, turn_left, stop, go_straight, coat, saturday,
         swimsuit, tshirt, shorts, tie, turtleneck, gloves, underwear, drums, guitar, harmonica, pianica,
         piano, recorder, saxophone, shamisen, trombone, trumpet, tuba, october, social_studies,
         shop_class, science, recess, gym_class, music, math, lunch_time, japanese, home_ec, english,
         cleaning_time, art, after_school, work, study, sing, shower, play, laugh, drink,
         dance, cry, cook, climb, clean, wednesday, thursday, sunday, monday, yesterday,
         tomorrow, today, friday, tuesday, september, november, may, march, june, july,
         january, february, december, august, april, weak, tall, strong, slow, short_length,
         old_person, old_thing, new, long1, light_weight, heavy, fast, up, right, left, down,
         zombie, witch, vampire, spider_web, skeleton, pumpkin, haunted_house, costume, candy,
         mouth, hair, dirty, penguin, panda, horse, cow, chicken, write, wear,
         use, touch, think, swim, young, ghost, jump, eat, pig, spider,
         read, push, practice, paint, listen, help1, fly, fall, drive, draw1,
         catch, can_swim, can_cook, cant_swim, cant_cook, ask, volleyball, track_and_field, tennis, table_tennis,
         speed_skate, soccer, snowboard, ski, rugby, kendo, judo, hockey, figure_skate, basketball,
         baseball, badminton, show, search, remember, open1, forget, carry, call, move,
         red, orange, yellow, light_green, green, dark_green, light_blue, blue, dark_blue, purple,
         white, light_gray, gray, dark_gray, black, brown, pink, surprised, embarrassed, scared,
         sad, mad, good, bad, confused, bored, circle, square, rectangle, oval,
         triangle, star, heart, diamond, zoo, train_station, subway_station, stadium, school, museum,
         movie_theater, library, hospital, art_gallery, aquarium, amusement_park)

    def __str__(self):
        return str(self.word)

    def getSound(self, index):
        return self.sounds[index]

# define japanese sound class
class JapaneseSounds:
    def __init__(self):
        self.sounds = (ice_cream, juice, kangaroo, octopus, queen, raccoon, shoes, socks, violin, fox,
         yogurt, zebra, go, come, run, sleep, stand, wake_up, walk, feet,
         nose, hand, eyes, ear, tiger, snake, monkey, lion, fish, elephant,
         dog, cat, bird, one, two, three, four, five, six, seven,
         eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen,
         eighteen, nineteen, twenty, turn_right, turn_left, stop, straight)

    def __str__(self):
        return str(self.word)

    def getSound(self, index):
        return self.sounds[index]

# define card class
class Card:
    def __init__(self, word):
        if (word in WORDS):
            self.word = word
        else:
            self.word = None
            print "Invalid card: ", word

    def __str__(self):
        return str(self.word)

    def get_word(self):
        return self.word

    def draw(self, canvas, pos):
        image_row = 0
        card_loc = [0,0]

        while image_row < CARDS_PER_ROW_IMAGE:
            if WORDS.index(self.word) < CARDS_PER_ROW_IMAGE * (image_row + 1):
                card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * (WORDS.index(self.word) % CARDS_PER_ROW_IMAGE),
                            CARD_CENTER[1] + CARD_SIZE[1] * (image_row % 12))
                break
            else:
                image_row += 1

        picture_chart = PICTURES[(WORDS.index(self.word)/(CARDS_PER_ROW_IMAGE * ROWS_IN_IMAGE))]
        canvas.draw_image(picture_chart, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class DealtDeck:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        deckToTest = ""
        for card in self.cards:
            deckToTest += "" + str(card)

        return "Deck to test contains " + deckToTest

    def __len__(self):
        count = 0

        for card in self.cards:
            count += 1

        return count

    def add_card(self, card):
        # add the card to the dealt deck
        self.cards.append(card)

    def remove_card(self, card):
        # remove a card from the dealt deck
        self.cards.remove(card)

    def pick_word(self):
        # picks a card from the
        return self.cards[random.randrange(0, len(self.cards))]

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        Card.draw(self, canvas, pos)


# define deck class
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []

        for word in WORDS:
            self.deck.append(Card(word))

    def shuffle(self):
        # shuffle the deck
        # use random.shuffle()
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        dealt_card = self.deck[-1]
        self.deck.pop()
        return dealt_card


    def __str__(self):
        # return a string representing the deck
        deck = ""
        for card in self.deck:
            deck += "" + str(card)

        return "Deck contains " + deck

    def __len__(self):
        count = 0

        for card in self.deck:
            count += 1

        return count

#define key word card class
class KeyWordCard:
    def __init__(self, card):
        self.card = []
        self.card.append(card)

    def __str__(self):
        key_word_card = ""
        for card in self.card:
            key_word_card += "" + str(card)

        return "Key word card is " + key_word_card

    def getCard(self):
        for card in self.card:
            return card

# define sound player
def playSound():
    for word in WORDS:
        if str(key_word_card.getCard()) == word:
            sound = sounds.getSound(WORDS.index(word))
            sound.rewind()
            sound.play()

# define event handlers for mouse
def mouse_handler(pos):
    global correct_cards
    global turns_taken
    global key_word_card
    global score
    global level
    global score_variance
    global past_score
    global TOP_GAP
    global turn_done
    global challenge_mode

    selected_cards = []

    if (pos[0] in range(0, CARD_SIZE[0] * 2)) and (pos[1] in range((5 * CARD_SIZE[1] + TOP_GAP), (6 * CARD_SIZE[1] + TOP_GAP))):
        if challenge_mode == "Listening":
            playSound()

    elif (pos[0] in range(CARD_SIZE[0] * 8, WIDTH)) and (pos[1] in range((5 * CARD_SIZE[1] + TOP_GAP), (6 * CARD_SIZE[1] + TOP_GAP))):
        turns_taken = 2
        turn_done = True
        playSound()
        timer.start()

    # Check selected card against laid cards
    for index, card in enumerate(new_deck_to_test.cards):
        vertical_index = index / CARDS_IN_ROW
        if vertical_index <= 4:
            if pos[0] in range(((index % CARDS_IN_ROW) * CARD_SIZE[0]), ((index % CARDS_IN_ROW + 1) * CARD_SIZE[0])):
                if pos[1] in range((vertical_index * CARD_SIZE[1] + TOP_GAP), ((vertical_index + 1) * CARD_SIZE[1] + TOP_GAP)):
                    selected_cards.append(card)

    if turns_taken > 0:
        if len(selected_cards) == 1:
            if key_word_card.getCard() == selected_cards[0]:
                correct_cards.append(key_word_card.getCard())
                score = len(correct_cards)

                turns_taken = 2
                level_up()


            else:
                sound_of_failure.rewind()
                sound_of_failure.play()

                turns_taken -= 1

                if turns_taken <=0:
                    turn_done = True
                    playSound()
                    timer.start()


# Update level
def level_up():
    global score
    global past_score
    global score_variance
    global level

    if score == past_score + score_variance:
        sound_of_success.rewind()
        sound_of_success.play()
        timer.start()
        past_score = score
        score_variance += 2
        level += 1

    else:
        deal()

# creates, shuffles and deals a deck of test words
def deal():
    global score
    global new_deck
    global new_deck_to_test
    global key_word_card
    global correct_cards
    global sounds
    global turn_done
    global turns_taken
    global challenge_mode
    global player_message

    player_message = ""
    turn_done = False
    turns_taken = 2

    # Create and shuffle new deck
    new_deck = Deck()
    Deck.shuffle(new_deck)

    # Create and deal new test deck
    new_deck_to_test = DealtDeck()
    choice_deck = DealtDeck()
    cards_to_deal = 50

    while cards_to_deal > 0:
        new_deck_to_test.add_card(Deck.deal_card(new_deck))

        cards_to_deal -= 1

    # Select key word
    for card in new_deck_to_test.cards:
        choice_deck.add_card(card)

    for correct_card in correct_cards:
        for card in new_deck_to_test.cards:
            if str(card) == str(correct_card):
                choice_deck.remove_card(card)
                if len(choice_deck) <= 0:
                    deal()

    key_word_card = KeyWordCard(choice_deck.pick_word())

    # set soundset
    if language == "Japanese":
        sounds = JapaneseSounds()

    else:
        sounds = EnglishSounds()

    if challenge_mode == "Listening":
        # Play key word sound
        playSound()

def game_reset():
    global correct_cards
    global score
    global level
    global past_score
    global score_variance
    global player_message

    correct_cards = []
    score = len(correct_cards)
    level = 0
    past_score = 2
    score_variance = 2
    player_message = "Please wait a moment."

# Listening button handler
def listening_button_handler():
    global challenge_mode

    challenge_mode = "Listening"
    game_reset()
    timer.start()


# Reading button handler
def reading_button_handler():
    global challenge_mode

    challenge_mode = "Reading"
    game_reset()
    timer.start()

# English button handler
def english_button_handler():
    global language

    language = "English"
    game_reset()
    timer.start()

# Japanese button handler
def japanese_button_handler():
    global language

    language = "Japanese"
    game_reset()
    timer.start()

# timer handler
def timer_handler():
    timer.stop()
    deal()

# draw handler
def draw(canvas):
    global new_deck_to_test
    global score
    global CARDS_IN_ROW
    global turns_taken
    global TOP_GAP
    global turn_done

    # draws cards on the table
    board_row = 0

    while board_row < (ROWS_ON_BOARD - 1):
        for index, card in enumerate(new_deck_to_test.cards):
            DealtDeck.draw(card, canvas, [(index % CARDS_IN_ROW * CARD_SIZE[0]), ((board_row) * CARD_SIZE[1]) + TOP_GAP])
            if index >= (CARDS_IN_ROW * (board_row + 1) - 1):
                board_row += 1

    # draws square around key word card
    if turn_done:
        for card in new_deck_to_test.cards:
            if card == key_word_card.getCard():
                index = new_deck_to_test.cards.index(card)
                vertical_index = index / CARDS_IN_ROW
                canvas.draw_polygon([(((index % CARDS_IN_ROW) * CARD_SIZE[0]), (vertical_index * CARD_SIZE[1] + TOP_GAP)),
                                    (((index % CARDS_IN_ROW) * CARD_SIZE[0]), ((vertical_index + 1) * CARD_SIZE[1] + TOP_GAP)),
                                    (((index % CARDS_IN_ROW + 1) * CARD_SIZE[0]), ((vertical_index + 1) * CARD_SIZE[1] + TOP_GAP)),
                                    (((index % CARDS_IN_ROW + 1) * CARD_SIZE[0]), (vertical_index * CARD_SIZE[1] + TOP_GAP))], 3, "Black")

    # draws the replay button, which replay's the sound
    canvas.draw_polygon([(0, (CARD_SIZE[1] * 5) + TOP_GAP),
                         (CARD_SIZE[0] * 2, (CARD_SIZE[1] * 5) + TOP_GAP),
                         (CARD_SIZE[0] * 2, (CARD_SIZE[1] * 6) + TOP_GAP),
                         (0, (CARD_SIZE[1] * 6) + TOP_GAP)], 3, "White")
    canvas.draw_text("Replay", (CARD_SIZE[0] / 5, (5.65 * CARD_SIZE[1]) + TOP_GAP), 40, "White", "sans-serif")

    # draws the pass button which forfeits the current turn
    canvas.draw_polygon([(CARD_SIZE[0] * 8, (CARD_SIZE[1] * 5) + TOP_GAP),
                         (WIDTH, (CARD_SIZE[1] * 5) + TOP_GAP),
                         (WIDTH, (CARD_SIZE[1] * 6) + TOP_GAP),
                         (CARD_SIZE[0] * 8, (CARD_SIZE[1] * 6) + TOP_GAP)], 3, "White")
    canvas.draw_text("Pass", (CARD_SIZE[0] * 8.45, (5.65 * CARD_SIZE[1]) + TOP_GAP), 40, "White", "sans-serif")

    # draws key word and player's score, turns left and level
    canvas.draw_text("Score: " + str(score), [CARD_SIZE[0] * 0.2, 40], 40, "White", "sans-serif")
    canvas.draw_text("Turns: " + str(turns_taken), [CARD_SIZE[0] * 8, 40], 40, "White", "sans-serif")
    canvas.draw_text("Level: " + str(level), [CARD_SIZE[0] * 4, 40], 40, "White", "sans-serif")

    keyword_width = frame.get_canvas_textwidth(str(key_word_card.getCard()), 40, "sans-serif")
    canvas.draw_text(str(key_word_card.getCard()), ((CANVAS_SIZE[0]/2) - (keyword_width/2), (5.65 * CARD_SIZE[1]) + TOP_GAP), 40, "Yellow", "sans-serif")

    if len(player_message) > 0:
        pm_width = frame.get_canvas_textwidth(player_message, 40, "sans-serif")
        canvas.draw_text(player_message, [(CANVAS_SIZE[0]/2) - (pm_width/2), CANVAS_SIZE[1]/2], 40, "Black", "sans-serif")

# initialization frame
frame = simplegui.create_frame("English Challenge", CANVAS_SIZE[0], CANVAS_SIZE[1])
frame.set_canvas_background("Black")
timer = simplegui.create_timer(3000, timer_handler)

#create mouse click and canvas callback
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)
frame.add_label('Challenge')
frame.add_button('Listening', listening_button_handler, 100)
frame.add_button('Reading', reading_button_handler, 100)
frame.add_label('Language')
frame.add_button('English', english_button_handler, 100)
frame.add_button('Japanese', japanese_button_handler, 100)


# get things rolling
deal()
frame.start()
