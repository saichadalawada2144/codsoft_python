import tkinter as tk
from tkinter import messagebox, simpledialog
class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
class ContactManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Manager")
        self.contacts = []
        self.name_label = tk.Label(root, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.phone_label = tk.Label(root, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.email_label = tk.Label(root, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.address_label = tk.Label(root, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(root)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)
        
        # Buttons
        self.add_button = tk.Button(root, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        
        self.view_button = tk.Button(root, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        
        self.search_button = tk.Button(root, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        
        self.update_button = tk.Button(root, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        
        self.delete_button = tk.Button(root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky="we")
        
        # View Shell
        self.view_shell = tk.Text(root, width=40, height=10)
        self.view_shell.grid(row=0, column=2, rowspan=9, padx=10, pady=5, sticky="ns")
        
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        
        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and Phone are required fields.")
        
    def view_contacts(self):
        self.view_shell.delete(1.0, tk.END)
        if self.contacts:
            for contact in self.contacts:
                self.view_shell.insert(tk.END, f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}\n\n")
        else:
            self.view_shell.insert(tk.END, "No contacts found.")
    
    def search_contact(self):
        search_query = simpledialog.askstring("Search Contact", "Enter name or phone number:")
        if search_query:
            self.view_shell.delete(1.0, tk.END)
            found_contacts = [contact for contact in self.contacts if search_query.lower() in contact.name.lower() or search_query in contact.phone]
            if found_contacts:
                for contact in found_contacts:
                    self.view_shell.insert(tk.END, f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}\n\n")
            else:
                self.view_shell.insert(tk.END, "No contacts found.")
    
    def update_contact(self):
        search_query = simpledialog.askstring("Update Contact", "Enter name or phone number:")
        if search_query:
            found_contacts = [contact for contact in self.contacts if search_query.lower() in contact.name.lower() or search_query in contact.phone]
            if found_contacts:
                contact = found_contacts[0]
                updated_name = simpledialog.askstring("Update Contact", "Enter new name:", initialvalue=contact.name)
                updated_phone = simpledialog.askstring("Update Contact", "Enter new phone number:", initialvalue=contact.phone)
                updated_email = simpledialog.askstring("Update Contact", "Enter new email:", initialvalue=contact.email)
                updated_address = simpledialog.askstring("Update Contact", "Enter new address:", initialvalue=contact.address)
                
                contact.name = updated_name if updated_name else contact.name
                contact.phone = updated_phone if updated_phone else contact.phone
                contact.email = updated_email if updated_email else contact.email
                contact.address = updated_address if updated_address else contact.address
                
                messagebox.showinfo("Success", "Contact updated successfully!")
            else:
                messagebox.showinfo("Error", "Contact not found.")
    
    def delete_contact(self):
        search_query = simpledialog.askstring("Delete Contact", "Enter name or phone number:")
        if search_query:
            found_contacts = [contact for contact in self.contacts if search_query.lower() in contact.name.lower() or search_query in contact.phone]
            if found_contacts:
                contact = found_contacts[0]
                self.contacts.remove(contact)
                messagebox.showinfo("Success", "Contact deleted successfully!")
            else:
                messagebox.showinfo("Error", "Contact not found.")
    
    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

root = tk.Tk()
app = ContactManagerApp(root)
root.mainloop()
