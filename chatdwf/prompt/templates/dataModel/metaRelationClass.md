# 关联类名称：{{ id }}
# 关联类类型：{{ type }}
# 依赖元素：{{ linksV2 }}
# 左类：名称：{{ leftRole }}，类型：{{ leftClass }}
# 右类：名称：{{ rightRole }}，类型：{{ rightClass }}
# 关联属性：
{%- if props.get('attributes') %}
{%- for attribute in props.get('attributes') %}
- 属性名：{{ attribute.attributeName }}，属性含义：{{ attribute.displayName }}，属性类型：{{ attribute.valueType }}
{%- endfor %}
{%- else %}
- 无属性
{%- endif %}