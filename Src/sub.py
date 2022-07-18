import json
from matplotlib.font_manager import json_load
from sqlalchemy import null

class JsonHelper:
    
    def __init__(self):
        self.quest_list = []
        
    def AppendQuest(self, qname, qtype, qgoal):
        if qname != null and  qtype != null and qgoal != null :
            newQuest = {"name": qname, "type": qtype, "goal": qgoal}
            self.quest_list.append(newQuest)


listQuest = []
dictQuest1 = {"name": "save princess", "type": "count", "goal": 2}
dictQuest2 = {"name": "kill princess", "type": "count", "goal": 4}

listQuest.append(dictQuest1)
listQuest.append(dictQuest2)

json_string = json.dumps(listQuest, indent=4)

print(json_string)

json_load = json.loads(json_string)

print(json_load[0]["name"])

#json_str = json.dumps(json_obj, indent=4)
#print(json_str)

#json_load = json.loads(json_str)

#print(json_load['quest'][1]['name'])
