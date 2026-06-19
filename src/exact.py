import time
from heuristic import calculate_fuel_cost

class ExactTSP:
    """
    Kelas untuk menyelesaikan Travelling Salesman Problem (TSP)
    menggunakan algoritma Backtracking dengan teknik Pruning.
    """
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.best_cost = float('inf')
        self.best_path = []
        
        # Mencari edge terkecil untuk kebutuhan estimasi lower bound (pruning)
        # Membantu memangkas cabang rute yang pasti lebih mahal dari best_cost
        self.min_edge = float('inf')
        for i in range(self.n):
            for j in range(self.n):
                if i != j and self.graph[i][j] < self.min_edge:
                    self.min_edge = self.graph[i][j]

    def solve(self):
        """Memulai proses pencarian rute eksak."""
        visited = [False] * self.n
        visited[0] = True # Mulai dari Hub (indeks 0)
        self.dfs(0, visited, [0], 0)
        return self.best_path, self.best_cost

    def dfs(self, current, visited, path, cost):
        # 1. LOGIKA PRUNING (PENTING AGAR TIDAK LAMBAT)
        remaining_nodes = self.n - len(path)
        lower_bound = cost + (remaining_nodes * self.min_edge)
        if lower_bound >= self.best_cost:
            return

        # 2. BASIS REKURSI
        if len(path) == self.n:
            total_cost = cost + self.graph[current][0]
            if total_cost < self.best_cost:
                self.best_cost = total_cost
                self.best_path = path[:] + [0]
            return

        # 3. EKSPLORASI DENGAN PENGURUTAN (HEURISTIK LOKAL)
        neighbors = []
        for next_node in range(self.n):
            if not visited[next_node]:
                neighbors.append((self.graph[current][next_node], next_node))
        
        neighbors.sort()

        for dist, next_node in neighbors:
            visited[next_node] = True
            self.dfs(next_node, visited, path + [next_node], cost + dist)
            visited[next_node] = False

def solve_exact(distance_matrix, locations, weights, fuel_price):
    """Fungsi wrapper untuk menjalankan solver dan menghitung TCO."""
    
    start_time = time.perf_counter()
    
    # Inisialisasi dan jalankan algoritma
    solver = ExactTSP(distance_matrix)
    best_path, best_distance = solver.solve()
    
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000
    
    # Kalkulasi biaya finansial
    fuel_cost = calculate_fuel_cost(
        best_path, distance_matrix, locations, weights, fuel_price
    )
    server_cost = execution_time_ms * 50
    tco = fuel_cost + server_cost
    
    return {
        "route": best_path,
        "distance": best_distance,
        "execution_time_ms": execution_time_ms,
        "fuel_cost": fuel_cost,
        "server_cost": server_cost,
        "tco": tco
    }

def print_exact_output(result, locations):
    route_names = [locations[idx] for idx in result["route"]]
    
    print("\n" + "=" * 70)
    print("          HASIL SIMULASI ALGORITMA B (EXACT - BACKTRACKING)           ")
    print("=" * 70)
    print(f"Urutan Rute Pelayanan : \n{' -> '.join(route_names)}")
    print("-" * 70)
    print(f"Total Jarak           : {result['distance']} km")
    print(f"Waktu Eksekusi Program: {result['execution_time_ms']:.6f} ms")
    print("-" * 70)
    print("RINCIAN TOTAL COST OF OWNERSHIP (TCO):")
    print(f"   Biaya Bahan Bakar (BBM) : Rp {result['fuel_cost']:,.2f}")
    print(f"   Biaya Server Komputasi  : Rp {result['server_cost']:,.2f}")
    print(f"   Total Pengeluaran (TCO) : Rp {result['tco']:,.2f}")
    print("=" * 70 + "\n")