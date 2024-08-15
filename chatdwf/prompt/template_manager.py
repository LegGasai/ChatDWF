from jinja2 import Environment, FileSystemLoader
from chatdwf.prompt import ModelComponent
import os

class TemplateManager:
    def __init__(self, template_dir):
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def get_template(self, model_component: ModelComponent):
        # fixme
        template_name = f"{model_component.type.value}.md"
        template = self.env.get_template(template_name)
        return template


if __name__ == "__main__":
    pass
    # manager = TemplateManager("templates/")
    # model = {
    #     "type":"metaItemClass",
    #     "name":"asset",
    #     "attributes": [
    #         {"name": "username", "type": "String"},
    #         {"name": "password", "type": "String"}
    #     ]
    # }
    # # 生成提示词
    # prompt = manager.get_template(model)
    # print(prompt)
    # print(prompt.render(model))


