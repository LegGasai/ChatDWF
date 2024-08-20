# 实体名称：{{ id }}
# 实体类型：{{ type }}
# 依赖元素：{{ linksV2 }}
# 属性：
{%- if props.get('attributes') %}
{%- for attribute in props.get('attributes') %}
- 属性名：{{ attribute.attributeName }}，属性含义：{{ attribute.displayName }}，属性类型：{{ attribute.valueType }}
{%- endfor %}
{%- else %}
- 无属性
{%- endif %}