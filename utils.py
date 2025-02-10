import json
import os


def create_output_dir(output_dir):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
    except Exception as e:
        print(e)
        print(f"\nError creating {output_dir} directory!\n")

def write_json_to_file(file_path, result):
    try:
        with open(file_path, 'w', encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(e)
        print(f"\nError writing to {file_path} JSON file!\n")

def generate_json_file(data, output_dir, filename):
    try:
        create_output_dir(output_dir)
        file_path = os.path.join(output_dir, filename)
        write_json_to_file(file_path, data)
        print(f"✅ {filename} JSON file successfully generated!")
    except Exception as e:
        print(e)
        print(f"\nError generating {filename} JSON file!\n")
    print("-" * 70)
    