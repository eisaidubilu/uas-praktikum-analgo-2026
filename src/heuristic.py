import time

def calculate_fuel_cost(route, distance_matrix, locations, weights, fuel_price):
    """
    Fungsi simulasi kalkulasi BBM dinamis (Sesuai spesifikasi teknis).
    Beban paket berkurang setiap kali kurir mampir di lokasi pelanggan.
    Rumus rasio: 0.05 liter/km saat penuh, 0.02 liter/km saat kosong.
    """
    total_fuel_cost = 0.0
    
    # Hitung total beban seluruh paket yang dibawa dari Hub di awal keberangkatan
    total_initial_weight = sum(weights.values())
    current_load = total_initial_weight
    
    # Telusuri rute dari satu titik ke titik berikutnya
    for i in range(len(route) - 1):
        u = route[i]
        v = route[i+1]
        distance = distance_matrix[u][v]
        
        # Hitung rasio konsumsi bensin secara linier berdasarkan sisa beban paket
        if total_initial_weight > 0:
            current_ratio = 0.02 + (0.03 * (current_load / total_initial_weight))
        else:
            current_ratio = 0.02
            
        # Hitung konsumsi bensin dan biaya untuk segmen jalan ini
        fuel_needed = distance * current_ratio
        total_fuel_cost += fuel_needed * fuel_price
        
        # Kurangi beban paket setelah kurir sampai di lokasi pelanggan tersebut
        loc_name = locations[v]
        if loc_name in weights:
            current_load -= weights[loc_name]
            if current_load < 0:
                current_load = 0
                
    return total_fuel_cost

def solve_greedy(distance_matrix, locations, weights, fuel_price):
    # Mulai penghitung waktu eksekusi presisi tinggi (milidetik)
    start_time = time.perf_counter()
    
    num_locations = len(locations)
    visited = [False] * num_locations
    
    # Mulai dari Indeks 0
    current_node = 0
    visited[current_node] = True
    route = [current_node]
    
    # Selalu pilih tetangga terdekat berikutnya
    for _ in range(num_locations - 1):
        nearest_node = -1
        min_distance = float('inf')
        
        for next_node in range(num_locations):
            if not visited[next_node] and distance_matrix[current_node][next_node] < min_distance:
                min_distance = distance_matrix[current_node][next_node]
                nearest_node = next_node
                
        # Pindah ke titik terdekat yang ditemukan
        visited[nearest_node] = True
        route.append(nearest_node)
        current_node = nearest_node

    # Kembali ke Hub dari lokasi terakhir pengantaran
    route.append(0)

    # Menghitung total jarak
    total_distance = 0
    for i in range(len(route) - 1):
        total_distance += distance_matrix[route[i]][route[i+1]]
    
    # Hitung pengeluaran operasional (Biaya BBM + Biaya Komputasi Server)
    fuel_cost = calculate_fuel_cost(route, distance_matrix, locations, weights, fuel_price)
    
    # Akhiri penghitung waktu eksekusi
    end_time = time.perf_counter()
    execution_time_ms = (end_time - start_time) * 1000 
    
    # Rumus: WaktuEksekusiAlg × Rp50
    server_cost = execution_time_ms * 50
    tco = fuel_cost + server_cost
    
    return {
        "route": route,
        "total_distance": total_distance,
        "execution_time_ms": execution_time_ms,
        "fuel_cost": fuel_cost,
        "server_cost": server_cost,
        "tco": tco
    }

def print_cli_output(result, locations):
    route_names = [locations[idx] for idx in result["route"]]
    
    print("\n" + "=" * 70)
    print("         HASIL SIMULASI ALGORITMA A (HEURISTIK - GREEDY)        ")
    print("=" * 70)
    print(f"Urutan Rute Pelayanan : \n{' -> '.join(route_names)}")
    print("-" * 70)
    print(f"Total Jarak           : {result['total_distance']} km")
    print(f"Waktu Eksekusi Program: {result['execution_time_ms']:.6f} ms")
    print("-" * 70)
    print("RINCIAN TOTAL COST OF OWNERSHIP (TCO):")
    print(f"   Biaya Bahan Bakar (BBM) : Rp {result['fuel_cost']:,.2f}")
    print(f"   Biaya Server Komputasi  : Rp {result['server_cost']:,.2f}  (Waktu x Rp50)")
    print(f"   Total Pengeluaran (TCO) : Rp {result['tco']:,.2f}")
    print("=" * 70 + "\n")