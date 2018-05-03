import functools
import command

class Intent(object):
    
    def __init__(self, bot, context):
        """
        Creates new intent for specified chatbot with given name
        Arguments:
            bot the chatbot
            name the intent name
            context the execution context holding configuration parameters
        """
        self.chatbot = bot
        self.context = context
        self.commands = []
        self.initCommands()
        
    def execute(self, nlu_data):
        """
        Executes given intent by applying appropriate command to the given
        parsed NLU data response
        """

        cmd_result=[command.do(self.chatbot, None) for command in self.commands]
        return functools.reduce(lambda result, results: result+"\n"+results, cmd_result)
    
    def initCommands(self):
        """
        The method to init specific to particular intent.
        """
        pass
        
class HelloIntent(Intent):
    def initCommands(self):
        self.commands.append(command.GreetCommand())

class GetTimeIntent(Intent):
    def initCommands(self):
        self.commands.append(command.GetTimeCommand())

class UnKnownIntent(Intent):
    def initCommands(self):
        self.commands.append(command.UnKnownCommand())

class JokeIntent(Intent):
    def initCommands(self):
        self.commands.append(command.JokesCommand())
