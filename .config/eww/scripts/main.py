import os
import subprocess
import time
import threading

MOTIVATIONAL = [
    "The only place you find success before work is in the dictionary.",
    "If you don’t go after what you want, you’ll never have it. If you don’t ask, the answer is always no. If you don’t step forward, you’re always in the same place.",
    "Being strong means rejoicing in who you are, complete with imperfections.",
    "Take chances, make mistakes. That's how you grow. Pain nourishes your courage. You have to fail in order to practice being brave.",
    "Nothing lasts forever. Not even your troubles.",
    "There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle",
    "It's not the size of the dog in the fight, but the size of the fight in the dog.",
    "I quit being afraid when my first venture failed and the sky didn't fall down.",
    "It took me a long time not to judge myself through someone else's eyes",
    "Nobody can make you feel inferior without your consent.",
    "A life spent making mistakes is not only more honorable, but more useful than a life spent doing nothing.",
    "You're going to fail your way to success, you have nothing to be ashamed of so keep your head up. It’s much easier to come up with excuses of why you can't do it. If you do what is easy your life will be hard.",
    "You make the world a better place by making yourself a better person.",
    "You will never know what you are capable of until you take that first step and go for it.",
    "The only easy day was yesterday.",
    "Life is like a steering wheel, it only takes one small move to change your entire direction.",
    "A man who treats his woman like a princess is proof that he has been born and raised in the arms of a queen.",
    "The size of your problems is nothing compared with your ability to solve them. Dont overestimate your problems and underestimate yourself."
]

TECHNOLOGY = [
    "The great growling engine of change - technology.",
    "Technology... is a queer thing. It brings you great gifts with one hand, and it stabs you in the back with the other.",
    "If we continue to develop our technology without wisdom or prudence, our servant may prove to be our executioner.",
    "It's not a faith in technology. It's faith in people.",
    "Sharing is good, and with digital technology, sharing is easy.",
    "The technology of the time dictated the way things looked.",
    "You affect the world by what you browse.",
    "I'm in favor of any technology that makes my work available to the reading public at a reasonable price.",
    "Technology is a useful servant but a dangerous master.",
    "Technology is the fashion of the '90s. It affects everyone, and everyone is interested in it - either from fear of being left behind or because they have a real need to use technology.",
    "Technology is not neutral.",
    "Technology, like art, is a soaring exercise of the human imagination.",
    "We have more media than ever and more technology in our lives. It's supposed to help us communicate, but it has the opposite effect of isolating us.",
    "Our technological powers increase, but the side effects and potential hazards also escalate.",
    "The further you get into technology, the further you go into gaming. That's the general rule.",
    "Technology has become as ubiquitous as the air we breathe, so we are no longer conscious of its presence.",
    "Why are we, as a nation so obsessed with foreign things? Is it a legacy of our colonial years?",
    "Technology without hatred can be a blessing. Technology with hatred is always a disaster.",
    "Technology gives us the facilities that lessen the barriers of time and distance - the telegraph and cable, the telephone, radio, and the rest.",
    "You are not training young people for the world of tomorrow unless you are doing proven technology training.",
    "The real danger is not that computers will begin to think like men, but that men will begin to think like computers.",
    "Technology made large populations possible; large populations now make technology indispensable.",
    "The most technologically efficient machine that man has ever invented is the book.",
    "The art challenges the technology, and the technology inspires the art.",
    "Technology is best when it brings people together.",
    "The human spirit must prevail over technology.",
    "What new technology does is create new opportunities to do a job that customers want done.",
    "Technological progress has merely provided us with more efficient means for going backwards.",
    "The great myth of our times is that technology is communication.",
    "Technology should improve your life… not become your life.",
    "We are stuck with technology when what we really want is just stuff that works.",
    "Ethics change with technology.",
    "Technology is anything that wasn’t around when you were born.",
    "Once a new technology rolls over you, if you're not part of the steamroller, you're part of the road.",
    "We’re changing the world with technology.",
    "Technology is unlocking the innate compassion we have for our fellow human beings.",
    "Technology over technique produces emotionless design.",
    "Technology fuels our culture. But it's our responsibility to use it wisely.",
    "Technology is a word that describes something that doesn’t work yet.",
    "Any sufficiently advanced technology is indistinguishable from magic.",
    "Technology is teaching us to be human again.",
    "Technology is neither good nor bad; nor is it neutral.",
    "The best way to predict the future is to invent it.",
    "People think of technology as an end. It’s not. It’s a means to an end.",
    "Technology changes rapidly; human nature, not so much.",
    "Technology can be our best friend, and technology can also be the biggest party pooper of our lives.",
    "As technology advances, it’s harder to find time for meaningful disconnection.",
    "In the future, people won’t program computers. They’ll train them.",
    "Technology is the campfire around which we tell our stories.",
    "Every once in a while, a new technology, an old problem, and a big idea turn into an innovation.",
]


FUNNY = [
    "Full form of study - S-T-U-D-Y = [S]inging, [T]weeting, [U]nlimited Texting, [D]reaming, [Y]awning.",
    "If you are player then Im the GAME.",
    "I buy expensive suits. They just look cheap on me.",
    "I used to jog but the ice cubes kept falling out of my glass.",
    "Just saw the most smartest person when i was in front of the mirror",
    "I don't care what the haters and naysayers say. If they make jokes about me, I'll laugh because they'll probably be funny.",
    "My life needs editing.",
    "I want some one to give me a Loan and then leave me Alone.",
    "Tragedy is when I cut my finger. Comedy is when you fall into an open sewer and die.",
    "When WORDS fail, eyes speak.When eyes fail,?HEART? speaks. When HEART fails, nothing speaks they put cotton in the nose",
    "Some people call me Mike, You can call me tonight.",
    "Cant talk, telepathy only!",
    "From there to here, and here to there, funny things are everywhere.",
    "Chaos in the midst of chaos isn't funny, but chaos in the midst of order is.",
    "Get your facts first, then you can distort them as you please.",
    "My last seen at? was just to check your last seen at?.",
    "Knowledge is like underwear. It is useful to have it, but not necessary to show it off.",
    "Don't get me wrong, there are sometimes if I go and see a really funny comedy, that I wished I had smoked a joint. I'll be honest with you. That's the truth.",
    "My fake plants died because I did not pretend to water them.",
    "80% of boys have girlfriends.. Rest 20% are having brain.",
    "You have eyes my dear but you cannot see.", "God is really creative , i mean ..just look at me"
]

INSPIRATIONAL = [
    "Onward and Upward!  To Narnia and the North!",
    "The power of imagination makes us infinite.",
    "You weren't just a star to me, you were my whole damn sky.",
    "One original thought is worth a thousand mindless quotings.",
    "My task, which I am trying to achieve is, by the power of the written word, to make you hear, to make you feel--it is, before all, to make you see.",
    "He who controls the past controls the future. He who controls the present controls the past.",
    "Worry about your character, not your reputation. Your character is who you are, your reputation is who people think you are.",
    "Never give up. There is no such thing as an ending, just a new beginning.",
    "Where there is ruin, there is hope for a treasure.",
    "Even if I knew that tomorrow the world would go to pieces, I would still plant my apple tree.",
    "I hated every minute of training, but I said, 'Don't quit. Suffer now and live the rest of your life as a champion.'",
    "I am enough of an artist to draw freely upon my imagination. Imagination is more important than knowledge. Knowledge is limited. Imagination encircles the world.",
    "It is during our darkest moments that we must focus to see the light.",
    "Before you diagnose yourself with depression or low self-esteem, first make sure that you are not, in fact, just surrounded by assholes.",
    "I am a little pencil in the hand of a writing God who is sending a love letter to the world.",
    "Find a place inside where there's joy, and the joy will burn out the pain.",
    "When one door closes, another door opens; but we so often look so long and regretfully upon the closed door, that we do not see the ones which open for us.",
    "This is not the end, this is not even the beginning of the end, this is just perhaps the end of the beginning.",
    "Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid.",
    "I failed in some subjects in exam, but my friend passed in all. Now he is an engineer in microsoft and i am the owner of microsoft.",
    "Be the change that you wish to see in the world. ",
    "Not all of us can do great things. But we can do small things with great love."
]

FRIENDSHIP = [
    "Somebody asked me to explain the relationship between you and me, they expected the answer as, just friends. But I simply smiled and said. Gods gift.",
    "Sound become music, movement becomes dance, smile becomes laughter & life becomes celebration. When old friend keep in touch. Happy friends day!!!",
    "There is only one thing worse than fighting with allies and that is fighting without them.",
    "Friendship is the only cement that will hold the world together.",
    "A loving memory of your smiling face, a friend like you can never replace, deep in my heart you will always stay, truly remembered ever!!",
    "Friendship is born at that moment when one person says to another: What! You too? I thought I was the only one.",
    "Only a true best friend can protect you from your immortal enemies.",
    "A poor man says work is life. A rich man says money is life. A lover says love is life but. I say my idiot friends are my life.",
    "Square has 4 ends triangle has 3 ends line has to ends life has one end but our friendship has no end!!!",
    "She is a friend of my mind. She gather me, man. The pieces I am, she gather them and give them back to me in all the right order.",
    "Friends are like money in the bank, longer you keep them, the more they are worth!!!",
    "Read it carefully and get meaning! Minimum love is friendship. But maximum friendship is love strange but true! Happy friendship day!",
    "A true friend unbosoms freely, advises justly, assists readily, adventures boldly, takes all patiently, defends courageously, and continues a friend unchangeably.",
    "Friendship is the hardest thing in the world to explain. Its not something you learn in school. But if you havent learned the meaning of friendship you really havent learned anything.",
    "Friendship is a mercury drop. If it is dropped. Impossible to recollect. So do not drop your friends!!!!",
    "I' ll never forget my high school friends.",
    "I have never considered a difference of opinion in politics, in religion, in philosophy, as a cause for withdrawing from a friend.",
    "A man must eat a peck of salt with his friend before he knows him.",
    "A stranger stabs you in the front, a friend stabs you in the back, a boyfriend stabs you in the heart, but best friends only poke each other with straws.",
    "A brother may not be a friend, but a friend will always be a brother.",
    "Good Friends Are Hard to Find, Difficult to Leave, Impossible to Forget.",
    "Friendship is not finding gold or silver among the rocks of life. It is accepting each other as coal until diamonds are formed with time!!!",
    "Friends are like sunshine They can brighten up your day,A true friend is someone who Will chase the clouds away."
    "Love is not only made for lovers. It is also made 4 true friends. A true friend can love more than a lover.",
    "A friend is someone who gives you total freedom to be yourself.",
    "True friends are never apart. Maybe in distance, but not in heart.",
    "Friends are like stars, they come and go, but the ones that stay are the ones that glow!!!!"
]

NATURE = [
    "The evolution of human mentality has put us all in vitro now behind the glass wall of our own ingenuity.",
    "Nature gives to every time and season some beauties of its own; and from morning to night, as from the cradle to the grave, it is but a succession of changes so gentle and easy that we can scarcely mark their progress.",
    "It is human nature to think wisely and act in an absurd fashion.",
    "Let a hundred flowers bloom, let a hundred schools of thought contend.",
    "The human spirit needs places where nature has not been rearranged by the hand of man.",
    "There are three principal means of acquiring knowledge... observation of nature, reflection, and experimentation. Observation collects facts; reflection combines them; experimentation verifies the result of that combination.",
    "Nature is so powerful, so strong. Capturing its essence is not easy - your work becomes a dance with light and the weather. It takes you to a place within yourself.",
    "Self-preservation is the first law of nature.",
    "Nothing is more memorable than a smell. One scent can be unexpected, momentary and fleeting, yet conjure up a childhood summer beside a lake in the mountains.",
    "For greed all nature is too little.",
    "The moral virtues, then, are produced in us neither by nature nor against nature. Nature, indeed, prepares in us the ground for their reception, but their complete formation is the product of habit.",
    "Human nature is potentially aggressive and destructive and potentially orderly and constructive.",
    "Human nature is evil, and goodness is caused by intentional activity.",
    "The sun, with all those planets revolving around it and dependent on it, can still ripen a bunch of grapes as if it had nothing else in the universe to do.",
    "Solitary trees, if they grow at all, grow strong.",
    "Nature is just enough; but men and women must comprehend and accept her suggestions.",
    "Nature is full of infinite causes that have never occurred in experience.",
    "Law is born from despair of human nature.",
    "The earth has music for those who listen.",
    "Man's nature is not essentially evil. Brute nature has been know to yield to the influence of love. You must never despair of human nature.",
    "Every flower is a soul blossoming in nature."
]

SUCCESS = [
    "Take up one idea. Make that one idea your life - think of it, dream of it, live on that idea. Let the brain, muscles, nerves, every part of your body, be full of that idea, and just leave every other idea alone. This is the way to success.",
    "Prosperity makes friends, adversity tries them.",
    "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing or learning to do.",
    "Success is a state of mind. If you want success, start thinking of yourself as a success.",
    "No one who achieves success does so without acknowledging the help of others. The wise and confident acknowledge this help with gratitude.",
    "The secret to success is to know something nobody else knows.",
    "Reading more books will only confuse you more and you will be dreaming about success instead of becoming successful yourself.",
    "Strategy is a style of thinking, a conscious and deliberate process, an intensive implementation system, the science of insuring future success.",
    "If you work just for money, you'll never make it, but if you love what you're doing and you always put the customer first, success will be yours.",
    "Success depends upon previous preparation, and without such preparation there is sure to be failure.",
    "At the end of the day, the most overwhelming key to a child's success is the positive involvement of parents.",
    "Success and failure are both part of life. Both are not permanent.",
    "Without continual growth and progress, such words as improvement, achievement, and success have no meaning.",
    "I am not bound to win, but i am bound to be true. I am not bound to succeed, but i am bound to live up to what light i have.",
    "Success is a journey, not a destination.",
    "Successful people are not gifted; they just work hard, then succeed on purpose.",
    "Success is only meaningful and enjoyable if it feels like your own.",
    "Coming together is a beginning; keeping together is progress; working together is success.",
    "The road to success is not easy to navigate, but with hard work, drive and passion, it's possible to achieve the American dream.",
    "The negative side of the American Dream comes when people pursue success at any cost, which in turn destroys the vision and the dream."
]

CODING = [
    "Web development is difficult, only then it is fun to do. You just have to set your standards. If it were to be easy, would anyone do it? ",
    "Everybody should learn to program a computer because it teaches you how to think. ",
    "Quality is a product of a conflict between programmers and testers",
    "No matter which field of work you want to go in, it is of great importance to learn at least one programming language",
    "Software is like sex: it’s better when it’s free. ",
    "If we want users to like our software, we should design it to behave like a likable person.  ",
    "Confusion is part of programming.",
    "Programming is the art of telling another human being what one wants the computer to do. ",
    "Experience is the name everyone gives to their mistakes",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. ",
    "Programming today is a race between software engineers striving to build bigger and better idiot-proof programs and the Universe trying to produce bigger and better idiots. So far, the Universe is winning. ",
    "Programming is the art of algorithm design and the craft of debugging errant code.",
    "Of course, bad code can be cleaned up. But it’s very expensive.",
    "Clean code always looks like it was written by someone who cares. ",
    "Make it work, make it right, make it fast. ",
    "Code is like humor. When you have to explain it, it’s bad.",
    "Code is like humor. When you have to explain it, it’s bad.",
    "First, solve the problem. Then, write the code. ",
    "It’s not a bug; it’s an undocumented feature.",
    "Coding like poetry should be short and concise. ",
]

ATTITUDE = [
    "God is really creative, I mean ...just look at me !",
    "i am what i am.. i will never try to be some one else.",
    "May my enemies live a long life to see my success.",
    "Im sorry my fault. I forgot youre an Idiot.",
    "Two fundamentals of cool life  Walk like you are the king OR walk like you dont care ,who is the king.",
    "You create beauty with your attitude, your behaviours, and your actions. Its all up to you",
    "My life,My rules My Attitude!!!",
    "All things are ready if our mind be so.",
    "Keep moving! Nothing new to read""Style is a reflection of your attitude and your personality.",
    "I am who I am, Your approval is not needed", "Dont Copy My Style.",
    "Stop checking my status ! Go Get A Life ",
    "Someone Asked me what is UR attitude then i simply replied ? BEING SINGLE IS MY ATTITUDE",
    "Smile in front of people who hate you Ur happiness kills them",
    "People say me bad, trust me i am the worst!!!",
    "Not always available, try your luck ;)",
    "There is no market for YOUR EMOTIONS, so never advertise your FEELINGS just display YOUR ATTITUDE.,.",
    "I enjoy when people show Attitude to me because it shows that they need an Attitude to impress me!",
    "When i was born..Devil said..?Oh Shit..!! Competition?",
    "Xcuse me, I found something under my shoes. Oh its your attitude.",
    "Style is a reflection of your attitude and your personality.",
    "I am who I am, Your approval is not needed"
]

allquotes = {
    'motivational': MOTIVATIONAL,
    'technology': TECHNOLOGY,
    'funny': FUNNY,
    'inspirational': INSPIRATIONAL,
    'friendship': FRIENDSHIP,
    'nature': NATURE,
    'success': SUCCESS,
    'coding': CODING,
    'attitude': ATTITUDE,
    'all': MOTIVATIONAL + TECHNOLOGY + FUNNY + INSPIRATIONAL + FRIENDSHIP + NATURE + SUCCESS + CODING + ATTITUDE
}


import random


# a class for throw error
class CategoryNotFoundError(Exception):
    pass


"""Function For Get All Qoutes"""


def get_quotes(category="motivational"):
    # check if category Exists or not

    if category.lower() not in allquotes:
        # raise new error

        raise CategoryNotFoundError('No such category %s' % (category))

    # return all quotes

    return allquotes[category.lower()]


# Function For Get Single Quote

def get_quote(category="motivational"):
    # get all quotes from `get_quotes` Function

    quotes = get_quotes(category.lower())

    # return random single quote

    return random.choice(quotes)

def randomquote():
    quote = get_quote("technology")
    return quote
print(randomquote())
