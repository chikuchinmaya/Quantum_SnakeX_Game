# 🐍 QuantumSnakeX Game with Sound Using Amazon Q CLI  

A **dynamic AI-powered Snake game** built using **Python and Pygame**, enhanced by **Amazon Q CLI**!  

## 🚀 Features  
✔️ **Generating the initial game logic** using Amazon Q  
✔️ **Fixing errors and debugging** with AI assistance  
✔️ **Adding sound effects** using `pygame.mixer`  
✔️ **Optimizing gameplay speed** for better responsiveness  

Using **Amazon Q CLI**, I efficiently **generated, edited, and refined code** in real time.  

---

## 🔧 Installing Amazon Q  

### 🖥 MacOS  
Run this command in your terminal:  
```bash
brew install amazon-q
```

💻 WSL (Windows Subsystem for Linux)
Download the installation zip file:

```bash
curl --proto '=https' --tlsv1.2 -sSf "https://desktop-release.q.us-east-1.amazonaws.com/latest/q-x86_64-linux.zip" -o "q.zip"
```

Then, run:

```bash
unzip q.zip  
./q/install.sh
```
  
By default, the files are installed to ~/.local/bin.

🐧 Linux (Ubuntu)
Ensure your system is up-to-date and has Libfuse2 installed:

```bash
sudo apt-get update  
sudo apt install libfuse2
```  

Install the Amazon Q Debian package:
```bash
curl --proto '=https' --tlsv1.2 -sSf https://desktop-release.q.us-east-1.amazonaws.com/latest/amazon-q.deb -o amazon-q.deb  
sudo apt install -y ./amazon-q.deb  
```

🔑 Logging Into Amazon Q
Create an AWS Builder ID and log in using:
```bash
q login  
q  
```

🎮 Generating QuantumSnakeX
Here’s the prompt I used to generate the code for the QuantumSnakeX:
```bash
Write a high-quality, minimal, and efficient Python implementation of a greedy snake game, suitable for experienced developers, including only non-obvious comments.
Amazon Q provided a clean, optimized version of the Snake game!
```

🛠 Running QuantumSnakeX
Once you get the generated output, copy the code and paste it in Quantum_SnakeX.py, then run:
```bash
python Quantum_SnakeX.py
```


