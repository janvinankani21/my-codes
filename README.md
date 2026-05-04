# Auto-Python-Pusher

Yeh repository ek automated GitHub Actions workflow set up karti hai jo har roz raat 9:00 PM (IST) par ek naya, working Python program generate karta hai aur usko automatically aapke profile par push kar deta hai.

Iska fayda yeh hai ki aapko daily manual push nahi karna padega aur aapki GitHub profile activity roz update hoti rahegi.

## Setup Instructions

Agar aap yeh padh rahe hain, toh iska matlab hai ki Antigravity ne aapke liye yeh project bana diya hai. Ise GitHub par start karne ke liye, bas yeh simple steps follow karein:

1. **Create a new Repository on GitHub**
   - Apne GitHub account mein login karein.
   - Ek naya repository banayein (iske liye plus icon `+` par click karke `New repository` select karein).
   - Repo ka naam kuch bhi rakh sakte hain (e.g., `Daily-Python-Codes`).
   - Ise **Public** ya **Private** banayein (agar aap activity graph mein dikhana chahte hain toh yaad rakhein ki public repo best hoti hai, par private bhi graph mein count hoti hai agar settings mein allowed ho).
   - `Initialize this repository with a README` ko untick rakhein aur "Create repository" par click karein.

2. **Push These Files to Your New GitHub Repository**
   Apne terminal/command prompt mein jahan yeh folder (`Auto-Python-Pusher`) hai, wahan jayen aur yeh commands run karein:

   ```bash
   git init
   git add .
   git commit -m "Initial commit - Auto Pusher Setup"
   git branch -M main
   # Niche diye gaye link ko apne naye repo ke link se replace karein
   git remote add origin https://github.com/AAPKA_USERNAME/AAPKA_REPO_NAME.git
   git push -u origin main
   ```

3. **Enable Workflow (GitHub Actions Permissions)**
   - GitHub pe apne naye repository ki `Settings` mein jayen.
   - Left sidebar se `Actions` -> `General` par click karein.
   - Scroll karke `Workflow permissions` section mein aayen.
   - Wahan **"Read and write permissions"** select karein aur `Save` kar dein. (Yeh bohot zaruri hai, warna GitHub Actions aapke account pe code push nahi kar payega).

## Test Karke Dekhein (Manually Trigger)
1. Apne GitHub repo mein `Actions` tab par click karein.
2. Left side mein `Daily Python Program Pusher` par click karein.
3. Right side mein `Run workflow` ka button dikhega, uspe click karke run karein.
4. Thodi der mein ek naya folder `programs/` ban jayega jisme ek random Python file hoga!

## Yeh Kaise Kaam Karta Hai?
- `generate_code.py`: Isme bohot saare useful Python scripts (jaise Calculator, Password Generator, Fibonacci) ke templates hain. Yeh roz ek random template uthakar nayi file banata hai.
- `.github/workflows/auto_push.yml`: Yeh GitHub Actions ki script hai jo roz 15:30 UTC (9:00 PM IST) ko trigger hoti hai, aur khud-ba-khud code generate karke commit/push karti hai.
