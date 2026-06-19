import sys
from data_parser import load_delivery_data
from heuristic import solve_greedy, print_cli_output
from exact import solve_exact, print_exact_output

def main():
    # Validasi parameter CLI
    if len(sys.argv) < 3 or sys.argv[1] != "--scenario":
        print("Format Salah! Gunakan: python src/main.py --scenario [subsidy|crisis]")
        sys.exit(1)

    scenario_choice = sys.argv[2].lower()
    if scenario_choice not in ["subsidy", "crisis"]:
        print("Error: Skenario harus 'subsidy' atau 'crisis'!")
        sys.exit(1)

    print(f"=== PIPELINE SIMULASI: {scenario_choice.upper()} ===")

    # Membaca data dari JSON
    project_data = load_delivery_data("data/dataset.json")
    if not project_data:
        sys.exit(1)

    # Trimming dataset (ambil 12 lokasi) 
    n_limit = 12
    project_data["locations"] = project_data["locations"][:n_limit]
    project_data["matrix"] = [row[:n_limit] for row in project_data["matrix"][:n_limit]]
    
    # Filter bobot paket hanya untuk lokasi yang terpakai
    trimmed_weights = {}
    for loc in project_data["locations"]:
        trimmed_weights[loc] = project_data["weights"].get(loc, 0)
    project_data["weights"] = trimmed_weights

    fuel_price = project_data["scenarios"][scenario_choice]["fuel_price"]
    print(f"Sukses memuat {len(project_data['locations'])} lokasi.")
    print(f"Harga bensin aktif: Rp {fuel_price}/liter")

    # EKSEKUSI HEURISTIK
    hasil_greedy = solve_greedy(
        distance_matrix=project_data["matrix"],
        locations=project_data["locations"],
        weights=project_data["weights"],
        fuel_price=fuel_price
    )
    
    # Tampilkan hasil ke terminal layar komputer
    print_cli_output(hasil_greedy, project_data["locations"])

    # EKSEKUSI EKSAK 
    hasil_exact = solve_exact(
        distance_matrix=project_data["matrix"],
        locations=project_data["locations"],
        weights=project_data["weights"],
        fuel_price=fuel_price
    )
    
    # Tampilkan hasil Algoritma Eksak
    print_exact_output(hasil_exact, project_data["locations"])
    
    # Analisis 
    print("=== KOMPARASI TCO ===")
    print(f"Heuristik: Rp {hasil_greedy['tco']:,.2f}")
    print(f"Eksak    : Rp {hasil_exact['tco']:,.2f}")


if __name__ == "__main__":
    main()