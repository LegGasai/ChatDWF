import os
from typing import List
from jinja2 import Environment, FileSystemLoader, ChoiceLoader
from chatdwf.prompt import ModelComponent


class TemplateManager:
    def __init__(self, template_dir: List[str]):
        loaders = []
        for dir in template_dir:
            loaders.append(FileSystemLoader(dir))
        self.env = Environment(loader=ChoiceLoader(loaders))

    def get_template(self, model_component: ModelComponent):
        # fixme
        template_name = f"{model_component.type.value}.md"
        template = self.env.get_template(template_name)
        return template


if __name__ == "__main__":
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

    from chatdwf.model.graph import ModuleType
    template_dirs = list(map(lambda x: f"templates/{x}", ModuleType.get_values()))
    template_manager = TemplateManager(template_dirs)
    mc = ModelComponent("metaItemClass", "asset", [], [], {
        "attributes": [{
            "id": "60852BCCF21D804CA11FA0AA2CB3B6E2",
            "className": "Asset",
            "attributeName": "assetName",
            "displayName": "设备名称",
            "valueType": "String",
        }, {
            "id": "DC3D51E53893264BB6FF500D407B8098",
            "className": "Asset",
            "attributeName": "assetDesc",
            "displayName": "设备描述",
            "attributeCategory": "Variable",
            "valueType": "String",
        }, {
            "id": "8B12AF1184F14344A7762A16DADF564A",
            "className": "Asset",
            "attributeName": "assetState",
            "displayName": "设备状态",
            "attributeCategory": "Variable",
            "valueType": "String",
        }
        ]
    })
    t = template_manager.get_template(mc)
    print(mc)
    print(mc.to_dict())
    print(t.render(mc.to_dict()))


