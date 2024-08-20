import json
from collections import deque
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
    EXTERNAL_CLASS_AND_VIEW = "ExternalClassAndView"

    # FormModel

    # AuthModel

    # FunctionalModel

    # DataIntegration

    # OrganizationModel

    # SystemManagement

    @classmethod
    def get_by_name(cls, model_type: str):
        for name, member in ModelType.__members__.items():
            if (member.value.__eq__(model_type)):
                return member
        return None

    @classmethod
    def get_values(cls):
        return [member.value for member in ModelType]


@unique
class ModuleType(Enum):
    FUNCTIONAL_MODEL = "functionalModel"
    AUTH_MODEL = "authModel"
    DATA_MODEL = "dataModel"
    FORM_MODEL = "formModel"
    DATA_INTEGRATION = "dataIntegration"
    ORGANIZATION_MODEL = "organizationModel"
    SYSTEM_MANAGEMENT = "SystemManagement"
    CODE_PART = "codePart"

    @classmethod
    def get_by_name(cls, module_type: str):
        for name, member in ModuleType.__members__.items():
            if (member.value.__eq__(module_type)):
                return member
        return None

    @classmethod
    def get_values(cls):
        return [member.value for member in ModuleType]


class ModelComponent:
    def __init__(self, type: str, id: str, links: List[str], linksV2: List[Dict[str, str]], props: Dict):
        self.type = ModelType.get_by_name(type)
        self.id = id
        self.links = links
        self.linksV2 = linksV2
        self.props = props

    def __str__(self):
        return f"ModelComponent(type={self.type}, id={self.id}, links={self.links}, linksV2={self.linksV2}, props={self.props})"

    def to_dict(self):
        _dict = self.__dict__.copy()
        _dict["type"] = self.type.value if self.type else 'unknown'
        return _dict

    @staticmethod
    def from_dict(data: Dict) -> 'ModelComponent':
        return ModelComponent(
            type=data.get('type', 'unknown'),
            id=data.get('id', ''),
            links=data.get('links', []),
            linksV2=data.get('linksV2', []),
            props=data.get('props', {})
        )


def read_graph(file_path: str) -> Dict[str, Dict[str, ModelComponent]]:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    graph = {}

    for type, components in data.items():
        graph[type] = {}
        for component_id, component_data in components.items():
            graph[type][component_id] = ModelComponent(
                type=component_data['type'],
                id=component_data['id'],
                links=component_data.get('links', []),
                linksV2=component_data.get('linksV2', []),
                props=component_data.get('props', {})
            )

    return graph


def get_component_from_graph(graph: Dict[str, Dict[str, ModelComponent]], type: str, id: str):
    components_map = graph.get(type)
    if components_map and id in components_map:
        return components_map.get(id)
    return None


def extract_subgraph(root_id: str, root_type: str, graph: Dict[str, Dict[str, ModelComponent]]) -> List[ModelComponent]:
    root = get_component_from_graph(graph, root_type, root_id)
    if not root:
        return []
    model_lst = []
    queue = deque([root])
    while queue:
        cur_component = queue.popleft()
        model_lst.append(cur_component)

        links = cur_component.linksV2 or []
        for link in links:
            component = get_component_from_graph(graph, link.get('type'), link.get('id'))
            if component:
                queue.append(component)
    return model_lst


if __name__ == "__main__":
    file_path = 'E:\\pythonProjects\\ChatDWF\\scripts\\172.21.11.55.json'
    model_graph = read_graph(file_path)
    # print(model_graph)

    sub_graph = extract_subgraph("Asset","metaItemClass",model_graph)
    for c in sub_graph:
        print(c)
