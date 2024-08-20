# 外部实体名称：{{ id }}
# 外部实体类型：{{ type }}
# 关联外部数据源：{{ datasource }}
# 依赖元素：{{ linksV2 }}
# 属性：
{%- if attributes %}
{%- for attribute in attributes %}
- 属性名：{{ attribute.attributeName }}，属性含义：{{ attribute.displayName }}，属性类型：{{ attribute.valueType }}
{%- endfor %}
{%- else %}
- 无属性
{%- endif %}