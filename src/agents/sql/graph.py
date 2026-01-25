from langgraph.constants import END
from langgraph.graph import StateGraph

from agents.sql.nodes import (
    make_get_schemas_node,
    make_generate_sql_node,
    make_execute_sql_node,
    make_get_tables_node,
    make_regenerate_sql_node,
    check_sql_result_node,
)
from agents.sql.state import SQLAgentState


def create_sql_graph(container, llm):
    graph = StateGraph(SQLAgentState)

    graph.add_node("get_tables", make_get_tables_node(container))
    graph.add_node("get_schemas", make_get_schemas_node(container))
    graph.add_node("generate_sql", make_generate_sql_node(llm))
    graph.add_node("execute_sql", make_execute_sql_node(container))
    graph.add_node("regenerate_sql", make_regenerate_sql_node(llm))

    graph.set_entry_point("get_tables")

    graph.add_edge("get_tables", "get_schemas")
    graph.add_edge("get_schemas", "generate_sql")
    graph.add_edge("generate_sql", "execute_sql")
    graph.add_edge("regenerate_sql", "execute_sql")

    graph.add_conditional_edges(
        "execute_sql",
        check_sql_result_node,
        {
            "final": END,
            "regenerate_sql": "regenerate_sql",
        },
    )

    return graph.compile()
