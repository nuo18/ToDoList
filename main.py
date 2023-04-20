import customtkinter

TASK_FILE = 'tasks.txt'

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("ToDo List")

        # add widgets to app
        self.task_entry = customtkinter.CTkEntry(self, width=300)
        self.task_entry.grid(row=0, column=0, padx=20, pady=10)

        self.add_button = customtkinter.CTkButton(self, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=20, pady=10)

        self.task_list = customtkinter.CTkTextbox(self, width=300,state='disabled')
        self.task_list.grid(row=1, column=0, columnspan=2, padx=20, pady=10)

        # load tasks from file
        self.load_tasks()

    # add methods to app
    def add_task(self):
        task = self.task_entry.get()
        self.task_entry.delete(0, customtkinter.END)

        # append task to task file
        with open(TASK_FILE, 'a') as f:
            f.write(f"{task}\n")

        # add task to task list
        self.task_list.configure(state='normal')
        self.task_list.insert(customtkinter.END, f"{task}\n")
        self.task_list.configure(state='disabled')

    def load_tasks(self):
        try:
            with open(TASK_FILE, 'r') as f:
                tasks = f.readlines()

            # populate task list with loaded tasks
            for task in tasks:
                self.task_list.configure(state='normal')
                self.task_list.insert(customtkinter.END, task)
                self.task_list.configure(state='disabled')

        except FileNotFoundError:
            pass


app = App()
app.mainloop()
