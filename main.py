import tkinter as tk

window = tk.Tk()
window.title("File Reading")
window.geometry("650x650")
l = tk.Label(window, text="File Information", font=("Times New Roman", 15))


def read_file():
    textbox.delete("1.0", tk.END)
    with open("C:\\Users\\melik\\Desktop\\Marvel.txt", 'r') as f:
        content = f.read()
        textbox.insert(tk.END, "Marvel file is:\n\n"+content)


def calculate():
    textbox.delete("1.0", tk.END)
    wordList = []
    wordFreqSet = set()
    with open("C:\\Users\\melik\\Desktop\\Marvel.txt", 'r') as f:
        for line in f:
            for word in line.split():
                wordList.append(word)

    for item in range(0, len(wordList)):
        if item not in wordFreqSet:
            item_count = wordList.count(wordList[item])
            wordFreqSet.add(str(str(wordList[item]) + ' = ' + str(item_count)+"\n"))

    content = ""
    for wordFreqItem in wordFreqSet:
        content += wordFreqItem

    textbox.insert(tk.END, "Words With Their Frequencies:\n\n"+content)


textbox = tk.Text(window, font=("Times New Roman", 13), height=27, width=65)

read_btn = tk.Button(window, text="READ", bd=5, command=read_file)
calculate_btn = tk.Button(window, text="CALCULATE", bd=5, command=calculate)

l.pack()
textbox.pack()
read_btn.pack()
calculate_btn.pack()

tk.mainloop()