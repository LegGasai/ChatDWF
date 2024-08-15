from abc import ABC, abstractmethod
from chatdwf.prompt import ModelComponent
from chatdwf.prompt.template_manager import TemplateManager

template_manager = TemplateManager("/templates")

class PromptGenerator(ABC):
    @abstractmethod
    def generate_prompt(self, model: ModelComponent):
        pass


class MetaItemClassGenerator(PromptGenerator):
    def generate_prompt(self, model: ModelComponent):
        template = template_manager.get_template(model)

        pass


# todo : 实现其他类型的Generator
