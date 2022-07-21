import json


class JsonHelper:

    def __init__(self):
        self.quest_list = []
        self.contain_num = 0

    def AppendQuest(self, qname, qtype, qgoal, callLoad = False):
        if qname == '' or qtype == '선택' or qgoal == '':
            return False

        if not callLoad:
            for n in range(self.contain_num, len(self.quest_list)):
                if qname in self.quest_list[n]["name"]:
                    self.contain_num = n
                    return False

        new_quest = {"name": qname, "type": qtype, "goal": qgoal}
        self.quest_list.append(new_quest)
        print(self.quest_list)
        return True

    def ClearQuest(self):
        self.quest_list.clear()
        print(self.quest_list)

    def RemoveAtQuest(self, index):
        self.quest_list.pop(index)
        print(self.quest_list)

    def WriteJson(self):
        if self.length() > 0:
            with open('Quest.json', 'w', encoding='UTF-8') as json_file:
                json.dump(self.quest_list, json_file, indent=4, ensure_ascii=False)
            return True
        else:
            return False

    def __ReadJson(self, path):
        with open(path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        return data

    def AppendJsonData(self, path):
        json_data = self.__ReadJson(path)
        if json_data is not None:
            for data in json_data:
                self.AppendQuest(data["name"], data["type"], data["goal"], True)

            self.contain_num = self.length()
            return True
        else:
            return False

    def Get(self):
        return self.quest_list

    def length(self):
        return len(self.quest_list)

# listQuest = []
# dictQuest1 = {"name": "save princess", "type": "count", "goal": 2}
# dictQuest2 = {"name": "kill princess", "type": "count", "goal": 4}

# listQuest.append(dictQuest1)
# listQuest.append(dictQuest2)

# json_string = json.dumps(listQuest, indent=4)

# print(json_string)

# json_load = json.loads(json_string)

# print(json_load[0]["name"])

# json_str = json.dumps(json_obj, indent=4)
# print(json_str)

# json_load = json.loads(json_str)

# print(json_load['quest'][1]['name'])
