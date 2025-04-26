from lang_graph import build_graph

def main():
    query = input("Enter your research question: ")
    graph = build_graph()
    result = graph.invoke(query)
    print("\n Final Answer:")
    print(result["final_answer"])

if __name__ == "__main__":
    main()
