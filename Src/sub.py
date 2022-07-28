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
        return True

    def ClearQuest(self):
        self.quest_list.clear()

    def RemoveAtQuest(self, index):
        self.quest_list.pop(index)

    def WriteJson(self):
        if self.length() > 0:
            with open('Quest.json', 'w', encoding='UTF-8') as json_file:
                jsonObject = {'Quests': self.quest_list}
                json.dump(jsonObject, json_file, indent=4, ensure_ascii=False)
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
            json_data = json_data['Quests']
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