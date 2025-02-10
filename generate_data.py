from utils import generate_json_file
from db_connect import execute_query


def generate_classes_json_files():
    output_dir = './output/config/classes'
    
    get_data_class_query = 'SELECT c.id_data, d."name", d.description FROM "data_class" c INNER JOIN "data" d ON d.id = c.id_data;'
    get_class_query = 'SELECT id, name, description FROM "class";'
    
    data_classes = execute_query(get_data_class_query)
    classes = execute_query(get_class_query)
    
    print("-" * 70)
    print("🏁 Starting the generation of the Data Class JSON file...")
    print("-" * 70)
    
    for i in range(len(data_classes)):
        for j in range(len(classes)):
            
            print("⏳ Generating JSON file for data class:", data_classes[i][1])
            
            result = {
                "data": {
                    "id": data_classes[i][0],
                    "name": data_classes[i][1],
                    "description": data_classes[i][2]
                },
                "classes": [
                    {
                        "id": classes[j][0],
                        "name": classes[j][1],
                        "description": classes[j][2]
                    }
                ]
            }
            
            filename = f"{data_classes[i][1].lower().replace(' ', '_')}.json"
            generate_json_file(result, output_dir, filename)


def generate_filter_json_files():
    output_dir = './output/config/filters'
    
    get_filter_data_query = 'SELECT id, name, description FROM "data";'
    filter_data_result = execute_query(get_filter_data_query)
    
    print("\n" + "-" * 70)
    print("🏁 Starting the generation of the Filter JSON file...")
    print("-" * 70)
    
    for i in range(len(filter_data_result)):
        
        print("⏳ Generating JSON file for filter data:", filter_data_result[i][1])
        
        result = {
            "id": filter_data_result[i][0],
            "name": filter_data_result[i][1],
            "description": filter_data_result[i][2]
        }
        
        filename = f"{filter_data_result[i][1].lower().replace(' ', '_')}.json"
        generate_json_file(result, output_dir, filename)
    
    
def generate_lois_json_files():
    output_dir = './output/config/lois'
    
    get_filter_data_query = 'SELECT id, name, description FROM "data";'
    get_loi_data_query = 'SELECT id, name FROM loi l ;'
    
    filter_data_result = execute_query(get_filter_data_query)
    loi_data_result = execute_query(get_loi_data_query)
        
    print("\n" + "-" * 70)
    print("🏁 Starting the generation of the LOI JSON file...")
    print("-" * 70)
    
    for i in range(len(filter_data_result)):
        
        print("⏳ Generating JSON file for loi data:", filter_data_result[i][1])
        
        lois_list = []
        for j in range(len(loi_data_result)):            
            lois_list.append({
                "gid": loi_data_result[j][0],
                "name": loi_data_result[j][1],
                "loinames": []
            })
        
        result = {
            "data": {
                "id": filter_data_result[i][0],
                "name": filter_data_result[i][1],
                "description": filter_data_result[i][2]
            },
            "lois": lois_list
        }
        
        
        filename = f"{filter_data_result[i][1].lower().replace(' ', '_')}.json"
        generate_json_file(result, output_dir, filename)
        
        
def generate_periods_json_files():    
    output_dir = './output/config/periods'
    
    get_filter_data_query = 'SELECT id, name, description FROM "data";'
    get_period_data_query = 'SELECT d.id, p.start_date, p.end_date   FROM "data" d inner join "period" p on p.id_data = d.id'
       
    filter_data_result = execute_query(get_filter_data_query)
    period_data_result = execute_query(get_period_data_query)
    
    print("\n" + "-" * 70)
    print("🏁 Starting the generation of the Period JSON file...")
    print("-" * 70)
    
    periods_list = []
    for j in range(len(period_data_result)):        
        periods_list.append({
            "id": period_data_result[j][0],
            "start_date": period_data_result[j][1],
            "end_date": period_data_result[j][2]
        })
    
    for i in range(len(filter_data_result)):  
        
        print("⏳ Generating JSON file for period data:", filter_data_result[i][1])
        
        period_list = []    
        for period in periods_list:
            if period['id'] == filter_data_result[i][0]:                            
                period_list.append({
                    "start_date": {
                        "year": period['start_date'].year,
                        "month": period['start_date'].month,
                        "day": period['start_date'].day
                    },
                    "end_date": {
                        "year": period['end_date'].year,
                        "month": period['end_date'].month,
                        "day": period['end_date'].day
                    },
                    "features": []
                })
        
        result = {
            "data": {
                "id": filter_data_result[i][0],
                "name": filter_data_result[i][1],
                "description": filter_data_result[i][2]
            },
            "periods": period_list
        }
        
        filename = f"{filter_data_result[i][1].lower().replace(' ', '_')}.json"
        generate_json_file(result, output_dir, filename)
        
def generate_loinames_json_files():
    output_dir = './output/config/loinames'
    
    get_filter_data_query = 'SELECT id, name, description FROM "data";'
    get_loinames_data_query = '''
        select dll.id_data, d."name", dll.id_loi_loinames, l.id, l."name", ln.name as "loiname", ln.codibge from data_loi_loinames dll 
        inner join data d on d.id = dll.id_data
        inner join loi_loinames ll on ll.id = dll.id_loi_loinames
        inner join loi l on l.id = ll.id_loi 
        inner join loinames ln on ln.gid = ll.gid_loinames 
    '''    
    
    filter_data_result = execute_query(get_filter_data_query)
    loinames_data_result = execute_query(get_loinames_data_query)
    
    print("\n" + "-" * 70)
    print("🏁 Starting the generation of the LOI Names JSON file...")
    print("-" * 70)
    
    for filtered_item in filter_data_result:
        grouped_loinames = {}
        
        for loi_item in loinames_data_result:
            if filtered_item[0] == loi_item[0]:
                group_id = loi_item[3]  # Group ID
                
                if group_id not in grouped_loinames:
                    grouped_loinames[group_id] = []  # Create a new group if it doesn't exist
                
                grouped_loinames[group_id].append(loi_item)  # Append the LOI item to the group
        
        lois_grouped_data = {}
        
        for group_id, loi_items in grouped_loinames.items():
            for loi in loi_items:
                loi_group_id = loi[3]
                loi_group_name = loi[4]
                
                if loi_group_id not in lois_grouped_data:
                    lois_grouped_data[loi_group_id] = {
                        "gid": loi_group_id,
                        "name": loi_group_name,
                        "loinames": []
                    }
                
                loi_entry = {
                    "gid": loi[2],
                    "loiname": loi[5]
                }
                
                if loi_group_id == 2:
                    loi_entry["codibge"] = loi[6]
                
                lois_grouped_data[loi_group_id]["loinames"].append(loi_entry)
        
        result_json = {
            "data": {
                "id": filtered_item[0],
                "name": filtered_item[1],
                "description": filtered_item[2]
            },
            "lois": list(lois_grouped_data.values())
        }
        
        json_filename = f"{filtered_item[1].lower().replace(' ', '_')}.json"
        generate_json_file(result_json, output_dir, json_filename)
    
    
if __name__ == "__main__":
    generate_classes_json_files()
    generate_filter_json_files()
    generate_lois_json_files()
    generate_periods_json_files()
    generate_loinames_json_files()