import csv
import networkx as nx
import matplotlib.pyplot as plt
import minizinc

def solve_csp(namefile:str):
    model = minizinc.Model(namefile)
    gecode = minizinc.Solver.lookup("gecode")
    instance = minizinc.Instance(gecode, model)
    result = instance.solve()
    return result

def input_graph(namefile:str):
    with open(namefile, 'r', encoding='utf-8') as f:
        #read file csv
        reader = csv.reader(f)
        #tạo graph
        g = nx.Graph()

        for row in reader:
            #row kiểu list
            edge = row[0].split()
            node_a = int(edge[0])
            node_b = int(edge[1])
            g.add_edge(node_a, node_b)
            # print(f'constraint TinhThanh[{node_a}] != TinhThanh[{node_b}];')

        return g

def draw(csp, graph):
    color_list = ['red', 'blue', 'green', 'yellow']
    print(csp)
    # i - 1 bởi vì tỉnh đầu tiên tên là 1, mà list bằng từ 0
    node_colors = [color_list[csp["TinhThanh"][i - 1]] for i in graph.nodes()]

    nx.draw(graph, with_labels=True, node_color=node_colors, node_size=200, font_size=10)
    plt.show()

VNColor = solve_csp("VNColoring.mzn")

if str(VNColor) != "None":
    Graph = input_graph('map.csv')
    draw(VNColor, Graph)
else:
    print("Không thể vẽ với bài toán chưa thỏa mãn")