def update(table, request):
    # Get WHERE condition
    where_column = request.form.get('where_column')
    where_value = request.form.get('where_value')

    # Construct WHERE clause
    where_clause = f"{where_column} = '{where_value}'"

    # Get update columns and values
    update_columns = [key for key in request.form.keys() if key.startswith('update_column_')]
    new_columns = [request.form.get(key) for key in update_columns]
    new_values = [request.form.get(f'new_value_{index}') for index in range(1, len(update_columns) + 1)]

    # Construct SET clause
    set_clause = ', '.join([f"{column} = '{value}'" for column, value in zip(new_columns, new_values)])

    # Construct the SQL query
    query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"

    return query