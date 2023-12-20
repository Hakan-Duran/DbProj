def delete(table, request):
    column = request.form['column']
    txtvalue = request.form['txtvalue']
    query = f"DELETE FROM {table} WHERE {column}='{txtvalue}';"
    return query