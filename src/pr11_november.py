from tkinter import *

import json
import requests


link = "https://api.github.com/users/kubernetes"


def get_data():
    with open("pr11_out_november.json", 'w', encoding='utf-8') as f:
        link_value = field_link.get() # чтобы вводить ссылку вручную
        # link_value = link # чтобы вводить ссылку автоматически (для тестирования)
        response = requests.get(link_value)

        json.dump(response.json(), f)
        f.close()

    with open("pr11_out_november.json", encoding='utf-8') as f:
        data = json.load(f)
        f.close()

    with open("pr11_out_1_november.json", 'w', encoding='utf-8') as f:
        f.write(f"'company': {data['company']},\n"
                f"'created_at': {data['created_at']},\n"
                f"'email': {data['email']},\n"
                f"'id': {data['id']},\n"
                f"'name': {data['name']},\n"
                f"'url': {data['url']}")


window = Tk()
window.title("Window Name")
window.geometry('800x600')
window.resizable(width=False, height=False)

label_field = Label(window, text='Enter the repository link', anchor=CENTER)
label_field.pack()

field_link = Entry(window, justify=CENTER, font=('Arial', 15), width=40, background="gray")
field_link.pack()

btn = Button(window, text='Analysis', command=get_data)
btn.pack()

label_result = Label(window, anchor=CENTER)
label_result.pack()


window.mainloop()