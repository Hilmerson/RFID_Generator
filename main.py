import tkinter as tk
import customtkinter

def xml_gen(material_cislo, data, rfid_bc):
    RFID_STATIC = "111902000000000"
    RFID_END = "95"
    RFID_BC_STATIC = "RFID"
    XML_START = f'<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n<REHAU_RFID_PAINT_INFO creationDate="2021-11-16T02:26:40.474Z">\n'f"  "  '<EVENTLIST>\n'
    XML_END = f"  ""</EVENTLIST>\n</REHAU_RFID_PAINT_INFO>"

    xml_string = XML_START
    for i in range(len(data)):
        xml_string += (
              f"    ""<REHAU_RFID_PAINT_INFO_EVENT>\n"
              f"      ""<RFID>" + RFID_STATIC + data[i] + RFID_END + "</RFID>\n"
              f"      ""<RFID_BC>" + RFID_BC_STATIC + rfid_bc + data[i] + "</RFID_BC>\n"
              f"      ""<MATERIAL_NO>" + material_cislo + "</MATERIAL_NO>\n"
              f"    ""</REHAU_RFID_PAINT_INFO_EVENT>\n"
              )
    xml_string += XML_END

    return  xml_string

# Create a function to handle the button click event
def generate_xml():
    material_cislo = material_entry.get().upper().replace(" ", "")
    data = data_entry.get("1.0", "end-1c").replace(" ", "").split(',')
    data_clean = [x for x in data if x != '']
    rfid_bc = rfid_bc_entry.get().upper().replace(" ", "")

    final_string = xml_gen(material_cislo, data_clean, rfid_bc)
    output_text.delete(1.0, tk.END)  # Clear previous output
    output_text.insert(tk.END, final_string)


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
# Create the main GUI window
root = customtkinter.CTk()
root.title("RFID XML Generátor")
root.iconbitmap("favicon.ico")

# Create and place labels, entry fields, and buttons
material_label = customtkinter.CTkLabel(root, text="Materiál:")
material_label.grid(row=0, column=0, sticky="w")
material_label.grid_configure(padx=(20, 0))

material_entry = customtkinter.CTkEntry(root)
material_entry.grid(row=0, column=1, columnspan=2)  # Use columnspan to span two columns
material_entry.insert(tk.END, "R9080A")

rfid_bc_label = customtkinter.CTkLabel(root, text="RFID BC:")
rfid_bc_label.grid(row=1, column=0, sticky="w")
rfid_bc_label.grid_configure(padx=(20, 0))

rfid_bc_entry = customtkinter.CTkEntry(root)
rfid_bc_entry.grid(row=1, column=1, columnspan=2)  # Use columnspan to span two columns
rfid_bc_entry.insert(tk.END, "1H0")

data_label = customtkinter.CTkLabel(root, text="Hodnoty oddelené čiarkou (,):")
data_label.grid(row=2, column=0, sticky="w")
data_label.grid_configure(padx=(20, 0))

data_entry = customtkinter.CTkTextbox(root, width=350, height=100)
data_entry.grid(row=3, column=0, columnspan=2)  # Use columnspan to span two columns
data_entry.grid_configure(padx=(20, 0))

generate_button = customtkinter.CTkButton(root, text="Generovať XML", command=generate_xml)
generate_button.grid(row=4, column=0, sticky="w", columnspan=3)  # Use columnspan to span three columns
generate_button.grid_configure(padx=(20, 0))

output_text = customtkinter.CTkTextbox(root, height=500, width=500, font=('Courier New', 12))
output_text.grid(row=0, column=3, rowspan=15, padx=20, pady=10)  # Adjust rowspan to align with other elements

root.mainloop()  # Start the GUI event loop