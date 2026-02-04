{% macro round_value(column_name) %}
  ROUND({{ column_name }}, 2)
{% endmacro %}