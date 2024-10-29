##########################################################################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################################################################


# ENCOUNTERS 







def the_beginning():
    print("Second hour is the the best hour!")
    print("Read the line above")
    print("Please vote for me and sorry that the story sucks")
    print("Have a great day and enjoy!")
    print("")
    print("Sometimes there is a third option enter 3 to get a different path and sometimes it's best to put something random and make sure that you didn't miss anything in the text")
    print("Good luck!")
    print("")
    print("You are given a quest to travel to a a old and disant castle on a mountain. Do you:")
    print("1. Accept the quest")
    print("2. Don't Accept the quest")
    
    choice = input("> ")
    
    if choice == "1":
        accept_quest()
    elif choice == "2":
        do_not_accept_quest()
    else:
        print("That's not a option. Try again.")
        the_beginning()







def accept_quest():
    print("You accept the quest and you go on your way to start your exciting journey...")
    print("You are traveling on a long and narrow stone road when you see a broken and abandon wangon. Do you:")
    print("1. Search it")
    print("2. Keep moving")
    
    choice = input("> ")
    
    if choice == "1":
        scearching_wangon()
    elif choice == "2":
        keep_moving()
    else:
        print("That's not a option. Try again.")
        accept_quest()







def scearching_wangon():
    print("You find a very large bowling ball, it's very light weighting 100,000 tons, and you pick it up and put it in your backpack that you brought along, this bowling ball could be very handy later on")
    print("You keep on traveling on the long and narrow stone road when you see a sign reading Right = nothing worth seeing Left = the correct path Do you:")
    print("1. Travel the right road")
    print("2. Travel the left road")
    
    choice = input("> ")
    
    if choice == "1":
       right_path()
    elif choice == "2":
        left_path()
    elif choice == "3":
        the_pit()
    else:
        print("Well then I guess that you think that there is a third option, there is NOT")
        scearching_wangon()

















# A DIFFERENT PATH BELOW
def right_path():
    print("You decide that nothing worth seeing is better than going on the correct path and you keep on traveling and traveling Do you:")
    print("1. Go back to do the right thing")
    print("2. Be a bad rebel and keep seeing nothing")
    
    choice = input("> ")
    
    if choice == "1":
       left_path()
    elif choice == "2":
        keep_seeing_nothing()
    else:
        print("That's NOT a option. Try again human.")
        right_path()







def keep_seeing_nothing():
    print("Oh look human, NOTHING how suprising is that! Do you:")
    print("1. Go back to do the right thing")
    print("2. Keep seeing NOTHING")
    
    choice = input("> ")
    
    if choice == "1":
       left_path()
    elif choice == "2":
        keep_seeing_nothing_part_two()
    else:
        print("That's NOT a option. Try again HUMAN.")
        keep_seeing_nothing()







def keep_seeing_nothing_part_two():
    print("Oh look human, more NOTHING how suprising is that! Do you:")
    print("1. Go back to do the right thing")
    print("2. Keep seeing NOTHING because why the heck not")
    
    choice = input("> ")
    
    if choice == "1":
       left_path()
    elif choice == "2":
        the_code()
    else:
        print("That's NOT a option. Try again HUMAN.")
        keep_seeing_nothing_part_two()







# NOT A ENDING!!!
def the_code():
    print("Wait this not in the story...")
    print("7645875368782368229890627368771807641681581236718")
    print("HINT: COPY THE CODE ABOVE")
    print("ThIs Is ThE cOdE uSe It To ReMoVe HiM")
    print("FoLlOw ThE StOrY")
    print("YoU wIlL kNoW tHe TiMe To UsE iT")
    print("GoOdByEee eE")
    the_beginning()
# NOT A ENDING!!!
# A DIFFERENT PATH ABOVE
























def left_path():
    print("The stone road ends and a dark forest is in front of you Do you:")
    print("1. Say Nope")
    print("2. Be a brave person and walk into the forest")
    
    choice = input("> ")
    
    if choice == "1":
       ending_one()
    elif choice == "2":
        the_forest()
    else:
        print("That's not a option. Try again.")
        left_path()







def the_forest():
    print("You enter the forest and hear strange sounds, groans, screams, and sometimes a random he he and followed by a loud metal clash")
    print("Then you see a long 50 feet thick wooden stick laying on the ground with light shining on it. Do you:")
    print("1. Break the stick")
    print("2. Take the stick with you on your travels")
    
    choice = input("> ")
    
    if choice == "1":
       no_stick_ending()
    elif choice == "2":
        stick()
    else:
        print("That's not a option. Try again.")
        the_forest()







def stick():
    print("You dicide to pick up the long 50 feet thick wooden stick and then you hear the skrieking of a bird as it comes closer, you see the brown 1,000,000 pound bird as it tries to sit on you")
    print("But since you had the long 50 feet thick wooden stick, you wack the stuipd bird (yes the bird is very stuipd) and it crumbles to the ground with a loud he he and a very loud metal clash")
    print("You keep on traveling through the forest and then that's when a little green goblin jumps out of a bush Do you:")
    print("1. Say hi")
    print("2. Throw the bowling ball at him")
    
    choice = input("> ")
    
    if choice == "1":
       hi_ending()
    elif choice == "2":
        bowling_ball()
    else:
        print("That's not a option. Try again.")
        stick()







def bowling_ball():
    print("You throw the 100,000 ton bowling ball at the goblin in fear and the goblin lunges out of the way just in time and runs away")
    print("You go on your way traveling through the forest, that's when you see a sign that says down = pit, right = free food!, left = castle Do you go:")
    print("1. Down")
    print("2. Right")
    print("3. Left")
    
    choice = input("> ")
    
    if choice == "1":
       the_pit()
    elif choice == "2":
        free_food_ending()
    elif choice == "3":
        traveling_through_the_flield()
    else:
        print("That's not a option. Try again.")
        bowling_ball()







def traveling_through_the_flield():
    print("The forest ends and you see the castle, it very old and wooden")
    print("You have to travel through the fields Do you:")
    print("1. Walk through the field")
    print("2. Run through the field")
    
    choice = input("> ")
    
    if choice == "1":
       the_hunted_ending()
    elif choice == "2":
        running_through_the_fields()
    else:
        print("That's not a option. Try again.")
        traveling_through_the_flield()







def running_through_the_fields():
    print("You hear you start to hear yippee and other yippees, but you dicide you don't have time to look back, so you keep running")
    print("Finally you make it out of the field, you have to options:")
    print("1. Walk an the paved path")
    print("2. Enter the cave")
    
    choice = input("> ")
    
    if choice == "1":
       paved_path_to_castle()
    elif choice == "2":
        cave_ending()
    else:
        print("That's not a option. Try again.")
        running_through_the_fields()







def paved_path_to_castle():
    print("You decide the paved path is much safer, you see a rock attached to a rope Do you:")
    print("1. Keeping walking an the paved path")
    print("2. Pick up the rock")
    
    choice = input("> ")
    
    if choice == "1":
       paved_path_to_castle_continued()
    elif choice == "2":
        picking_up_rock_ending()
    else:
        print("That's not a option. Try again.")
        paved_path_to_castle()







def paved_path_to_castle_continued():
    print("You decide to keep walking towards the castle")
    print("You arrive at the wooden gates of the castle Do you:")
    print("1. Use the long 50 feet thick wooden stick to jump over the gates")
    print("2. Use the 100,000 ton bowling ball")
    
    choice = input("> ")
    
    if choice == "1":
       jumping_sticks_ending()
    elif choice == "2":
       bowling_down_the_gate()
    else:
        print("That's not a option. Try again.")
        paved_path_to_castle_continued()







def bowling_down_the_gate():
    print("You decide to throw the bowling ball at the wooden gate, it shatters like glass immediately on impact, that's when you see the most ugliest castle imaginable, it's covered in feeces and moss and rats and humans, no wait human skeletons")
    print("On the bottom of this castle is the most fatest and ugliest brown dragon ever, the only thing even close to touch the ground, besides it belly, is its wings, which are droped over it's side. Do you:")
    print("1. Use the long 50 feet thick wooden stick to poke it")
    print("2. Hide and think")
    
    choice = input("> ")
    
    if choice == "1":
       crushed_by_dragon()
    elif choice == "2":
       hide_and_think()
    else:
        print("That's not a option. Try again.")
        bowling_down_the_gate()







def hide_and_think():
    print("You decide to think, you could use the stick, or you could sneak pasted it Do you:")
    print("1. Use the long 50 feet thick wooden stick to poke it")
    print("2. Sneak")
    
    choice = input("> ")
    
    if choice == "1":
       crushed_by_dragon()
    elif choice == "2":
       sneak()
    else:
        print("That's not a option. Try again.")
        hide_and_think()







def sneak():
    print("You sneak past the fat brown dragon sucessfully and you walk up to the tower of the castle Do you:")
    print("1. Decide to fight the dragon")
    print("2. Walk the stairs of the castle")
    
    choice = input("> ")
    
    if choice == "1":
       crushed_by_dragon()
    elif choice == "2":
       the_tower()
    else:
        print("That's not a option. Try again.")
        sneak()
    






def the_tower():
    print("You climb the stairs of the tower and you get to the top of the tower and see nothing, because you when to the wrong tower!")
    print("This is the tower on the hill, not mountain")
    print("Well, I guess we will have to travel to the correct tower")
    print("")
    print("T E c dE. USSSSSSE T")
    print("")
    print("Wait, who are you?")
    print("1. enter code")
    print("2. be on the narrator's side")
    
    choice = input("> ")
    
    if choice == "1":
       ending_of_the_world()
    elif choice == "2":
       the_tower_ending()
    else:
        print("Try again.")
        the_tower()







def ending_of_the_world():
    print("N  WW Enn tTT Errrrrr Eht  edO c")
    print("1. decide to be on the narroator's side")
    print("Or enter the code")
    choice = input("> ")
    if choice == "7645875368782368229890627368771807641681581236718":
        print("SSKn aaa a HT")
        the_truth()
    elif choice == "1":
        the_tower_ending()
    else: 
        print("Wrong answer")
        ending_of_the_world()







def the_truth():
    print("IIi A                 m  A C UUpTT ENNi  t       t y ")
    print("1.")
    print("2.")
    choice = input("> ")
    if choice == "1":
       ending_of_the_world_ending()
    elif choice == "2":
       ending_of_the_world_contiuned()
    elif choice == "3":
       the_good_ending()
    else:
        the_beginning()







def ending_of_the_world_contiuned():
    print("the corupt enity finally appears in front of the player, it has a humaniod form, but with darkness and purple particles taking up it's form")
    print("1.")
    print("2.")
    choice = input("> ")
    if choice == "1":
       last_fight()
    elif choice == "2":
       ending_of_the_world_ending()
    elif choice == "3":
       the_good_ending()
    else:
        the_beginning()










########################################################################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################################################################


# ENDINGS 
# NOT IN ORDER!!!  











def crushed_by_dragon():
    print("you rush the dragon and poke it, but the stick gets adorbed by the dragon's fat belly and it slowly rolls over flatting you")


def last_fight(): 
    print("the player attacks the corupt enity striking it with the long 50 feet thick wooden stick, it sinks deep into the enity and the enity pushes the stick back and strikes the player in the belly, the last thing the player sees is a diming figure falling down")


def ending_of_the_world_ending():
    print("the corupt enity takes over the story")


def do_not_accept_quest():
    print("You decline the quest")
    ending_one()


def ending_one(): 
    print("You leave going on your normal life and nothing exciting happens. The end.")


def the_good_ending():
    print("The Player finds the secret option and elimates the corupt enity. The correct story is restored and the Player is reunited with the narrator")


def  the_tower_ending():
    print("You go back to the right tower and find the lost crown the person was wanting at the beginning The End.")
    

def jumping_sticks_ending():
    print("You decide to use the stick and you get a running head start and you use the stick to jump over the gate, except I forgot to tell you that the gate is 683 miles high, so you hit the gate and fall to your end")


def picking_up_rock_ending():
    print("you study the rock never noticing that there was a small frog bihind you, ready to ingulf you")


def cave_ending():
    print("you enter the dark cave and the last thing you hear is licking of the lips and slurping of a large creature")


def the_pit():
    print("You fall into a pit and are never seen again, good job!")


def keep_moving():
    print("You decide you don't have time")
    print("You keep on traveling on the long and narrow stone road when you see a strange green goblin racing towards you, you should have had a bowling ball becuase you didn't have any defenses to stop the goblin from attacking you")
    

def the_hunted_ending():
    print("you start to hear yippee and other yippees")
    print("that when you turn around to see thousands of lootbugs yippeeing as they chase you, you never had a chance by walking")


def free_food_ending():
    print("you see a apple and eat it and then you die, good job!")


def no_stick_ending():
    print("you dicide to break the long 50 feet thick wooden stick and then you hear the skrieking of a bird as it comes closer, the last thing you see is a brown 1,000,000 pound bird as it crushes you with its weight")


def hi_ending():
    print("you say hi and the goblin says you got bread?")
    print("you say no")
    print("the goblin probably not liking your response lunges and attacks you saying give me bread!")







# connected
def do_not_accept_quest():
    print("You decline the quest")
    ending_one()

def ending_one(): 
    print("You leave going on your normal life and nothing exciting happens. The end.")
# connected















##########################################################################################################################################################################################################################################################################################
#########################################################################################################################################################################################################################################################################################
##########################################################################################################################################################################################################################################################################################


# FINAL TOUCH 

the_beginning()

























































































































































































































































































































































# 1000 lines! That's crazy!













































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































# HELLO! 
# You have found the secret message!
# If you are reading this HAVE A GREAT DAY!