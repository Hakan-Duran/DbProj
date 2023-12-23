def insert(table, request):
    form_keys = request.form.keys()
    columns = list(form_keys)
    columns = [col for col in form_keys if request.form.get(col, '').strip()]  # Filter out empty or None values
    
    # Construct the SQL query dynamically based on the available data
    columns_values = [(col, request.form.get(col, "NULL")) for col in columns if col in form_keys]
    
    # Surround string values with single quotes in the VALUES clause
    formatted_values = [f"'{val}'" if isinstance(val, str) else val for _, val in columns_values]

    # Construct the SQL query
    query = f"INSERT INTO {table} ({', '.join(col for col, _ in columns_values)}) VALUES ({', '.join(str(val) for val in formatted_values)})"
    
    return query
    