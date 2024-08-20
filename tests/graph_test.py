import json

from chatdwf.model.graph import read_graph


if __name__ == "__main__":
    graph = read_graph("../scripts/172.21.11.55.json")

    ex = graph.get("ExternalClassAndView")
    mc = ex.get("movie")
    print(mc.props)
    props = mc.props.get("metaClassBO")
    print(props)
    print(json.loads(props.get('packagePath')))
