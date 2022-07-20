import json


class JsonHelper:

    def __init__(self):
        self.quest_list = []

    def AppendQuest(self, qname, qtype, qgoal):
        if qname is not None and qtype is not None and qgoal is not None:
            new_quest = {"name": qname, "type": qtype, "goal": qgoal}
            self.quest_list.append(new_quest)

    def ClearQuest(self):
        self.quest_list.clear()

    def RemoveAtQuest(self, index):
        self.quest_list.pop(index)

    def WriteJson(self):
        if len(self.quest_list) > 0:
            with open('Quest.json', 'w') as json_file:
                json.dump(self.quest_list, json_file, indent=4)

    def __ReadJson(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
        return data

    def AppendJsonData(self, path):
        json_data = self.__ReadJson(path)
        if json_data is not None:
            for data in json_data:
                self.AppendQuest(data["name"], data["type"], data["goal"])

    def Refresh(self):
        return self.quest_list

listQuest = []
dictQuest1 = {"name": "save princess", "type": "count", "goal": 2}
dictQuest2 = {"name": "kill princess", "type": "count", "goal": 4}

listQuest.append(dictQuest1)
listQuest.append(dictQuest2)

json_string = json.dumps(listQuest, indent=4)

print(json_string)

json_load = json.loads(json_string)

print(json_load[0]["name"])

# json_str = json.dumps(json_obj, indent=4)
# print(json_str)

# json_load = json.loads(json_str)

# print(json_load['quest'][1]['name'])
