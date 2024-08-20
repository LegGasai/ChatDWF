import json
import os.path
import traceback
from abc import ABC, abstractmethod
from typing import Dict
from chatdwf.utils import get_logger
from chatdwf.prompt import ModelComponent
from chatdwf.prompt.template_manager import TemplateManager
from chatdwf.model.graph import ModelType, ModuleType

logger = get_logger(__name__)

current_dir = os.path.dirname(os.path.abspath(__file__))
template_dirs = list(map(lambda x: os.path.join(current_dir, f"templates/{x}"), ModuleType.get_values()))
template_manager = TemplateManager(template_dirs)


class PromptGenerator(ABC):
    @abstractmethod
    def generate_prompt(self, model: ModelComponent) -> str:
        pass


class MetaItemClassGenerator(PromptGenerator):
    def generate_prompt(self, model: ModelComponent) -> str:
        try:
            template = template_manager.get_template(model)
            return template.render(model.to_dict())
        except Exception as e:
            logger.error(traceback.format_exc())
            return ""


class MetaRelationClassGenerator(PromptGenerator):
    def generate_prompt(self, model: ModelComponent) -> str:
        try:
            template = template_manager.get_template(model)
            model_dict = model.to_dict()
            if model_dict.get("props") and model_dict.get("props").get("metaRelationBO"):
                meta_info = model_dict.get("props").get("metaRelationBO")
                model_dict["leftClass"] = meta_info.get("leftClass", "")
                model_dict["leftRole"] = meta_info.get("leftRole", "")
                model_dict["rightClass"] = meta_info.get("rightClass", "")
                model_dict["rightRole"] = meta_info.get("rightRole", "")
            return template.render(model_dict)
        except Exception as e:
            logger.error(traceback.format_exc())
            return ""

class ExternalClassAndViewGenerator(PromptGenerator):
    def generate_prompt(self, model: ModelComponent) -> str:
        try:
            template = template_manager.get_template(model)
            model_dict = model.to_dict()
            if model_dict.get("props") and model_dict.get("props").get("metaClassBO"):
                meta_info = model_dict.get("props").get("metaClassBO")
                model_dict["datasource"] = meta_info.get("dataSourceOid", "")
                attributes_dict = json.loads(meta_info.get("packagePath",""))
                attributes = []
                for key, value in attributes_dict.items():
                    if(type(value) == dict):
                        attributes.append({"attributeName": key, "displayName": value.get("displayName"), "valueType": "Unknown"})
                print(attributes)
                model_dict["attributes"] = attributes
                return template.render(model_dict)
        except Exception as e:
            logger.error(traceback.format_exc())
            return ""

class MetaDataSourceGenerator(PromptGenerator):
    def generate_prompt(self, model: ModelComponent) -> str:
        try:
            template = template_manager.get_template(model)
            model_dict = model.to_dict()
            if model_dict.get("props"):
                props_dict = model_dict.get("props")
                model_dict["dataSourceType"] = props_dict.get("dataSourceType", "Unknown")
                model_dict["displayName"] = props_dict.get("displayName", "")
                model_dict["dataBaseName"] = props_dict.get("dataBaseName", "null")
            return template.render(model_dict)
        except Exception as e:
            logger.error(traceback.format_exc())
            return ""
# todo : 实现其他类型的Generator,并根据模型元素特点实现generate_prompt方法


class DefaultPromptGenerator(PromptGenerator):
    def generate_prompt(self, model: ModelComponent) -> str:
        return ""


class PromptGeneratorFactory:
    _default_generator = DefaultPromptGenerator()
    _generators: Dict[ModelType, PromptGenerator] = {
        ModelType.META_ITEM_CLASS: MetaItemClassGenerator(),
        ModelType.META_RELATION_CLASS: MetaRelationClassGenerator(),
        ModelType.EXTERNAL_CLASS_AND_VIEW: ExternalClassAndViewGenerator(),
        ModelType.META_DATA_SOURCE: MetaDataSourceGenerator(),
        # todo : 其他类型的Generator
    }

    @staticmethod
    def get_generator(model_type: ModelType) -> PromptGenerator:
        if model_type in PromptGeneratorFactory._generators:
            return PromptGeneratorFactory._generators[model_type]
        return PromptGeneratorFactory._default_generator
