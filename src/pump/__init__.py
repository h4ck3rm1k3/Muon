#from main import Pump
import time
import pprint
import pdb; 
from xudd.actor import Actor
from pypump import PyPump
from pypump.client import Client
def verifier_callback (url):
    print("Get callback" +url + "\n")
    print('Please follow the instructions at the following URL:')
    print(url)
    return raw_input("Verifier: ") # the verifier is a string

class Pump(Actor):
    
    pump = None
    me = None

    def __init__(self, *args, **kwargs):
        #pprint.pprint(args)
        #pprint.pprint(kwargs)
        self.webfinger = kwargs['webfinger']
        del kwargs['webfinger']
        super(Pump, self).__init__(*args, **kwargs)
        self.message_routing.update({
            #"fetch_inbox": self.fetch_inbox,
            "setup": self.setup,
        })

    def setup(self, message):
        """ Sets up pypump object """
        #pdb.set_trace()
        #pprint.pprint(message.__dict__)
        #pprint.pprint(message.body)
        #webfinger = message.body["webfinger"]
        
        

        if "key" in message.body:
            key=message.body["key"]
            secret=message.body["secret"]
            token=message.body["token"]
            token_secret=message.body["token_secret"]
            self.webfinger = message.body["webfinger"]
        else:
            pprint.pprint(client.__dict__)
            pprint.pprint(self.pump.__dict__)
            key = client.key
            secret= client.secret
            pprint.pprint(self.pump.store)
         
            token = self.pump.store[self.webfinger+"-oauth-request-token"] # self.pump.get_token()[0]
            token_secret = self.pump.store[self.webfinger+"-oauth-request-secret"] # self.pump.get_token()[1]
    
            config = {
                "webfinger": self.webfinger,
                "key": key,
                "secret" : secret,
                "token" :  token,
                "token_secret" : token_secret,
            }
            
            self.hive.send_message(
                to="muon@muon",
                directive="write_config",
                body=config
            )


        #self.fetch_inbox(message)
    
        #self.send_message(
        #    to="muon@muon",
        #    directive="start_gui"            
        #    )


        inbox = self.me.inbox[:100]
        print("looking at inbox")
        pprint.pprint(inbox)
        for activity in inbox:
            pprint.pprint(activity)


    # def fetch_inbox(self, message):
    #     #if self.me is None:
    #     #    time.sleep(1)
    #     #    return self.fetch_inbox(message)

    #     #appender, redraw, update = message.body
    #     inbox = self.me.inbox[:100]
    #     for activity in inbox:
    #         pprint.pprint(activity)
    #         #appender(activity)
    #         #redraw()

    #     update()


