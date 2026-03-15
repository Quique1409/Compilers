import re
import customtkinter as ctk

tokens = [
    ('Keyword', r'\b(print|printf|int|double|float|char|varchar|none|null)\b'),
    ('Constant', r'"[^"]*"|\d+'),
    ('Identifier', r'[a-zA-Z_]\w*'),
    ('Operator', r'[+\-*/=]'),
    ('Punctuation', r'[();$]'),
    ('Space', r'\s+'),
    ('Ignore', r'.')
]

def lexer(text, tokens):
    pos = 0
    result = []
    while pos < len(text):
        match = None
        for token in tokens:
            type, pattern = token
            regex = re.compile(pattern)
            match = regex.match(text, pos)
            if match:
                if type != 'Ignore' and type != 'Space':
                    result.append(type)
                break
        if not match:
            pos += 1
        else:
            pos = match.end(0)
    return result

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Lexical Analyzer")
app.geometry("700x700")

def analyze_text():
    source_code = input_text.get("1.0", "end-1c").strip()
    if not source_code:
        return
        
    output_text.configure(state="normal")
    output_text.delete("1.0", "end")
    lines = source_code.split('\n')
    
    for line_number, line in enumerate(lines, start=1):
        line = line.strip()
        if not line:
            continue
            
        result = lexer(line, tokens)

        output_text.insert("end", f"▶ LINE {line_number}:\n", "line_header")
        output_text.insert("end", f"  {line}\n", "code_text")
        output_text.insert("end", "  ⚡ TOKEN SEQUENCE:\n  ", "header")
        output_text.insert("end", " ".join(result) + "\n")
        output_text.insert("end", "  📊 TOTAL TOKENS: ", "header")
        output_text.insert("end", f"{len(result)}\n\n", "highlight")
        
    output_text.configure(state="disabled")

title_label = ctk.CTkLabel(app, text="Lexical Analyzer", font=ctk.CTkFont(size=24, weight="bold"))
title_label.pack(pady=(20, 10))
input_frame = ctk.CTkFrame(app, fg_color="transparent")
input_frame.pack(fill="x", padx=30, pady=(10, 5))

ctk.CTkLabel(input_frame, text="Source Code:", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w")

input_text = ctk.CTkTextbox(input_frame, height=120, font=ctk.CTkFont(family="Consolas", size=14), corner_radius=10)
input_text.pack(fill="x", pady=(5, 0))
input_text.insert("0.0", 'printf("This is an example");\n\nint $a=1$;\n\nHoy Checo Perez quedó P15 en el GP de China')

analyze_btn = ctk.CTkButton(
    app, 
    text="Analyze Code", 
    command=analyze_text,
    font=ctk.CTkFont(size=15, weight="bold"),
    height=45,
    corner_radius=8,
    hover_color="#185E9E"
)
analyze_btn.pack(pady=15)

output_frame = ctk.CTkFrame(app, fg_color="transparent")
output_frame.pack(fill="both", expand=True, padx=30, pady=(5, 20))

ctk.CTkLabel(output_frame, text="Results:", font=ctk.CTkFont(size=14, weight="bold")).pack(anchor="w")

output_text = ctk.CTkTextbox(
    output_frame, 
    font=ctk.CTkFont(family="Consolas", size=14), 
    corner_radius=10, 
    fg_color="#1E1E1E",
    state="disabled"
)
output_text.pack(fill="both", expand=True, pady=(5, 0))
output_text._textbox.tag_config("line_header", foreground="#C586C0", font=("Consolas", 15, "bold"))
output_text._textbox.tag_config("code_text", foreground="#9CDCFE", font=("Consolas", 13, "italic"))
output_text._textbox.tag_config("header", foreground="#569CD6", font=("Consolas", 13, "bold"))
output_text._textbox.tag_config("highlight", foreground="#4CAF50", font=("Consolas", 14, "bold"))

app.mainloop()
