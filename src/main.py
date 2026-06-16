import sys
from data_parser import load_delivery_data

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

    fuel_price = project_data["scenarios"][scenario_choice]["fuel_price"]
    print(f"[INFO] Sukses memuat {len(project_data['locations'])} lokasi.")
    print(f"[INFO] Harga bensin aktif: Rp {fuel_price}/liter\n")

    print("--- HASIL EKSEKUSI ALGORITMA (Menunggu Implementasi Anggota Lain) ---")

if __name__ == "__main__":
    main()