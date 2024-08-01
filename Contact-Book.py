
import customtkinter as cctk
from CTkMessagebox import CTkMessagebox as messagebox
cctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
cctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class ContactBookApp(cctk.CTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Contact Book")
        self.contacts = []

        # UI Elements
        self.label = cctk.CTkLabel(self, text="Contact Book", font=cctk.CTkFont("Helvetica", 16))
        self.label.grid(row=0, column=1, pady=10)

        self.add_button = cctk.CTkButton(self, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=1, column=0, padx=10, pady=10)

        self.view_button = cctk.CTkButton(self, text="View Contacts", command=self.view_contacts)
        self.view_button.grid(row=1, column=1, padx=10, pady=10)

        self.search_button = cctk.CTkButton(self, text="Search Contact", command=self.search_contact)
        self.search_button.grid(row=1, column=2, padx=10, pady=10)

        self.update_button = cctk.CTkButton(self, text="Update Contact", command=self.update_contact)
        self.update_button.grid(row=2, column=0, padx=10, pady=10)

        self.delete_button = cctk.CTkButton(self, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=2, column=1, padx=10, pady=10)

        self.exit_button = cctk.CTkButton(self, text="Exit", command=self.destroy)
        self.exit_button.grid(row=2, column=2, padx=10, pady=10)

    def add_contact(self):
        add_window = cctk.CTkToplevel(self)
        add_window.title("Add Contact")

        # UI Elements for adding a contact
        cctk.CTkLabel(add_window, text="Store Name:").grid(row=0, column=0)
        store_name_entry = cctk.CTkEntry(add_window)
        store_name_entry.grid(row=0, column=1)

        cctk.CTkLabel(add_window, text="Phone Number:").grid(row=1, column=0)
        phone_number_entry = cctk.CTkEntry(add_window)
        phone_number_entry.grid(row=1, column=1)

        cctk.CTkLabel(add_window, text="Email:").grid(row=2, column=0)
        email_entry = cctk.CTkEntry(add_window)
        email_entry.grid(row=2, column=1)

        cctk.CTkLabel(add_window, text="Address:").grid(row=3, column=0)
        address_entry = cctk.CTkEntry(add_window)
        address_entry.grid(row=3, column=1)

        add_button = cctk.CTkButton(add_window, text="Add", command=lambda: self.save_contact(
            store_name_entry.get(), phone_number_entry.get(), email_entry.get(), address_entry.get()))
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

    def save_contact(self, store_name, phone_number, email, address):
        contact = {
            "Store Name": store_name,
            "Phone Number": phone_number,
            "Email": email,
            "Address": address
        }
        self.contacts.append(contact)
        messagebox(title="Contact Book", message="Contact added successfully!",icon="check", option_1="OK")

    def view_contacts(self):
        view_window = cctk.CTkToplevel(self)
        view_window.title("View Contacts")

        if not self.contacts:
            cctk.CTkLabel(view_window, text="No contacts available.").pack(pady=10)
        else:
            for i, contact in enumerate(self.contacts, start=1):
                contact_info = f"{i}. {contact['Store Name']} - {contact['Phone Number']}"
                cctk.CTkLabel(view_window, text=contact_info).pack(pady=5)

    def search_contact(self):
        search_window = cctk.CTkToplevel(self)
        search_window.title("Search Contact")

        cctk.CTkLabel(search_window, text="Enter name or phone number:").pack()
        search_entry = cctk.CTkEntry(search_window)
        search_entry.pack(pady=10)

        search_button = cctk.CTkButton(search_window, text="Search", command=lambda: self.display_contact(search_entry.get()))
        search_button.pack(pady=10)

    def display_contact(self, search_term):
        search_result = []
        for contact in self.contacts:
            if search_term.lower() in contact['Store Name'].lower() or search_term in contact['Phone Number']:
                search_result.append(contact)

        display_window = cctk.CTkToplevel(self)
        display_window.title("Search Result")

        if not search_result:
            cctk.CTkLabel(display_window, text="No matching contacts found.").pack(pady=10)
        else:
            for i, contact in enumerate(search_result, start=1):
                contact_info = f"{i}. {contact['Store Name']} - {contact['Phone Number']}"
                cctk.CTkLabel(display_window, text=contact_info).pack(pady=5)

    def update_contact(self):
        update_window = cctk.CTkToplevel(self)
        update_window.title("Update Contact")

        cctk.CTkLabel(update_window, text="Enter name or phone number to update:").pack()
        update_entry = cctk.CTkEntry(update_window)
        update_entry.pack(pady=10)

        update_button = cctk.CTkButton(update_window, text="Update", command=lambda: self.edit_contact(update_entry.get()))
        update_button.pack(pady=10)

    def edit_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact['Store Name'].lower() or search_term in contact['Phone Number']:
                edit_window = cctk.CTkToplevel(self)
                edit_window.title("Edit Contact")

                cctk.CTkLabel(edit_window, text="Edit contact information:").pack()

                cctk.CTkLabel(edit_window, text="New Store Name:").pack()
                new_store_name_entry = cctk.CTkEntry(edit_window)
                new_store_name_entry.pack()

                cctk.CTkLabel(edit_window, text="New Phone Number:").pack()
                new_phone_number_entry = cctk.CTkEntry(edit_window)
                new_phone_number_entry.pack()

                cctk.CTkLabel(edit_window, text="New Email:").pack()
                new_email_entry = cctk.CTkEntry(edit_window)
                new_email_entry.pack()

                cctk.CTkLabel(edit_window, text="New Address:").pack()
                new_address_entry = cctk.CTkEntry(edit_window)
                new_address_entry.pack()

                save_button = cctk.CTkButton(edit_window, text="Save", command=lambda: self.save_edit(
                    contact, new_store_name_entry.get(), new_phone_number_entry.get(),
                    new_email_entry.get(), new_address_entry.get(), edit_window))
                save_button.pack(pady=10)

                return

        messagebox(title="Contact Book", message="No matching contact found for update.", icon="check", option_1="OK")

    def save_edit(self, contact, new_store_name, new_phone_number, new_email, new_address, edit_window):
        contact['Store Name'] = new_store_name if new_store_name else contact['Store Name']
        contact['Phone Number'] = new_phone_number if new_phone_number else contact['Phone Number']
        contact['Email'] = new_email if new_email else contact['Email']
        contact['Address'] = new_address if new_address else contact['Address']

        messagebox(title="Contact Book", message="Contact updated successfully!",icon="check", option_1="OK")
        edit_window.destroy()

    def delete_contact(self):
        delete_window = cctk.CTkToplevel(self)
        delete_window.title("Delete Contact")

        cctk.CTkLabel(delete_window, text="Enter name or phone number to delete:").pack()
        delete_entry = cctk.CTkEntry(delete_window)
        delete_entry.pack(pady=10)

        delete_button = cctk.CTkButton(delete_window, text="Delete", command=lambda: self.remove_contact(delete_entry.get()))
        delete_button.pack(pady=10)

    def remove_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact['Store Name'].lower() or search_term in contact['Phone Number']:
                confirm = messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {contact['Store Name']}?")
                if confirm:
                    self.contacts.remove(contact)
                    messagebox(title="Contact Book", message="Contact deleted successfully!",icon="check", option_1="OK")
                return

        messagebox(title="Contact Book", message="No matching contact found for deletion.",icon="info", option_1="OK")


if __name__ == "__main__":
    app = ContactBookApp()
    app.mainloop()