import random
import datetime

class Command(object):

    def do(self, bot, entity):
        """
        Execute command's action for specified intent.
        Arguments:
            bot the chatbot
            entity the parsed NLU entity
        """
        pass


class GreetCommand(Command):
    """
    The command to greet user
    """
    
    def __init__(self):
        """
        Default constructor which will create list of gretings to be picked
        randomly to make our bot more human-like
        """
        self.greetings = ["Hey!", "Hello!", "Hi there!", "Hallo!", "How are you!"]
    
    def do(self, bot, entity):
        return(random.choice(self.greetings))


class GetTimeCommand(Command):
    """
    The command to get current time
    """

    def do(self, bot, entity):
        return datetime.datetime.now().strftime("It is %I:%M %p")


class UnKnownCommand(Command):
    """
    The command to get current time
    """

    def do(self, bot, entity):
        return "I'm sorry! Could you please paraphrase?"


class JokesCommand(Command):
    """
    The command to get current time
    """

    def __init__(self):
        self.jokes = [
            "I'm the humblest person I know.",
            "We never make misteaks.",
            "87.5% of all statistics are made up.",
            "Here, take this placebo.",
            "We Poms hate being called whingers.",
            "Nostalgia isn't what it used to be.",
            "What do you call a fish without eyes? Fsh.",
            "What do you call an alligator detective? An investi-gator.",
            "What lights up a soccer stadium? A soccer match.",
            "Why shouldn't you write with a broken pencil? Because it's pointless.",
            "If athletes get athlete's foot, what do elves get? Mistle-toes.",
            "What's brown and sticky? A stick.",
            "What did the policeman say to his bellybutton? You're under a vest.",
            "What do you call a pig that does karate? A pork chop.",
            "What kind of ghost has the best hearing? The eeriest.",
            "When do computers overheat? When they need to vent.",
            "What kind of music do planets like? Neptunes.",
            "Where can you buy chicken broth in bulk? The stock market.",
            "Why do bees have sticky hair? Because they use honeycombs.",
            "How do rabbits travel? By hareplanes.",
            "How do you tell if a vampire is sick? By how much he is coffin.",
            "What do you call a cow with two legs? Lean beef!"
        ]

    def do(self, bot, entity):
        return random.choice(self.jokes)