实体类描述：这边写实体类的含义，使用方法。比如实体类.属性名操作实体类属性

# 实体名称：{{ name }}
# 实体类型：{{ type }}
# 属性
{% for attribute in attributes %}
- 属性名：{{ attribute.name }}，属性类型：{{ attribute.type }}
{% endfor %}





