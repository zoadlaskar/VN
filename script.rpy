# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.




















































define s = Character("Mr.Mori")
define d = Character("zeil")
define e = Character("[e_name]")
define j = Character("Sara") #the extra
define v = Character("David")
define r = Character("Eva")
if e =="":
    default e_name = "Percy"



# The game starts here.

label start:
    play audio bach volume 0.20


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene cafe a day

    # This shows a character sprite. A placeholder is used, but you can

    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
   
   
    show zeil smile
    with fade
    d "What is your name?"
    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    # both of them are robots or half robot who are trying to be human or understanding what it means to be
    # These display lines of dialogue.
    
    e "My name is [e]."
    d "Nice to meet you [e],my name is Zeil!"
    d "I know it's your first day, so I have to tell you first your living quarters are in room 324 ?"  
    e "Wait, who are you!?"
    d "Oh right, sorry forgot to introduce myself!" 
    d "The principal assigned me to show new students around"   
    d "Anyways let's go to your dorm to discuss the other rules"
    
    # This ends the game.e
    scene bg dorm night
    show zeil delighted
    d "Alright so this is your room not bad I would say"
    d "First you cannot go past the perimeters of this school unless given permission to do so"
    d "Second you cannot skip graduation day" 
    e "Why is that?"
    d "Well after you graduate they sort of do some operation on you to decide if you stay here or get 'transferred'"
    e "What does that mean?"
    d "I'm not totally sure but you won't be here anymore that's all I know."
    show zeil smile2
    d "Alright, that's all for today I'll see ya later!"

    show text "7 hours later"
    # fake human memories due to being AI 
    scene bg lights off 
    e "Today was boring wonder why parents sent me here of all places"
    e " I wonder what she meant by transferred"
    e "What other place is there besides here?"
    e "It feels like I've heard this before though."
    
    
    scene bg dorm night
    e "Where should I go tommorow? "
    menu: 
     
        
        "I'll go to the cafe":
            
            jump cafe1
        "I'll go to the classroom":
            
            jump classroom1
label cafe1:
    scene cafe a evening
    e "Oh hey what are you doing here?"
    show zeil smile with fade
    d "Nothing just wanted a coffee"
    d "Let me order for you"

    d "I'd like some coffee with my creamer, make that two please!"
    e "Thanks, so tommorrow is our first day of class "
    d "Yeah and we have philosophy101 together"
    e "Is the teacher good?"
    d "Well the teacher is, so it' a bit differents, but I heard his class is great!"
    e "Oh? that will be interesting what kind of philosophy?"
    d "Oh I don't know but I hear he talks about the soul a lot!"
    e "Sounds horrible"
    show zeil sad with fade
    d "Yeah maybe, but I think it's interesting"
    d "I wonder what a soul is."
    show zeil smile with fade
    d "I'm sorry! I didn't mean for it to sound so gloomy!"
    e "It's okay I wonder sometimes too"
    e "Do you wonder what's outside this school?"
    d "Yeah I do but it's not like we can leave anyways they'll punish us."
    e "What do you mean by that?"
    d "I'm not sure but the last person that tried to leave..."
    e "What?"
    d "I never saw them again."
    e "..."
    d "They probably got transferred, so it's okay I guess"
    d "Anyways, I'll see you later it's get really late."
    hide zeil smile with fade
    scene cafe a night
    e "Someone dissappeared for going outside?"
    e "This doesn't really make any sense?"
    e "Why are we even staying here then?"
    #play ominous sound add in later
    e "What's that note over there?"
    

    "This place is not safe - [e]"
    
    # he is 016 but his memories got wiped
    e " That's not possible I couldn't have wrote this..."
    e "I better get going..."
    #leads to route where he figures out he isn't human a bit too soon
    jump route1p1


    
   
 #alternate route   
label classroom1:
    scene classroom a night
    show zeil normal at right 
    hide zeil normal at right
    d "Hey what's up "
    e "Nothing just walking around"
    show zeil smile at right
    d "Yeah something about walking around here is nostalgic"
    e "Yeah I get that feeling too."
    e "I don't remember stuff from my past often."
    e "It's refreshing to remember sometimes."
    d "It's funny when I have this memory."
    hide zeil smile at right 
    show zeil normal at right
    d "When I was young I used to really want to get into this light blue liquid in my backyard."
    d "In that liquid there was this little rubber duck and I always wanted to sort of float in that liquid."
    d "Like that duck."
    d "My mom forbid from going into in the liquid."
    d "But, one day I did or at least I think I did"
    d "..."
    e "What happened after?"
    d "All I remember is jumping in. There was no after."
    
    hide zeil normal at right
    show os_angry at right 
    show zeil shocked at left
    s "What are you two doing out so late!"
    hide os_angry
    show zeil sad at left
    d "I'm sorry sir, we were just looking around"

    show os_laugh at right
    s "I'm just kidding it's nice to see you people so eager!"
    hide os_laugh at right
    show os_neutral
    s "However, do not make a habit of this. "
    s "How should I put it?"
    s "Do that again and you'll both face punishment!"
    s "That being said you guys have a good night!"
    
    hide os_neutral
    e "Is it just me or is there something off about him?"
    e "There isn't even any class today."
    show zeil smug with fade
    d "Don't you think you're overthinking this?"
    e "No of course not Zeil!"
    show zeil delighted with fade
    d "Relax, I'm just messing with you."
    e "I don't know something just ... feels wrong."
    d "I've lived here my entire life everything's fine."
    d "As long as we follow the rules we have nothing to worry about."
    e "..."
    " Something doesn't feel right but maybe i'm just overthinking" 
    e "Yeah you're probably right."
    d "Alright i'm tired I'll see you in class."
    e "Goodbye!"
     
    jump altroute1

label altroute1:
    scene bg dorm night   
    e "It's strange because it feels like I recognize what that liquid maybe."
    e "I wonder why we haven't seen it or heard about it at class."
    show text "3 hours later"
    show zeil smile2 
    with hpunch
    hide zeil smile2
    with vpunch
    d "Hey you want to take a walk?!"
    e "What are you doing here!It's 2 am!"
    show zeil sad
    d "Sorry! I just wanted to say I have an idea?"  
    hide zeil sad 
    show zeil smile 
    e "Well what is it."
    d "I think we should go look at the restricted section in the library!"
    e "Why that sounds insane."
    hide zeil smile 
    show zeil smug 
    d "What are you scared!"
    e "No! I just don't know."
    hide zeil smug

    show text "Library " with fade
    show zeil normal 
    e "What are those two doing here anyways?"
    d "I have no idea."
    d "She's just a student I had no idea she knew the professor this well."
    e "Let's hide and listen."
    hide zeil normal 
    show zeil bored
    d "That's so boring!"
    e "I want to hear this."
    d "Alright."
    hide zeil bored
    scene student council room a night
    show os_sigh at right 
    
    show extra normal at left
    with zoomout
    s "Those animals will eventually start wondering what's outside this school."
    j "What would make you think so."
    s "It's simply inevitable and besides the fool left a note for himself."
    s "The note tells them to run  away."
    j "So, what do we do?"
    s "We do not let them."
    s "If they were to be able to leave under our supervision."
    s "We would be killed."
    j "Why do you care?"
    s "Because I have my own plan which I must complete before I myself die."
    #his plan is to destroy the world system and make a new one that is just
    s "So for that reason we must not let them leave."
    s "This story has been told for decades."
    s "We've stopped those disgusting robots before."
    
    s "Now there's only a year or so until my plan will be enacted."
    s "So we cannot fail now."
    s "I promise I'll take back what they took from us."
    j "I'm not aware of what you are referring to."
    s "Don't worry about it. You will be mine again when you remember."
    j "..."
    j "What happens if they don't leave this time?"
    s "Nothing they'll be killed on graduation and get harvested."
    show extra normal at left with fade 
    show os_sigh at right
    with move
    hide os_sigh at right 
    hide extra normal at left
    show zeil sad 
    d "..."
    d "You knew something and didn't say anything?"
    hide zeil sad 
    show zeil sad
    e "I have no idea what he's talking about!"
    e " I never wrote that note! I promise."
    d "How can I trust you!"
    e "I got here a few days ago zeil, I had no idea."
    e "I promise."
    hide zeil shocked
    show zeil sad 
    d "..."
    e "..."
    e "How can we be robots?"
    e "I'm a human I can feel it! and see it!"
    d "Look around you the prfoessor, himself isn't human no one here is!"
    e "..."
    d "These memories I get randomly they've always felt out of place."
    d "They felt almost like a dream sometimes."
    d "I knew that but i didn't care."
    d "But now I know that they may have never existed."
    e "You don't know that."
    d "This is what I do know."
    d "There is no after for us."
    d "On graduation day they'll kill us but what's the use we aren't alive."
    e "Didn't you hear them we can try to leave!"
    e "There could be an entire world out there that we have never seen."
    d "It doesn't matter don't you get it."
    d "It doesn't matter where we go no where in this world was meant or us."
    d "I may have no heard much but I do understand that by the seems of it..."
    d "We are just food for them."
    d "I'm going home."
    e "I'll meet you at the dorm after."
    hide zeil sad
    e "I have to get out this school soon."
    e "Alright I need to somehow break into that room."
    e "Okay so there's a dog."
    menu:   
        "Run past it.":
            jump dumbdeath1
        "Sneak around it.":
            jump altroute2
$ dumb_end = False
label dumbdeath1:
#I just wanted to try this it is not serious lol
    show os_angry
    s "Who's there!"
    e "..."
    s "Oh it's you."
    s "I'm sorry but I cannot have you ruining my plans this soon."
    hide os_angry
    show os_laugh
    s "I'm sorry but this is your friend."
    show text "He stabs you."

    scene pblack with Pause(1.5)
    show text "Game Over"
    return
    jump dumbend

label altroute2:
    scene student council room a night
    e "Oh thank god that was terrifying dog."
    show text "World Geography"
    e "I'm gonna take this to my room."
    scene bg dorm night
    e "I don't think i'll bother zeil today."
    show text "World Geography"
    e "There are pages ripped out of this."
    e "The 'Ocean'" 
    
    #I guess his reason to try to escape in terms of hope and somethign to look forward to
    e "What I've seen this before"
    e "I have to get there no matter what."
    scene starry night
    "[e]! come here! Your mother has been waiting for you for the last few days."
    e "I'm coming mom!"
    scene bg dorm night
    e "These memories aren't real mother never existed..."
    e "..."
    #Unfinished route
   
    return
    
    
    
    
#main storyline
label route1p1:
    scene bg dorm night
    e "What does this note mean"
    e "I'll ask zeil"
    scene classroom a day
    show os_neutral at right
    s "Good morning class!"
    s "My name is Professor Mori."
    s "First let us set some rules"
    s "First I will not tolerate any disrespect from you people."
    s "Is that understood?"
    s "Second if I hear as so much as a hum you will spend you weekends here."
    s "Say Yes if you understand"
    "Yes Professor!"
    s "Good. moving on todays topic."
    
    s "Today, we will discuss the soul."
    s "To start, would anyone like to answer what a soul is?"
    hide os_neutral at right
    show extra normal with fade 
    j "It a spiritual part of one's self that may or may not exist"
    hide extra normal with fade
    show os_neutral at right
    s "Mediocre answer, but not exactly."
    s "A lot of people do have souls, others do not"
    s "Also a soul is not as it seems."
    s "It's not one as a whole but rather one at their core."
    s "Some of us know that but we never know who we are at our core."
    
    hide os_neutral at right
    show zeil delighted at left
    e "Hey Zeil, do you know what this means?"
    d "No, I'm not sure why you would write to yourself"
    e "No, I'm being serious zeil I didn't write this."
    d "Well, if you're so worried, you should ask the professor."
    d "He's pretty good with this stuff."
    e "Thanks Zeil, I'll do that."
    e "I can't believe I have to ask Professor douchebag."
    hide zeil delighted at left
    show os_neutral at right
    s "See you in a week class"
    e "Hey professor I was wondering if you would be able to help with a puzzle or code of some sort"
    s "If you must I'll be in the cafe until 11 tonight"
    scene cafe a night  
    show os_annoyed at right
    s " So, what did you want to bother me with?"
    e "Do you have any idea what this note means?"
    hide os_annoyed at right 
    show os_worry at right 
    hide os_worry at right  
    e "It has my name on it but I've only been here for two days."
    #He knows why but won't tell you because deep down he wants to know if he himself has a soul by seeing if the mc developes one
    s "hmm..."
    s "That is quite strange."
    
    show os_neutral at right
    s "Perhaps you did write it but do not remember"
    e "..."
    e "I don't see how that's possible"
    s " It maybe possible."
    e "..."
    hide os_neutral at right
    show os_neutral at right
    s "No need to be foolish someone probably just has the same name as you."
    s "Besides you are right how could that be?"
    hide os_neutral at right
    e "Thanks professor I feel sligtly more relieved"
    e " I guess i'll be going now"
    show os_neutral
    s "Alright."
    hide os_smile
    #leaders of the svhool 
    # He projects his self hatred onto students of his kind
    # He eventually finds himself wishing for them to get out after those two fall in love and show their souls after he breaks them down 
    # However, they do not give up and as his last attempt fails he finally heals
    "Is everything according to plan, Mori?"
    show os_smirk
    "Yes sir."
    hide os_smirk
    scene school hallway a nightlight
    e "Something feels familiar like I've been here a long time ago..."
    show zeil smile
    d "Hey! what are you doing here?"
    e "Nothing just walking around"
    d "I think I can help you!"
    d "I went to the library and I found something mentioning mysterious notes"
    e "What did you find?"
    d "Well, I can't understand it but it does say something about a place where land meets a water-like body"
    e "I don't know what that means."
    e "Maybe we should research more about that."
    d "Sure [e]!"
    d "We'll talk about that but are you ready for art class?"
    menu:
        "Yeah, let's go":
            jump route1j1a
        

#external conflict == society dehumanizing them mc
#internal conflict understanding what it means to be human or have a soul mc
#external == society vs man zeil
#internal  == she accepts her condition zeil
#internal == he is one of them but he hates himself prof
# exteral == he is a part of the system but originally did not want to be  prof
label route1j1a:
    scene classroom a night
    show os_neutral at right
    s "Good morning class!"
    s "Today I want you mutts to draw anything that comes to mind."
    " Jeez why does he keeping calling us that."
    hide os_neutral
    show zeil angry at left 
    e "Umm are you okay?"
    d "Yeah, I just don't know what to draw that's all."
    e "I drew a funny picture of you just now!"
    hide zeil angry at left 
    show zeil laugh at left
    d "Hey!! I'll get you back for that!"
    hide zeil laugh at left
    show os_angry at right 
    s "Enough!"
    s "You're lucky you're a new student."
    s "However, you come see me in my office after class!"
    e "She did nothing wrong!"
    
    s "Say that again and you'll dissappear like that kid two years ago"
    hide os_angry at right 
    show zeil sad at left 
    d "No,I'm sorry professor it's my fault."
    show os_angry at right
    s "Alright I'll see you in detention."
    hide os_angry at right 
    
    e "We didn't do anything wrong!"
    show zeil sad at left
    d "It doesn't matter that's the way it is."
    hide zeil sad at left 
    e "No it's my fault I should be the one going to detention."
    show zeil angry 
    d"No! just go away [e]!"
    hide zeil angry 
    show zeil smile 
    s "Don't worry i'll be fine go now."
    e "Alright, i'm sorry i'll leave now"
    hide zeil smile 
    show zeil sad 
    s "This feels wrong..."
    hide zeil smile 
    scene bg dorm night
    "*Thud Thud*" 
    
    e "Who's there?"
    d "hey [e] it's me."
    show zeil normal
    e "Zeil what are you doing?"
    d "I just wanted to stay over for the night."
    e "Yeah but why? did anything happen?" 
    d "No it's just that I just wanted to apologize for getting mad."
    hide zeil normal
    e "It's fine I deserved it."
    e "Anyways I'm going to sleep on the couch you can sleep wherever you want."
    show zeil smile
    d "Thanks [e]!, I'll take the bed if that's fine."
    e "Yeah, sure that's fine the couch is terrific."
    hide zeil smile 
    "Something definitely happened"
    "'[e] falls asleep.'"
    
    show zeil sad at right 
    with move
    "It's not fair what was I suppose to do?"
    hide zeil sad
    "Two hours pass"
    scene cafe a night
    show zeil sad 
    with hpunch 
    "What is your name?"
    scene bg dorm night
    "When was that?!"
    e "Hey do zeil do you want to go somewhere?"
    d "[e]! it's midnight."
    e "Suit yourself. I'm taking a walk."
    d "You know we could get in trouble right?"
    e "We won't it will be fun."
    d "No I won't not again..."
    e "Oh.. sorry. I'll be right back okay?"
    menu: 
        "Go to the clubroom":
            
            jump route2a
        
        "I change my mind I'll stay":
            jump route1j1a2
   
label route1j1a2:
    scene bg dorm night
    e "I'll stay."
    d "Why is that?"
    e "I don't know just wanted to talk."     
    e "I just want to know what happened?"
    d "Nothing really."
    e "He didn't do anything did he?"
    d "God no! He just said something."
    e "If you don't mind I want to ask what it is."
    d "..."
    d "I'm not sure if I want to say too much."
    e "That's fine."
    d "But I will say a bit."
    d "He told me that I'm empty and there's nothing in me." 
    e "That's not true at all. He's probably talking about himself."
    e "Are you sure that's all."
    d "Yes..."
     
    menu:
        "Go for a walk.":
            jump route2a      
    
    
    
label route2a:
    scene bg starry night
    show os_smirk at right
    s "So we start again."
    hide os_smirk at right
    show os_neutral at right 
   
    
    show extra normal at left
    with zoomout
    
    s "What's the trial number?"
    j "This attempt 15."
    hide os_neutral at right
    show os_sigh at right
    s "Those two are not humans no amount of attempts will ever change that." 
    s "I do not see why they continue with this experiment."
    hide extra normal at left
    hide os_sigh at right
    
    # Other route will be the same as the previous 15 
    # They
 
    
    scene club room a night
    e "This school could use some better vending machines everything here tastes the same."
    e "I wonder what outside this place looks like."
    e "I remember going to the beach as a kid but nothing more than that."
    e "Why do they only offer sprite and coke."
    e "There seems to a note attached to it."
    "Do not trust the Mr.Mori or Sara-[e]"
    e "Someone must be playing a prank on me."
    e "It seems as though it was written years prior."
    e "I'll need to investigate this."
    
    scene classroom a night 
    show os_neutral at right
    s "So today we you will partner with anyone or work by yourself."
    s "You will compose a song."
    hide os_neutral at right
    show zeil smile
    d "Let's work together!"
    e "Sure this might tought i've never written any music ever!"
    d "It's fine! I know a few."
    hide zeil smile
    
    e "Wow that was amazing!"
    show zeil smile2
    d "Thanks!"
    hide zeil smile2
    
    show os_sigh at right
    s "Alright class is dismissed! Please leave."
    hide os_sigh at right 
    e "I have to know what that note means."
    show zeil angry     
    d "What are you doing!"
    e "I got another note and I need to follow him to understand."
    d "You could get in big trouble if you get caught."
    d "At least let me see the note."
    hide zeil angry
    show zeil annoyed
    "You show her the note"
    d "This isn't very funny for you to write notes to yourself!"
    e "I'm not that's why I have to know."
    d "Alright let me go with you!"
    scene school hallway a night
    e "What are they saying?"
    show zeil normal
    d "I don't know let's get a bit closer."
    hide zeil normal
    show os_angry at right
    show extra normal at left 
    with zoomout
    
    s "I'm not sure what the administration is trying to prove with this experiment."
    s "For centuries we have known that people like us are not human."
    j "You are right we are fully robotic by model."
    s "That's right we are nothing more."
    s "They will get the same result anyways."
    j "..."
    j "This is the last trial, and most of these students will be reset by the end of the summer."
    s "I hope so."
    s "Did you hear that?"
    hide os_angry at right with dissolve
    hide extra normal at left 
    show zeil shocked
    e "Why did you sneeze!"
    d "I'm sorry"
    s "Who's there!!"
    d "We need to go!"
    hide zeil shocked
    scene bg dorm night
    show zeil sad 
    e "What was that about!"
    d "At the end of year we have graduation."
    d "That means we will be 'reset' during graduation."
    e "What does does reset mean?"
    d "I don't know we need to find out though."
    e "What does he mean by we are not human?"
    d "I'm not sure either."
    e "I don't believe it either ways!"
    d "I don't what I believe now."
    d "I think they know it was. "
    e "What makes you think that!?"

    d "Just a feeling if i'm being honest."
    e "We might be in a world of danger."
    scene pblack with fade
    show text "Act 2 \n Outside the School" with Pause(1.5)
    scene bg dorm night
    show zeil normal
    e "Hey, are you going to class today?"
    d "No, I think I'll pass."
    e "Are you sure?"
    d "Yeah I'll be fine."
    scene classroom a night
    show os_angry at right
    s "Today students we have two more of you."
    hide os_angry at right
    show eva normal2 at left 
    
    r "Hi, my name is Eva!"
    hide eva normal2 at left
    scene classroom a night
    show david laugh at left
    v "Hi, my name is David."

    #she gets depressed and won't help as she wants to hide from the truth
    #he does it himself
    #gets in serious danger
    #she breaks out of her sadness to help her friend or something like that
    #commence romance
    

    
    #he left himself some notes 
    #they eventually fall in love
    #the Professor challenges by sending them notes and dilemmas to find out if they have soul 
    # However, her acceptance of her condition vs his willingness to move forward lead to a falling out where the villain proffessor s
    # concludes their is no soul and so graduation day nears and on the brink of despair right before one of them is transferred they find their souls
 
 
 
 
 
 
 
 
 
    # the villain is in denial until he is defeated he accepts his loss and sets them free and himself






#ends the game
#label
return




























