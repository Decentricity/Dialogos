import re

def extract_dialogue(text):
    # Initialize variables to keep track of the state
    # Inisialisasi variabel untuk melacak keadaan
    dialogue = []
    current_dialogue = []
    quote_char = None
    inside_dialogue = False
    
    # Split the text into lines
    # Memisahkan teks menjadi baris-baris
    lines = text.split('\n')
    
    for line in lines:
        # If we are not inside a dialogue block, look for the start of a new dialogue block
        # Jika kita tidak berada di dalam blok dialog, cari awal dari blok dialog baru
        if not inside_dialogue:
            match = re.match(r'^\s*([\'"])(.*)', line)
            if match:
                quote_char = match.group(1)
                line = match.group(2)
                inside_dialogue = True
        
        # If we are inside a dialogue block, look for the end of the dialogue block
        # Jika kita berada di dalam blok dialog, cari akhir dari blok dialog
        if inside_dialogue:
            match = re.match(r'(.*?)(?<!\\)' + re.escape(quote_char) + r'(.*)', line)
            if match:
                current_dialogue.append(match.group(1))
                dialogue.append(''.join(current_dialogue))
                current_dialogue = []
                line = match.group(2)
                inside_dialogue = False
        
        # If we are still inside a dialogue block, add the current line to the current dialogue
        # Jika kita masih berada di dalam blok dialog, tambahkan baris saat ini ke dialog saat ini
        if inside_dialogue:
            current_dialogue.append(line)
    
    # Reformat the dialogue into chat format
    # Reformat dialog menjadi format obrolan
    chat_format = '\n'.join(dialogue)
    
    return chat_format

def process_text_file(input_file, output_file):
    # Read the content of the input file
    # Membaca konten dari file masukan
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Extract and reformat the dialogue
    # Ekstrak dan reformat dialog
    chat_format = extract_dialogue(content)
    
    # Write the reformatted dialogue to the output file
    # Tulis dialog yang telah diformat ulang ke file keluaran
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(chat_format)

# Example usage
# Contoh penggunaan
input_file = './path_to_input_text.txt'
output_file = './path_to_output_chat.txt'
process_text_file(input_file, output_file)
