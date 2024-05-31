from telegram.ext import Updater, MessageHandler, filters

# Simple message parser
def parse_message(message):
    elements = message.split(',')
    processes = [item.strip()[len('process:'):] for item in elements if item.strip().startswith('process:')]
    applications = [item.strip()[len('app:'):] for item in elements if item.strip().startswith('app:')]
    relations = [item.strip() for item in elements if '->' in item]
    return processes, applications, relations

# Basic ArchiMate model classes
class Element:
    def __init__(self, name):
        self.name = name

class BusinessProcess(Element):
    pass

class ApplicationComponent(Element):
    pass

class Model:
    def __init__(self):
        self.elements = []
        self.relations = []

    def add_element(self, element):
        self.elements.append(element)

    def add_relation(self, source, target):
        self.relations.append((source, target))

    def get_element_by_name(self, name):
        for element in self.elements:
            if element.name == name:
                return element
        return None

    def to_json(self):
        elements_json = [{"name": element.name, "type": type(element).__name__} for element in self.elements]
        relations_json = [{"source": source.name, "target": target.name} for source, target in self.relations]
        return {"elements": elements_json, "relations": relations_json}
