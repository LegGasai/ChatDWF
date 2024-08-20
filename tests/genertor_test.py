import json

from chatdwf.prompt.prompt_genertor import PromptGeneratorFactory
from chatdwf.model.graph import ModelComponent, read_graph, get_component_from_graph


if __name__ == "__main__":
    graph = read_graph("../scripts/172.21.11.55.json")
    mc = get_component_from_graph(graph,"metaDataSource","7C2024BE35B0054D9C38AD6784A59FA0" )

    print(mc)
    generator = PromptGeneratorFactory.get_generator(mc.type)
    print(generator.generate_prompt(mc))
