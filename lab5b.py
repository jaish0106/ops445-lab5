#!/usr/bin/env python3
# Author ID: ajjayaratnam

def read_file_string(file_name):
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

def append_file_string(file_name, string_of_lines):
    """Appends the string to the end of the specified file."""
    with open(file_name, 'a') as f:
        f.write(string_of_lines)

def write_file_list(file_name, list_of_lines):
    """Writes each item in the list as a new line in the specified file."""
    with open(file_name, 'w') as f:
        for line in list_of_lines:
            f.write(line + '\n')

def copy_file_add_line_numbers(file_name_read, file_name_write):
    """Copies content from file_name_read to file_name_write, adding line numbers."""
    with open(file_name_read, 'r') as read_f, open(file_name_write, 'w') as write_f:
        for i, line in enumerate(read_f, start=1):
            write_f.write(f"{i}:{line}")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
