line_count = 0

with open('t8.shakespeare.txt', 'r') as f_var:
    for line in f_var:
        line_count += 1

        if 'the' in line or 'The' in line:
            new_line = line.replace(' the ', ' The ').replace(' The ', ' THE ')

            print(f"[{line_count}] {new_line.strip()}")
