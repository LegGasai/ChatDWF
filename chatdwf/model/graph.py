from typing import List, Dict
from enum import Enum, unique


@unique
class ModelType(Enum):
    # DataModel
    META_ITEM_CLASS = "metaItemClass"
    META_DATA_SOURCE = "metaDataSource"
    META_ATTRIBUTE = "metaAttribute"
    META_RELATION_CLASS = "metaRelationClass"
    CLASS_SCRIPT = "classScript"
    EXTERNAL_CLASS = "ExternalClass"

    # FormModel

    # AuthModel

    # FunctionalModel

    # DataIntegration

    # OrganizationModel

    # SystemManagement

    def get_by_name(model_type: str):
        for name, member in ModelType.__members__.items():
            if (name.__eq__(model_type)):
                return member
        return None




class ModelComponent:
    def __init__(self, type: str, id: str, links: List[str], props: Dict):
        self.type = ModelType.get_by_name(type)
        self.id = id
        self.links = links
        self.props = props




# todo: 从data/下读取json模型图
def read_graph(file_path: str):
    pass